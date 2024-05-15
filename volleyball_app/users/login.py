import mysql.connector
# Create your views here.
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="volleydb"
)
mycursor = mydb.cursor()
def checkCredentials(username, password):
    mycursor.execute("SELECT * FROM Database_Manager")
    db_mng_list = mycursor.fetchall()
    for db_mng in db_mng_list:
        if(username==db_mng[0] and password==db_mng[1]): # if username in username list AND if password matches
            return "dbManager"
        
    mycursor.execute("SELECT username, password FROM Coach")
    coach_list = mycursor.fetchall()
    for coach in coach_list:
        if(username==coach[0] and password==coach[1]): # if username in username list AND if password matches
            return "coach"
    mycursor.execute("SELECT username, password FROM Jury")
    jury_list = mycursor.fetchall()
    for jury in jury_list:
        if(username==jury[0] and password==jury[1]): # if username in username list AND if password matches
            return "jury"
    mycursor.execute("SELECT username, password FROM Player")
    player_list = mycursor.fetchall()
    for player in player_list:
        if(username==player[0] and password==player[1]): # if username in username list AND if password matches
            return "player"
    return False
