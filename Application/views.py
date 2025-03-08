from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime

from .models import User, Category, JournalLog

# Allows the user to log in
def login_view(request):

    # POST - allows the user to login via a form
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        # If successful, redirects to the homepage, otherwise displays an error message
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "application/login.html", {
                "message_red_alert": "Invalid username or password."
            })
    # GET - displays the login page
    else:
        return render(request, "application/login.html")


# Allows the user to register as a new user
def register(request):

    # POST - allows user to register via a form
    if request.method == "POST":

        # Gets all information about the new user
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation, otherwise returns an error message
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "application/register.html", {
                "message_red_alert": "Passwords must match."
            })

        # Attempt to create new user (sees if user already exists), otherwise returns an error message
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "application/register.html", {
                "message_red_alert": "Username already taken."
            })
        
        # Logs the user in and redirects them to the homepage
        login(request, user)
    # GET - displays the register new user page
    else:
        return render(request, "application/register.html")


# Allows the user to log out
@login_required(login_url='login')
def logout_view(request):
    return HttpResponseRedirect(reverse("login"))


# Homepage
def homepage(request):
    return render(request, "application/homepage.html")


# Response page
def response(request):
    print("hello")


# History category page
def history_render_category(request):
    categories = Category.objects.all()

    if request.method == "POST":
        # get category id from user selection
        category_name = request.POST.get("category")

        # category idt_object_or_404(Category, id=category_id)

        # Render the new page, passing the selected category to the template
        return render(request, "application/history-category.html", {
            "category": category  # Pass the selected category to the template
        })
    else:
        return render(request, "application/history-category.html")



# Past entries page
def past_entries(request):
    print("hello")



