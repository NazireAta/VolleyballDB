from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))


class dbManager_addPlayer(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date of Birth'}))
    height = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Height'}))
    weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Weight'}))
    positions = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Positions'}))
    team_ID = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Team ID'}))


class dbManager_addCoach(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nationality'}))


class dbManager_addJury(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nationality'}))

class dbManager_update_stadium_name(forms.Form):
    stadium_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Stadium ID'}))
    stadium_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Stadium Name'}))

class coach_delete_match_session(forms.Form):
    session_ID = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Session ID'}))

class coach_add_match_session(forms.Form): # session id increment et
    session_ID = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Session ID'}))
    team_ID = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Team ID'}))
    stadium_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Stadium ID'}))
    time_slot = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Time Slot'}))
    date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date'}))
    jury_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Jury Name'}))
    jury_surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Jury Surname'}))
    #assigned_jury_username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Assigned Jury Username'}))
    #rating null olacak bunu formda almiyoruz

class coach_create_squad(forms.Form):
    session_ID = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Session ID'}))
    player1_username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 1 Username'}))
    player1_position = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 1 Position'}))
    player2_username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 2 Username'}))
    player2_position = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 2 Position'}))
    player3_username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 3 Username'}))
    player3_position = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 3 Position'}))
    player4_username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 4 Username'}))
    player4_position = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 4 Position'}))
    player5_username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 5 Username'}))
    player5_position = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 5 Position'}))
    player6_username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 6 Username'}))
    player6_position = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player 6 Position'}))

class jury_rate(forms.Form):
    session_ID = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Session ID'}))
    rating = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Rating'}))

