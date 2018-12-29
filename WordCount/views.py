from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home1.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for w in wordlist:
        if w in worddict:
            worddict[w] +=1
        else:
            worddict[w] = 1

    return render(request,'count.html',{'f':fulltext,'l':len(wordlist),'d':worddict})
    #pass

def about(request):
    return render(request,'about.html')
