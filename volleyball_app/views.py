from django.shortcuts import render, redirect
from django.http import HttpResponse
from volleyball_app.users.login import *
from volleyball_app.users.forms import *
import mysql.connector
from volleyball_app.models import *
from django.contrib.auth.decorators import login_required
from .models import MatchSession

# Create your views here.
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="volleydb"
    )
mycursor = mydb.cursor()
cur_user = ""
cur_role = ""

def index(request):
    context = {"login_fail": False, "login_form": LoginForm()}
    return render(request,'volleyball_app/login.html',context)


def loginIndex(request):
    context = {"login_fail": False, "login_form": LoginForm()}
    return render(request,'volleyball_app/login.html',context)


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    loginCheck = checkCredentials(username,password)
    global cur_user
    cur_user = username
    global cur_role
    cur_role = loginCheck
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
    cur_role = ""
    cur_user = ""
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
               "update_stadium_name_form": dbManager_update_stadium_name(),
               "error_message": None}
    return render(request,'volleyball_app/dbManager.html',context)


def dbManager(request):
    context = {
        "add_player_form": dbManager_addPlayer(),
        "add_coach_form": dbManager_addCoach(),
        "add_jury_form": dbManager_addJury(),
        "update_stadium_name_form": dbManager_update_stadium_name(),
        "error_message": None,
        "argument_value": None
    }
    if request.method == 'POST':
        # Check which form was submitted and process accordingly
        argument_value = request.POST.get('argument_name')
        try:
            if cur_role != "dbManager":
                error_message = "You are not authorized to access this page."
                print(error_message)
                context['error_message'] = error_message
                context['argument_value'] = argument_value
                return render(request, 'volleyball_app/dbManager.html', context)
            if argument_value == 'player':
                form = dbManager_addPlayer(request.POST)
                if form.is_valid():
                    # Process the form data and save to database
                    
                    username=form.cleaned_data['username']
                    password=form.cleaned_data['password']
                    name=form.cleaned_data['name']
                    surname=form.cleaned_data['surname']
                    date_of_birth=form.cleaned_data['date_of_birth']
                    height=form.cleaned_data['height']
                    weight=form.cleaned_data['weight']
                    print(username, password, name, surname, date_of_birth, height, weight)
                    sql = "INSERT INTO player (username, password, name, surname, date_of_birth, height, weight) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (username, password, name, surname, date_of_birth, height, weight)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted. ")
                    sql = "DELETE FROM match_session WHERE session_id = %s"
            elif(argument_value == 'coach'):
                form = dbManager_addCoach(request.POST)
                if form.is_valid():
                    # Process the form data and save to database
                    
                    username=form.cleaned_data['username']
                    password=form.cleaned_data['password']
                    name=form.cleaned_data['name']
                    surname=form.cleaned_data['surname']
                    nationality=form.cleaned_data['nationality']
                    sql = "INSERT INTO coach (username, password, name, surname, nationality) VALUES (%s, %s, %s, %s, %s)"
                    val = (username, password, name, surname, nationality)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted. ")
                    sql = "DELETE FROM match_session WHERE session_id = %s" 
            elif(argument_value == 'jury'):
                form = dbManager_addJury(request.POST)
                if form.is_valid():
                    # Process the form data and save to database
                    username=form.cleaned_data['username']
                    password=form.cleaned_data['password']
                    name=form.cleaned_data['name']
                    surname=form.cleaned_data['surname']
                    nationality=form.cleaned_data['nationality']
                    sql = "INSERT INTO jury (username, password, name, surname, nationality) VALUES (%s, %s, %s, %s, %s)"
                    val = (username, password, name, surname, nationality)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted. ")
                #elif 'update_stadium_name_form' in request.POST:
            elif(argument_value == 'stadium'):
                form = dbManager_update_stadium_name(request.POST)
                if form.is_valid():
                    # Process the form data and update the stadium name in the database
                    stadium_id = form.cleaned_data['stadium_id']
                    new_stadium_name = form.cleaned_data['stadium_name']
                    #stadium = Stadium.objects.get(stadium_id=stadium_id)
                    #stadium.stadium_name = new_stadium_name
                    sql = "UPDATE stadium SET stadium_name = %s WHERE stadium_id = %s"
                    val = (new_stadium_name, stadium_id)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record updated. ")
                    if(mycursor.rowcount==0):
                        error_message = "Couldn't find a stadium with the given ID."
                        print(error_message)
                        context['error_message'] = error_message 
                        context['argument_value'] = argument_value
                        return render(request, 'volleyball_app/dbManager.html', context)
                    #stadium.save()
        except mysql.connector.Error as error:
            error_message = "Failed due to {}".format(error)
            print(error_message)
            context['error_message'] = error_message 
            context['argument_value'] = argument_value
    # If the form submission was unsuccessful or it's a GET request, render the dbManager page with empty forms
    return render(request, 'volleyball_app/dbManager.html', context)


