"""
URL configuration for kursova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('стаття', views.стаття, name="стаття"),
    path('реєстрація', views.реєстрація, name="реєстрація"),
    path('вхід', views.вхід, name="вхід"),
    path('вихід', views.вихід, name="вихід"),
    path('особистий_кабінет', views.особистий_кабінет, name="особистий_кабінет"),
    path('про_нас', views.про_нас, name="про_нас"),
]
