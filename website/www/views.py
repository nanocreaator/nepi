from django.shortcuts import render
from django.core.files import File
from helper import markdownify

def index(request):
    body  = markdownify("index")
    return render(request, 'layout/body_face.html', {'content':body})


def source(request):
    title = "source code"
    body = markdownify("source")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})
