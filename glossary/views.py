import string
from django.shortcuts import render, render_to_response, redirect
from .models import Glossary

def append(request):
    return render(request, 'append.html')


def appendArticle(request):
    if not request.user.is_authenticated:
        return redirect("/")
    # Todo 형태소 분석기 사용
    # https://www.lucypark.kr/courses/2015-dm/text-mining.html
    not_letters = u'!"#%\'()*+,-./:;<=>?@&[\]^_`{|}~1234567890'
    table = dict((ord(char), ' ') for char in not_letters)
    article = request.POST['article'].lower().translate(table)
    occurrences = {}
    for w in article.split(' '):
        occurrences[w] = occurrences.get(w, 0) + 1

    # reset_isNew()
    for w in occurrences.keys():
        try:
            t = Glossary.objects.filter(account=request.user).get(word=w)
        except (KeyError, Glossary.DoesNotExist):
            newGlossary = Glossary(word=w, account=request.user)
            newGlossary.frequency = occurrences.get(w, 0)
            newGlossary.isShow = True
            newGlossary.isNew = True
            newGlossary.save()
        else:
            t.frequency += occurrences.get(w, 0)
            t.save()

    return redirect(reverse('glossary.views.new_list'))
