import db_creation_fnc as database

db = database.DB(db="data")
# db = database.DB("AP2pUlIJEe", "remotemysql.com",
#                  3306, "AP2pUlIJEe", "1zP34rKdgi")


# TODO connection integrity issue create user updatelocation

'''
Sign up a user. Insertion in login table and in user table

returns user_id
'''


def createUser(email, password, name, surname, birthday, nationality, url_picture, lat, lon, languages_list="languages", interests_list="interests"):
    loginuser = [(email, password)]
    user_id = db.insert_in_table("login", loginuser, columns="(mail,password)")

    user = [(name, surname, birthday, nationality,
             url_picture, languages_list, interests_list)]
    user_id = db.insert_in_table(
        "user", user, columns="(name,surname,birthday,nationality,url_picture,languages_list,interests_list)")

    updateLocation(user_id, lat, lon)

    return user_id


def updateProfile(user_id, name, surname, birthday, nationality, url_picture, languages_list="languages", interests_list="interests"):
    user_id = db.select_from_table(
        "user", where_condition="user_id = '" + user_id + "'")
    return user_id


'''
Checks in login table whether a row with email and password exits

@param email
@param password

returns user_id
'''


def login(email, password):
    user_id = db.select_from_table(
        "login", where_condition="mail = '" + email + "' AND password = '" + password + "'")

    if user_id != []:
        print(user_id)
        return user_id
    else:
        return None


'''
add conversation
'''


def addChat(user_id1, user_id2):
    conv_info = [(user_id1, user_id2)]
    conv_id = db.insert_in_table(
        "conversation", conv_info, columns="(user_id1,user_id2)")
    return conv_id


'''
gets the list of conversations that the user has

@param user_id
returns result: conversations
'''


def getListChats(user_id):
    where = "user_id1 = " + user_id + " OR user_id2 = " + user_id
    result = db.select_from_table(
        "conversation", where_condition=where, multiple=True)
    return result


'''
gets messages in a conversation

@param conv_id : id of the conversation
returns result: messages
'''


def getChatMessages(conv_id):
    where = "conv_id = " + str(conv_id)
    result = db.select_from_table("message", where_condition=where)
    return result


'''
sends a message to a conversation

@param conv_id
@param sender_user_id
@param text
@param url_resource

returns mes_id : id of the message
'''


def addMessage(conv_id, sender_user_id, text, url_resource=""):
    message = [(conv_id, sender_user_id, text, url_resource)]
    mes_id = db.insert_in_table(
        "message", message, columns="(conv_id,sender_user_id,text,url_resource)")
    return mes_id


def getUserInfo(user_id):
    where = "user_id = " + str(user_id)
    user_info = db.select_from_table("user", where_condition=where)
    return user_info


'''
update user's location
'''


def updateLocation(user_id, lat, lon):
    print((lat, lon))
    db.update_table("locations", ["lat", "lon"],
                    (lat, lon), "user_id = " + str(user_id))
    return user_id


'''
search people

@param user_id, lat, lon
@returns list_people: [{userinfos...},{userinfos...}]
'''

# TODO: only one result is returned ("fetch_one" in select_from_table) and order depending on distance range


def searchPeople(user_id, lat, lon):
    list_people = db.select_from_table("user", multiple=True)
    return list_people
