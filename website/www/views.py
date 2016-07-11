from django.shortcuts import render
from django.core.files import File
from helper import markdownify

def index(request):
    body  = markdownify("index")
    return render(request, 'layout/body_face.html', {'content':body})


def overview(request):
    title = "overview"
    body = markdownify("overview")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def source(request):
    title = "source code"
    body = markdownify("source")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def get_started(request):
    title = "get started"
    body = markdownify("get_started")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def api(request):
    title = "API"
    body = markdownify("api")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def download(request):
    title = "download"
    body = markdownify("download")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def contact(request):
    title = "contact"
    body = markdownify("contact")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def manual(request):
    title = "manual"
    body = markdownify("manual")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})
