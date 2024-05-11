def checkCredentials(username, password):
    print(username)
    if(username=="dbManager"): # if username in username list AND if password matches
        print(1)
        return "dbManager"
    if(username=="coach"): # if username in username list and if password matches
        return "coach"
    if(username=="jury"): # if username in username list and if password matches
        return "jury"
    if(username=="player"): # if username in username list and if password matches
        return "player"
    return False
