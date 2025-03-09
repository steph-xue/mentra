from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
from google import genai
from django.shortcuts import render, get_object_or_404, redirect
import os

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
        return redirect("homepage")
    # GET - displays the register new user page
    else:
        return render(request, "application/register.html")


# Allows the user to log out
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect("login")


# Homepage
def homepage(request):
    # POST - allows user to input via form
    print(request)
    if request.method == "POST":

        user_story = request.POST.get("user_story")
        category = request.POST.get("category")
        category_data = Category.objects.get(category_name=category)

        print("hi")

        # Call API to get response
        api_response = get_api_response(category_data, user_story)
        print("hello")

         # Create journal log object
        journal_log_data = JournalLog(
            input=user_story,
            output=api_response,
            category=category_data,
            date_time=datetime.datetime.now()
        )

        # Save journal log object to the database
        journal_log_data.save()

        # Print journal log data for debugging
        print("Journal Log Created:", journal_log_data)

        # Store the journal log ID in session
        request.session["journal_log_id"] = journal_log_data.id 

        return HttpResponseRedirect(reverse("response"))

    # GET - renders the homepage
    else:
        categories = Category.objects.all()
        return render(request, "application/homepage.html", {
                "categories": categories  
            })


# Response page
def response(request):
    journal_log_id = request.session.get("journal_log_id")

    journal_log_data = None
    if journal_log_id:
        try:
            journal_log_data = JournalLog.objects.get(id=journal_log_id)
        except JournalLog.DoesNotExist:
            journal_log_data = None  # Handle missing entry gracefully

    return render(request, "application/response.html", {
        "journal_log": journal_log_data,
    })




def history_render_category(request):
    categories = Category.objects.all()

    # POST - allows user to input via form
    if request.method == "POST":

        # get category id from user selection
        category_id = request.POST.get("category")
        category = get_object_or_404(Category, id=category_id)

        # Render the new page, passing the selected category to the template
        return render(request, "application/history-render.html", {
            "category": category  
        })
    else:
        return render(request, "application/history-category.html", {
                "categories": categories  
            })
        


# Past entries page
def past_entries(request, category):

    journal_entries = JournalLog.objects.filter(category=category)

    return render(request, "application/history-render.html",  {
        "category": category,
        "journal_entries": journal_entries
    })
   


def get_api_response(category, user_story):

    category_prompt = ""

    if category.category_name == "Supportive":  
            category_prompt = "Provide an empathetic and encouraging response to this journal entry."
    elif category.category_name == "Insightful":
            category_prompt = "Analyze this journal entry and provide thoughtful reflections."
    elif category.category_name == "Actionable":
            category_prompt = "Suggest SMART goals or actionable steps based on this journal entry with refernences to helpful links."

    #retrive API key
    api_key = os.getenv("API_KEY")

    if not api_key:
            print("Api key is missing")
            return "API key is missing."

    client = genai.Client(api_key=api_key)

    inputs = [category_prompt, user_story]
    print(inputs)

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=inputs,
        )

        if response.text:
            return response.text
        else: 
            return "No content returned from the API"

    except Exception as e:
        return "An error occured"


        