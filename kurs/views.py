from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import RegistrationForm
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, "kursova.html", {'articles': articles})

def стаття(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {'article': article})

def реєстрація(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("вхід"))
    else:
            form = RegistrationForm()
    return render(request, "registration.html", {'form': form})


def особистий_кабінет(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("вхід"))
    return render(request, "user.html")

def вхід(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("особистий_кабінет"))
        else:
            return render(request, "login.html", {"message": "Error"})
    return render(request, "login.html")

def вихід(request):
    logout(request)
    return render(request, "login.html")

def про_нас(request):
    return render(request, "about_us.html")