def coachIndex(request):
    sql="Select * from stadium"
    mycursor.execute(sql)
    stadium_list = mycursor.fetchall()
    context = {"login_fail": False, 
               "delete_match_session_form": coach_delete_match_session(),
               "add_match_session_form": coach_add_match_session(),
               "create_squad_form": coach_create_squad(),
                "stadium_list": stadium_list,
                "error_message": None}
    return render(request,'volleyball_app/coach.html',context)


def coach(request):
    sql="Select * from stadium"
    mycursor.execute(sql)
    stadium_list = mycursor.fetchall()
    context = {
        "delete_match_session_form": coach_delete_match_session(),
        "add_match_session_form": coach_add_match_session(),
        "create_squad_form": coach_create_squad(),
        "stadium_list": stadium_list,
        "error_message": None,
        "argument_value": None
    }
    if request.method == 'POST':
        argument_value = request.POST.get('argument_name')
        try:
            if cur_role != "coach":
                error_message = "You are not authorized to access this page."
                print(error_message)
                context['error_message'] = error_message
                context['argument_value'] = argument_value
                return render(request, 'volleyball_app/dbManager.html', context)
            if argument_value == 'delete_match':
            # Check which form was submitted and process accordingly
                form = coach_delete_match_session(request.POST)
                if form.is_valid():
                    # Process the form data and save to database
                    session_id=form.cleaned_data['session_ID']
                    sql="DELETE FROM sessionsquads WHERE session_id = %s"
                    val = (session_id,)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    row_count=mycursor.rowcount
                    sql = "DELETE FROM match_session WHERE session_ID = %s"
                    val = (session_id,)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(row_count+mycursor.rowcount, "record deleted. ")
            elif argument_value == 'add_match':                             #conflictlere bak
                form = coach_add_match_session(request.POST)
                if form.is_valid():
                    # Process the form data and save to database
                    session_ID = form.cleaned_data['session_ID']
                    team_ID = int(form.cleaned_data['team_ID'])          
                    stadium_id = form.cleaned_data['stadium_id']
                    time_slot = form.cleaned_data['time_slot']
                    date = form.cleaned_data['date']
                    jury_name = form.cleaned_data['jury_name']
                    jury_surname = form.cleaned_data['jury_surname']
                    sql = "SELECT username FROM jury WHERE name = '{}' AND surname = '{}'".format(jury_name, jury_surname)
                    mycursor.execute(sql)
                    jury_username = mycursor.fetchall()
                    if len(jury_username) == 0:
                        error_message = "Couldn't find a jury with the given name and surname."
                        print(error_message)
                        context['error_message'] = error_message 
                        context['argument_value'] = argument_value
                        return render(request, 'volleyball_app/coach.html', context)
                    assigned_jury_username = jury_username[0][0]

                    cur_user = request.session.get('name')
                    mycursor.execute("SELECT team_ID FROM Team WHERE coach_username = '{}' AND CURDATE() BETWEEN STR_TO_DATE(contract_start, '%d.%m.%Y') AND STR_TO_DATE(contract_finish, '%d.%m.%Y');".format(cur_user))  
                    team_ID_list = mycursor.fetchall()
                    print(team_ID_list)
                    if len(team_ID_list) == 0:
                        error_message = "Couldn't find a team for the user."
                        print(error_message)
                        context['error_message'] = error_message 
                        context['argument_value'] = argument_value
                        return render(request, 'volleyball_app/coach.html', context)
                    team_ID_=int(team_ID_list[0][0])
                    if team_ID != team_ID_: 
                        error_message = "You can only add match sessions for your own team."
                        print(error_message)
                        context['error_message'] = error_message 
                        return render(request, 'volleyball_app/coach.html', context)
                    sql = "INSERT INTO match_session (session_ID, team_ID, stadium_id, time_slot, date, assigned_jury_username) VALUES (%s, %s, %s, %s, %s, %s)"
                    val = (session_ID, team_ID, stadium_id, time_slot, date, assigned_jury_username)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted. ")
            elif argument_value == 'squad':
                form = coach_create_squad(request.POST)
                if form.is_valid():
                    # Process the form data and save to database
                    session_ID = form.cleaned_data['session_ID']
                    player1_username = form.cleaned_data['player1_username']
                    player1_position = form.cleaned_data['player1_position']
                    player2_username = form.cleaned_data['player2_username']
                    player2_position = form.cleaned_data['player2_position']
                    player3_username = form.cleaned_data['player3_username']
                    player3_position = form.cleaned_data['player3_position']
                    player4_username = form.cleaned_data['player4_username']
                    player4_position = form.cleaned_data['player4_position']
                    player5_username = form.cleaned_data['player5_username']
                    player5_position = form.cleaned_data['player5_position']
                    player6_username = form.cleaned_data['player6_username']
                    player6_position = form.cleaned_data['player6_position']
                    sql = "SELECT count(*) FROM sessionsquads WHERE session_ID = '{}'".format(session_ID)
                    mycursor.execute(sql)
                    count = mycursor.fetchall()[0][0]
                    print(count)
                    if count != 0:
                        error_message = "A squad has already been created for this session."
                        print(error_message)
                        context['error_message'] = error_message 
                        context['argument_value'] = argument_value
                        return render(request, 'volleyball_app/coach.html', context)
                    sql = "Insert into sessionsquads (session_ID, played_player_username, position_id) values (%s, %s, %s)"
                    val = (session_ID, player1_username, player1_position)
                    mycursor.execute(sql, val)
                    #mydb.commit()
                    val = (session_ID, player2_username, player2_position)
                    mycursor.execute(sql, val)
                    #mydb.commit()
                    val = (session_ID, player3_username, player3_position)
                    mycursor.execute(sql, val)
                    #mydb.commit()
                    val = (session_ID, player4_username, player4_position)
                    mycursor.execute(sql, val)
                    #mydb.commit()
                    val = (session_ID, player5_username, player5_position)
                    mycursor.execute(sql, val)
                    #mydb.commit()
                    val = (session_ID, player6_username, player6_position)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted. ")
        except mysql.connector.Error as error:
            error_message = "Failed due to {}".format(error)
            print(error_message)
            context['error_message'] = error_message 
            context['argument_value'] = argument_value
    # If the form submission was unsuccessful or it's a GET request, render the dbManager page with empty forms
    return render(request, 'volleyball_app/coach.html', context)


