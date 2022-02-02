from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'feature/magic_page.html')


def dashboard(request):
    return render(request, 'feature/dashboard.html')


def hundred(request):
    return render(request, 'feature/hundred.html')


def bestof(request):
    return render(request, 'feature/bestof.html')


def moreof(request):
    return render(request, 'feature/moreof.html')


def story(request):
    return render(request, 'feature/story.html')
