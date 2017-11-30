import string
from django.shortcuts import render, redirect
from nltk.tokenize import RegexpTokenizer
from .models import Glossary


def append(request):
    if not request.user.is_authenticated():
        return redirect("/")
    else:
        return render(request, 'append.html')


def append_article(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        # Todo 형태소 분석기 사용
        # https://www.lucypark.kr/courses/2015-dm/text-mining.html
        tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
        not_letters = u'$!"#%\'()*+,-./:;<=>?@&[\]^_`{|}~1234567890 '
        table = dict((ord(char), ' ') for char in not_letters)
        article = request.POST['article'].lower().translate(table)
        result = tokenizer.tokenize(article)

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
