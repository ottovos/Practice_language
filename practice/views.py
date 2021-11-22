from django.shortcuts import render
from . models import Language, Words
from django.http import HttpResponse

def practiceWords(request):
    all_words_list = Words.objects.order_by()
    context = {'all_words_list': all_words_list}
    return render(request, 'practice/practice.html', context)

def addWords(request):
    # return HttpResponse('Later you will find here the choice of language to practice with')
    return render(request, 'practice/addWords.html')



