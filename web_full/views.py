from django.shortcuts import render


def index_view(request):
    return render(request, 'web/index.html', {})


def about(request):
    return render(request, 'web/about.html', {})


def tutorial(request):
    return render(request, 'web/tutorial.html', {})


def contact(request):
    return render(request, 'web/contact.html', {})
