from django.shortcuts import render
from django.core.files import File
from helper import markdownify

def index(request):
    body  = markdownify("index")
    return render(request, 'layout/body_face.html', {'content':body})


def overview(request):
    title = "OVERVIEW"
    body = markdownify("overview")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def platform(request):
    title = "SUPPORTED PLATFORMS"
    body = markdownify("platform")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def install(request):
    title = "INSTALL"
    body = markdownify("install")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def api(request):
    title = "API & DOCS"
    body = markdownify("api")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def contact(request):
    title = "CONTACT"
    body = markdownify("contact")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def learn(request):
    title = "LEARN"
    body = markdownify("learn")
    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def example(request, example=None):
    if example is None:
        title = "EXAMPLES"
        body = markdownify("example")
    else:
        title = "EXAMPLE"
        body = markdownify("examples/{}".format(example))

    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def tutorial(request, tutorial=None):
    if tutorial is None:
        title = "TUTORIALS"
        body = markdownify("tutorial")
    else:
        title = "TUTORIAL"
        body = markdownify("tutorials/{}".format(tutorial))

    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})


def case(request, case=None):
    if case is None:
        title = "CASES"
        body = markdownify("case")
    else:
        title = "CASE"
        body = markdownify("cases/{}".format(case))

    return render(request, 'layout/body_inside.html', {'content':body, 'title':title})
