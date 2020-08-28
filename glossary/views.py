from django.shortcuts import render, redirect
from nltk.tokenize import RegexpTokenizer
from newspaper import Article
from PIL import Image
from pytesseract import pytesseract
from django.core.files.storage import FileSystemStorage
import PyPDF2

from django.conf import settings
# from django.conf.urls.static import static

from .models import Glossary


def tokenize_and_save(request, article):
    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    not_letters = u'$!"#%\'()*+,-./:;<=>?@&[\]^_`{|}~1234567890 \t’‘\n\r¶★”“«—¥Ó©óò'
    table = dict((ord(char), ' ') for char in not_letters)
    a = article.lower().translate(table)
    result = tokenizer.tokenize(a)

    occurrences = {}

    for i in result:
        occurrences[i] = occurrences.get(i, 0) + 1

    # reset_isNew()
    for w in occurrences.keys():
        try:
            t = Glossary.objects.filter(account=request.user).get(word=w)
        except (KeyError, Glossary.DoesNotExist):
            new_glossary = Glossary(word=w, account=request.user)
            new_glossary.frequency = occurrences.get(w, 0)
            new_glossary.isShow = True
            new_glossary.isNew = True
            new_glossary.save()
        else:
            t.frequency += occurrences.get(w, 0)
            t.save()


def append(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        return render(request, 'append.html')


def test_root():
    return redirect('/')


def append_url(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        try:
            url = request.GET['target_url']
            article = Article(url)
            article.download()
            article.parse()
            tokenize_and_save(request, article.text)
            return redirect('glossary:new_list')
        except Exception:
            return redirect('glossary:append')


def append_image(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        try:
            if request.method == 'POST' and request.FILES['image_file']:
                tempfile = request.FILES['image_file']
                fs = FileSystemStorage()
                filename = fs.save(tempfile.name, tempfile)
                aa = settings.MEDIA_ROOT + "/" + filename
                im = Image.open(aa)
                article = pytesseract.image_to_string(im)
                fs.delete(aa)
                tokenize_and_save(request, article)
                return redirect('glossary:new_list')
            else:
                return redirect('glossary:append')
        except Exception:
            return redirect('glossary:append')


def append_document(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        try:
            if request.method == 'POST' and request.FILES['document_file']:
                tempfile = request.FILES['document_file'].name.lower()
                if tempfile.endswith('.txt'):
                    # 텍스트 파일로 처리한다.
                    text_process(request)
                    return redirect('glossary:new_list')
                elif tempfile.endswith('.pdf'):
                    # PDF 파일로 처리한다.
                    pdf_process(request)
                    return redirect('glossary:new_list')
                else:
                    # 처리하지 않고 끝낸다.
                    return redirect('glossary:append')
            else:
                return redirect('glossary:append')
        except Exception:
            return redirect('glossary:append')


def append_article(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        # 형태소 분석기 사용
        # https://www.lucypark.kr/courses/2015-dm/text-mining.html
        try:
            if request.method == 'POST' and request.POST['article']:
                tokenize_and_save(request, request.POST['article'])
                return redirect('glossary:new_list')
            else:
                return redirect('glossary:append')
        except Exception:
            return redirect('glossary:append')


def get_total_count(glossary_obj, user):
    return glossary_obj.filter(account=user).count()


def to_remember_list(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        glossary_obj = Glossary.objects
        glossary_list = glossary_obj.filter(
            isShow=True,
            account=request.user).order_by('-frequency', 'word')[:5000]
        total_count = get_total_count(glossary_obj, request.user)
        to_remember_count = glossary_list.count()
        remembered_count = total_count - to_remember_count
        hidden_flag = False
        new_flag = 'F'
        return render(
            request,
            "list.html",
            {'glossary_list': glossary_list,
             'hidden_flag': hidden_flag,
             'new_flag': new_flag,
             'total_count': total_count,
             'remembered_count': remembered_count,
             'to_remember_count': to_remember_count}, )


def new_list(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        glossary_list = Glossary.objects.filter(
            isShow=True,
            isNew=True,
            account=request.user).order_by('-frequency', 'word')[:5000]
        hidden_flag = False
        new_flag = 'T'
        return render(request,
                      'list.html',
                      {'glossary_list': glossary_list,
                       'hidden_flag': hidden_flag,
                       'new_flag': new_flag})


def hide(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        t = Glossary.objects.filter(
            account=request.user).get(word=request.GET['w'])
        t.isShow = False
        t.save()
        if request.GET['new'] == 'T':
            return redirect('glossary:new_list')
        else:
            return redirect('glossary:to_remember_list')


def show(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        t = Glossary.objects.filter(
            account=request.user).get(word=request.GET['w'])
        t.isShow = True
        t.save()
        return redirect('glossary:remembered_list')


def remembered_list(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        glossary_obj = Glossary.objects
        glossary_list = glossary_obj.filter(
            isShow=False,
            account=request.user).order_by('-frequency', 'word')[:5000]
        total_count = get_total_count(glossary_obj, request.user)
        remembered_count = glossary_list.count()
        to_remember_count = total_count - remembered_count
        hidden_flag = True
        new_flag = 'F'
        return render(request, 'list.html',
                      {'glossary_list': glossary_list,
                       'hidden_flag': hidden_flag,
                       'new_flag': new_flag,
                       'total_count': total_count,
                       'remembered_count': remembered_count,
                       'to_remember_count': to_remember_count})


def memory(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        glossary_list = Glossary.objects.filter(
            isShow=True,
            account=request.user).order_by('-frequency', 'word')[:5000]
        hidden_flag = False
        new_flag = 'F'
        return render(request, 'memory.html',
                      {'glossary_list': glossary_list,
                       'hidden_flag': hidden_flag,
                       'new_flag': new_flag})


def delete_all(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        t = Glossary.objects.filter(account=request.user)
        t.delete()
        return redirect('glossary:to_remember_list')


def delete_word(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        t = Glossary.objects.filter(
            account=request.user).get(word=request.GET['w'])
        t.delete()
        return redirect('glossary:remembered_list')


def text_process(request):
    tempfile = request.FILES['document_file']
    fs = FileSystemStorage()
    filename = fs.save(tempfile.name, tempfile)
    aa = settings.MEDIA_ROOT + "/" + filename

    f = open(aa, mode='rt', encoding='utf-8')
    for line in f:
        tokenize_and_save(request, line)
    f.close()
    fs.delete(aa)


def pdf_process(request):
    tempfile = request.FILES['document_file']
    fs = FileSystemStorage()
    filename = fs.save(tempfile.name, tempfile)
    aa = settings.MEDIA_ROOT + "/" + filename

    file_object = open(aa, "rb")
    pfr = PyPDF2.PdfFileReader(file_object)

    for page in range(pfr.numPages):
        page_object = pfr.getPage(page)
        tokenize_and_save(request, page_object.extractText())

    file_object.close()
    fs.delete(aa)
