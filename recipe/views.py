from django.shortcuts import render,redirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RecipeSerializer
def index(req):
    allrecipe = Recipe.objects.all()
    context = {"allrecipe": allrecipe}
    return render(req, "index.html", context)

def allrecipe(req):
    query = req.GET.get('search', '')
    if query:
        allrecipe = Recipe.objects.filter(
            name__icontains=query
        ) | Recipe.objects.filter(
            recipeid__icontains=query
        )
    else:
        allrecipe = Recipe.objects.all()
    
    context = {"allrecipe": allrecipe}
    return render(req, "allrecipe.html", context)

def registerrecipe(req):
    if req.method == "GET":
        context = {}
        form = RecipeForm()
        context["form"] = form
        return render(req, "registerrecipe.html", context)
    else:
        context = {}
        form = RecipeForm(req.POST, req.FILES or None)
        if form.is_valid():
            form.save()
        context["form"] = form
        return redirect("/allrecipe")


def updaterecipe(req, recipeid):
    reciperecord = Recipe.objects.get(recipeid=recipeid)
    if req.method == "POST":
        form = RecipeForm(req.POST, req.FILES, instance=reciperecord)
        if form.is_valid():
            form.save()
            return redirect("/allrecipe")
    else:
        form = RecipeForm(instance=reciperecord)

    context = {"form": form, "reciperecord": reciperecord}
    return render(req, "updaterecipe.html", context)


def deleterecipe(req, recipeid):
    reciperecord = Recipe.objects.get(recipeid=recipeid)
    reciperecord.delete()
    return redirect("/allrecipe")





def signin(req):
    return render(req, "signin.html")


def signup(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        ucpass = req.POST["ucpass"]
        context = {}

        if uname == "" or upass == "" or ucpass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signup.html", context)
        elif upass != ucpass:
            context["errmsg"] = "Password and confirm password doesn't match"
            return render(req, "signup.html", context)
        else:
            try:
                userdata = User.objects.create(username=uname, password=upass)
                userdata.set_password(upass)
                userdata.save()
                return redirect("/signin")
            except:
                context["errmsg"] = "User Already exists"
                return render(req, "signup.html", context)
    else:
        context = {}
        context["errmsg"] = ""
        return render(req, "signup.html", context)


from django.contrib.auth import authenticate, login, logout


def signin(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        context = {}
        if uname == "" or upass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signin.html", context)
        else:
            userdata = authenticate(username=uname, password=upass)
            if userdata is not None:
                login(req, userdata)
                return redirect("/allrecipe")
            else:
                context["errmsg"] = "Invalid username and password"
                return render(req, "signin.html", context)
    else:
        return render(req, "signin.html")


def userlogout(req):
    logout(req)
    return redirect("/")

class RecipeListView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