def juryIndex(request):
    cur_user = request.session.get('name')
    mycursor.execute("select avg(rating) from match_session where assigned_jury_username='{}'".format(cur_user)) 
    average_rating = mycursor.fetchall()[0][0]

    mycursor.execute("select count(rating) from match_session where assigned_jury_username='{}'".format(cur_user))  
    count_rating = mycursor.fetchall()[0][0]

    context = {"login_fail": False, 
               "average_rating": average_rating,
               "count_of_sessions_rated": count_rating,
               "rate_session_form": jury_rate(),
               "error_message": None
    }
    return render(request,'volleyball_app/jury.html',context)


def jury(request):
    cur_user = request.session.get('name')
    mycursor.execute("select avg(rating) from match_session where assigned_jury_username='{}'".format(cur_user))  #jury name i nerden alcam
    average_rating = mycursor.fetchall()[0][0]
    mycursor.execute("select count(rating) from match_session where assigned_jury_username='{}'".format(cur_user))  
    count_rating = mycursor.fetchall()[0][0]
    context = {
        "average_rating": average_rating,
        "count_of_sessions_rated": count_rating,
        "rate_session_form": jury_rate(),
        "error_message": None,
        "argument_value": None
    }
    if request.method == 'POST':
        argument_value = request.POST.get('argument_name')
        try:
            if cur_role != "jury":
                error_message = "You are not authorized to access this page."
                print(error_message)
                context['error_message'] = error_message
                context['argument_value'] = argument_value
                return render(request, 'volleyball_app/dbManager.html', context)
            # Check which form was submitted and process accordingly
            if argument_value == 'rate':
                form = jury_rate(request.POST)
                if form.is_valid():
                    # Process the form data and save to database
                    session_ID=int(form.cleaned_data['session_ID'])
                    rating=form.cleaned_data['rating']

                    sql = "SELECT session_id FROM match_session WHERE assigned_jury_username = '{}'".format(cur_user)
                    mycursor.execute(sql)
                    session_IDs = mycursor.fetchall()
                    session_IDs = list(session_IDs)
                    is_present = False
                    for i in session_IDs:
                        if session_ID==i[0]:
                            is_present = True
                            print("present")
                            break
                    if not is_present:
                        error_message = "You can only rate sessions that you have been assigned to."
                        context['error_message'] = error_message
                        print("You can only rate sessions that you have been assigned to.")
                        return render(request, 'volleyball_app/jury.html', context)
                    sql = "update match_session set rating = %s where session_ID = %s"           # triggerlar eklencek
                    val = (rating, session_ID)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record updated. ") 
        except mysql.connector.Error as error:
            error_message = "Failed due to {}".format(error)
            print(error_message)
            context['error_message'] = error_message 
    # If the form submission was unsuccessful or it's a GET request, render the dbManager page with empty forms
    return render(request, 'volleyball_app/jury.html', context)


