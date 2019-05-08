import db_creation_fnc as database

db = database.DB()

'''
Sign up a user. Insertion in login table and in user table

returns user_id
'''
def createUser(email,password,name,surname,birthday,nationality,url_picture,languages_list=[],interests_list=[]):
    loginuser=[(email,password)]
    user_id = db.insert_in_table("login",loginuser)

    user=[(name,surname,birthday,nationality,url_picture,languages_list=[],interests_list=[])]
    user_id = db.insert_in_table("user",user)
    return user_id

def updateProfile(name,surname,birthday,nationality,url_picture,languages_list=[],interests_list=[]):
    return

'''
Checks in login table whether a row with email and password exits

@param email
@param password

returns user_id
'''
def login(email,password):
    return

'''
gets the list of conversations that the user has

@param user_id
returns result: conversations
'''
def getListChats(user_id):
    where = "where user_id1 = " + user_id + " OR user_id2 = " + user_id
    result = db.select_from_table("conversation",where_condition = where, return_value = "rowcount" )
    return result

'''
gets messages in a conversation

returns result: messages
'''
def getChatMessages(conv_id):
    where = "conv_id = " + conv_id
    result = db.select_from_table("message",where_condition=where)
    return result

def addMessage(conv_id, user_id, text, url_resource=""):
    return

def getUserInfo(user_id):
    return
