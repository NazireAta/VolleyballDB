from django.shortcuts import render, redirect
from django.http import HttpResponse
from volleyball_app.users.login import *
from volleyball_app.users.forms import *

# Create your views here.

def index(request):
    index_text = "view.index function is called"
    context = {'index_text': index_text}
    return render(request,'renders/index.html', context)


def printNumber(request, number):
    numbers = [i for i in range(number, number+5)]
    arr =[]
    for i in range(len(numbers)):
        arr.append({"index": i, "number":numbers[i]})
    return render(request,'renders/numbers.html', {"arr": arr})

def printString(request, string):
    t = string +"512"
    return HttpResponse(f"view.printString function is calledwith number {string} and 5 more is {t}")


def loginIndex(request):
    context = {"login_fail": False, "login_form": LoginForm()}
    return render(request,'volleyball_app/login.html',context)


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    loginCheck = checkCredentials(username,password)
    if(loginCheck=="dbManager"):
        request.session['name'] = username
        return redirect('../dbManager/')
    elif(loginCheck=="coach"):
        request.session['name'] = username
        return redirect('../coach/')
    elif(loginCheck=="jury"):
        request.session['name'] = username
        return redirect('../jury/')
    elif(loginCheck=="player"):
        request.session['name'] = username
        return redirect('../player/')
    context = {"login_fail": True, "login_form": LoginForm()}
    return render(request,'volleyball_app/login.html',context)
    

def home(request):
    name = request.session['name']
    return render(request, 'volleyball_app/home.html', {"name":name})


def dbManagerIndex(request):
    context = {"login_fail": False, 
               "add_player_form": dbManager_addPlayer(),
               "add_coach_form": dbManager_addCoach(),
               "add_jury_form": dbManager_addJury(),
               "update_stadium_name_form": dbManager_update_stadium_name()}
    return render(request,'volleyball_app/dbManager.html',context)

def dbManager(request):
    if request.method == 'POST':
        # Check which form was submitted and process accordingly
        if 'add_player_form' in request.POST:
            form = dbManager_addPlayer(request.POST)
            if form.is_valid():
                # Process the form data and save to database
                ## ELIF BAK
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                height=form.cleaned_data['height'],
                weight=form.cleaned_data['weight']
                ## ELIF BAKMAYI BIRAK 
        elif 'add_coach_form' in request.POST:
            form = dbManager_addCoach(request.POST)
            if form.is_valid():
                # Process the form data and save to database
                ## ELIF BAK
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                nationality=form.cleaned_data['nationality']
                ## ELIF BAKMAYI BIRAK  
        elif 'add_jury_form' in request.POST:
            form = dbManager_addJury(request.POST)
            if form.is_valid():
                # Process the form data and save to database
                ## ELIF BAK
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                nationality=form.cleaned_data['nationality']
                ## ELIF BAKMAYI BIRAK
        elif 'update_stadium_name_form' in request.POST:
            form = dbManager_update_stadium_name(request.POST)
            if form.is_valid():
                # Process the form data and update the stadium name in the database
                ## ELIF BAK
                stadium_id = form.cleaned_data['stadium_id']
                new_stadium_name = form.cleaned_data['stadium_name']
                stadium = Stadium.objects.get(id=stadium_id)
                stadium.stadium_name = new_stadium_name
                ## ELIF BAKMAYI BIRAK
                stadium.save()

    # If the form submission was unsuccessful or it's a GET request, render the dbManager page with empty forms
    context = {
        "add_player_form": dbManager_addPlayer(),
        "add_coach_form": dbManager_addCoach(),
        "add_jury_form": dbManager_addJury(),
        "update_stadium_name_form": dbManager_update_stadium_name()
    }
    return render(request, 'volleyball_app/dbManager.html', context)


def coachIndex(request):
    stadium_list = [[1, "vv","TR"], [2, "ahs","US"], [5, "sada","DE"]] #ELIF BAK example data koydum duzeltilcek
    context = {"login_fail": False, 
               "delete_match_session_form": coach_delete_match_session(),
               "add_match_session_form": coach_add_match_session(),
               "create_squad_form": coach_create_squad(),
                "stadium_list": stadium_list}
    return render(request,'volleyball_app/coach.html',context)


def coach(request):
    stadium_list = [[1, "vv","TR"], [2, "ahs","US"], [5, "sada","DE"]] #ELIF BAK example data koydum duzeltilcek
    if request.method == 'POST':
        # Check which form was submitted and process accordingly
        if 'delete_match_session_form' in request.POST:
            form = coach_delete_match_session(request.POST)
            if form.is_valid():
                # Process the form data and save to database
                ## ELIF BAK
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
                ## ELIF BAKMAYI BIRAK 
        elif 'add_match_session_form' in request.POST:
            form = coach_add_match_session(request.POST)
            if form.is_valid():
                # Process the form data and save to database
                ## ELIF BAK
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
                ## ELIF BAKMAYI BIRAK 
        elif 'create_squad_form' in request.POST:
            form = coach_create_squad(request.POST)
            if form.is_valid():
                # Process the form data and save to database
                ## ELIF BAK
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
                ## ELIF BAKMAYI BIRAK  
    # If the form submission was unsuccessful or it's a GET request, render the dbManager page with empty forms
    context = {
        "delete_match_session_form": coach_delete_match_session(),
        "add_match_session_form": coach_add_match_session(),
        "create_squad_form": coach_create_squad(),
        "stadium_list": stadium_list
    }
    return render(request, 'volleyball_app/coach.html', context)


def juryIndex(request):
    average_rating = 5 # ELIF BAK example value koydum
    count_of_sessions_rated = 10

    context = {"login_fail": False, 
               "average_rating": average_rating,
               "count_of_sessions_rated": count_of_sessions_rated,
               "rate_session_form": jury_rate()
    }
    return render(request,'volleyball_app/jury.html',context)


def jury(request):
    average_rating = 5 # ELIF BAK example value koydum
    count_of_sessions_rated = 10

    if request.method == 'POST':
        # Check which form was submitted and process accordingly
        if 'rate_session_form' in request.POST:
            form = jury_rate(request.POST)
            if form.is_valid():
                # Process the form data and save to database
                ## ELIF BAK
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
                ## ELIF BAKMAYI BIRAK  
        
    # If the form submission was unsuccessful or it's a GET request, render the dbManager page with empty forms
    context = {
        "average_rating": average_rating,
        "count_of_sessions_rated": count_of_sessions_rated,
        "rate_session_form": jury_rate()
    }
    return render(request, 'volleyball_app/jury.html', context)


def playerIndex(request):
    height_player_played_most = 180 # ELIF BAK example value koydum
    player_list = [[1, "elif nur","deniz"], [2, "nazire","ata"], [5, "aydin","ata"]]

    context = {"login_fail": False, 
               "height_player_played_most": height_player_played_most,
               "player_list": player_list
    }
    return render(request,'volleyball_app/player.html',context)


def player(request):
    height_player_played_most = 180 # ELIF BAK example value koydum
    player_list = [[1, "elif nur","deniz"], [2, "nazire","ata"], [5, "aydin","ata"]]

    if request.method == 'POST':
        # Check which form was submitted and process accordingly
        if 'rate_session_form' in request.POST:
            form = jury_rate(request.POST)
            if form.is_valid():
                # Process the form data and save to database
                ## ELIF BAK
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
                ## ELIF BAKMAYI BIRAK  
        
    # If the form submission was unsuccessful or it's a GET request, render the dbManager page with empty forms
    context = {
        "height_player_played_most": height_player_played_most,
               "player_list": player_list
    }
    return render(request, 'volleyball_app/player.html', context)