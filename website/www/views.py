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


def platform(request):
    title = "supported platforms"
    body = markdownify("platform")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def install(request):
    title = "install"
    body = markdownify("install")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def api(request):
    title = "api & docs"
    body = markdownify("api")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def tutorial(request):
    title = "tutorials"
    body = markdownify("tutorial")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def contact(request):
    title = "contact"
    body = markdownify("contact")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def example(request):
    title = "examples & use cases"
    body = markdownify("example")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})
