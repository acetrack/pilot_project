import string
from django.shortcuts import render, redirect
from nltk.tokenize import RegexpTokenizer
from newspaper import Article
from PIL import Image
from pytesseract import pytesseract
from django.core.files.storage import FileSystemStorage


from django.conf import settings
# from django.conf.urls.static import static

from .models import Glossary


def tokenize(request, article):
    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    not_letters = u'$!"#%\'()*+,-./:;<=>?@&[\]^_`{|}~1234567890 \t’‘\n\r'
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
    if not request.user.is_authenticated():
        return redirect("/")
    else:
        return render(request, 'append.html')


def append_url(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        url = request.POST['target_url']
        article = Article(url)
        article.download()
        article.parse()
        tokenize(request, article.text)
        return redirect('glossary:new_list')


def append_image(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST' and request.FILES['image_file']:
            tempfile = request.FILES['image_file']
            fs = FileSystemStorage()
            filename = fs.save(tempfile.name, tempfile)
            aa = settings.MEDIA_ROOT + "/" + filename
            im = Image.open(aa)
            article = pytesseract.image_to_string(im)
            fs.delete(aa)
            tokenize(request, article)
            return redirect('glossary:new_list')
        else:
            return redirect('glossary:append')


def append_article(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        # Todo 형태소 분석기 사용
        # https://www.lucypark.kr/courses/2015-dm/text-mining.html
        tokenize(request, request.POST['article'])
        return redirect('glossary:new_list')


def list(request):
    if not request.user.is_authenticated():
        return redirect("/")
    else:
        glossary_list = Glossary.objects.filter(
            isShow=True,
            account=request.user).order_by('-frequency', 'word')[:5000]
        hidden_flag = False
        new_flag = 'F'
        return render(
            request,
            "list.html",
            {'glossary_list': glossary_list,
             'hidden_flag': hidden_flag,
             'new_flag': new_flag})


def new_list(request):
    if not request.user.is_authenticated():
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
    if not request.user.is_authenticated():
        return redirect("/")
    else:
        t = Glossary.objects.filter(
            account=request.user).get(word=request.GET['w'])
        t.isShow = False
        t.save()
        if request.GET['new'] == 'T':
            return redirect('glossary:new_list')
        else:
            return redirect('glossary:list')


def show(request):
    if not request.user.is_authenticated():
        return redirect("/")
    else:
        t = Glossary.objects.filter(
            account=request.user).get(word = request.GET['w'])
        t.isShow = True
        t.save()
        return redirect('glossary:hidden_list')


def hidden_list(request):
    if not request.user.is_authenticated():
        return redirect("/")
    else:
        glossary_list = Glossary.objects.filter(
            isShow=False,
            account=request.user).order_by('-frequency', 'word')[:5000]
        hidden_flag = True
        new_flag = 'F'
        return render(request, 'list.html',
                      {'glossary_list': glossary_list,
                       'hidden_flag': hidden_flag,
                       'new_flag': new_flag})


def memory(request):
    if not request.user.is_authenticated():
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