def playerIndex(request):
    cur_user = request.session.get('name')
    sql= "with PlayerCounts as( select p.username, p.height, count(*) as played_count FROM Player p JOIN SessionSquads s ON p.username = s.played_player_username where s.played_player_username!='{}' and s.session_ID in (select distinct session_id from sessionsquads where played_player_username='{}') group by p.username) select avg(pc.height) from PlayerCounts pc where played_count like (select count(*) as played_count FROM Player p JOIN SessionSquads s ON p.username = s.played_player_username where s.played_player_username!='{}' and s.session_ID in (select distinct session_id from sessionsquads where played_player_username='{}') group by p.username order by played_count desc limit 1)".format(cur_user,cur_user,cur_user,cur_user)
    mycursor.execute(sql)
    height_player_played_most = mycursor.fetchall()[0][0]
    sql="select distinct p.username, p.name, p.surname FROM Player p JOIN SessionSquads s ON p.username = s.played_player_username where s.played_player_username!='{}' and s.session_ID in (select distinct session_id from sessionsquads where played_player_username='{}')".format(cur_user,cur_user)
    mycursor.execute(sql)
    player_list = mycursor.fetchall()

    context = {"login_fail": False, 
               "height_player_played_most": height_player_played_most,
               "player_list": player_list,
                "error_message": None
    }
    return render(request,'volleyball_app/player.html',context)


def player(request):
    cur_user = request.session.get('name')
    sql= "with PlayerCounts as( select p.username, p.height, count(*) as played_count FROM Player p JOIN SessionSquads s ON p.username = s.played_player_username where s.played_player_username!='{}' and s.session_ID in (select distinct session_id from sessionsquads where played_player_username='{}') group by p.username) select avg(pc.height) from PlayerCounts pc where played_count like (select count(*) as played_count FROM Player p JOIN SessionSquads s ON p.username = s.played_player_username where s.played_player_username!='{}' and s.session_ID in (select distinct session_id from sessionsquads where played_player_username='{}') group by p.username order by played_count desc limit 1)".format(cur_user,cur_user,cur_user,cur_user)
    mycursor.execute(sql)
    height_player_played_most = mycursor.fetchall()[0][0]
    sql="select distinct p.username, p.name, p.surname FROM Player p JOIN SessionSquads s ON p.username = s.played_player_username where s.played_player_username!='{}' and s.session_ID in (select distinct session_id from sessionsquads where played_player_username='{}')".format(cur_user,cur_user)
    mycursor.execute(sql)
    player_list = mycursor.fetchall()
        
    # If it's a GET request, render the dbManager page with empty forms
    context = {
        "height_player_played_most": height_player_played_most,
               "player_list": player_list,
                "error_message": None
    }
    return render(request, 'volleyball_app/player.html', context)