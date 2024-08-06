"""
URL configuration for recipemanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from recipe import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from recipe.views import RecipeListView, RecipeDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('allrecipe/', views.allrecipe, name='allrecipe'),
    path('registerrecipe/', views.registerrecipe, name='registerrecipe'),
    path('updaterecipe/<int:recipeid>/', views.updaterecipe, name='updaterecipe'),
    path('deleterecipe/<int:recipeid>/', views.deleterecipe, name='deleterecipe'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

