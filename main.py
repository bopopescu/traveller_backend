import db_actions
from db_actions import createUser, updateProfile, getUserInfo, login, getListChats, getChatMessages, updateLocation, addMessage, searchPeople
from flask import Flask, session, request, render_template, jsonify
from flask_cors import CORS, cross_origin
import json


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    if 'user_id' in session:
        user_id = session['user_id']
        return "logged as " + str(user_id)
    else:
        return "not logged"


@app.route('/searchpeople', methods=['GET', 'POST'])
def search_people():
    if request.method == 'POST':
        content = request.get_json(force=True)
        user_id = content['user_id']
        lat = content['lat']
        lon = content['lon']

        result = searchPeople(user_id, lat, lon)
        response = jsonify(result)
        return response


'''
create new user
'''


@app.route('/createprofile', methods=['GET', 'POST'])
@cross_origin()
def create_profile():
    if request.method == 'POST':
        content = request.get_json(force=True)

        email = content['email']
        password = content['password']
        name = content['name']
        surname = content['surname']
        birthday = content['birthday']
        nationality = content['nationality']
        url_picture = content['url_picture']
        lat = content['lat']
        lon = content['lon']

        user_id = createUser(email, password, name, surname,
                             birthday, nationality, url_picture, lat, lon)
        session['user_id'] = user_id

        # updateLocation(user_id,lat,lon)

        response = jsonify(str(user_id))
        print(response)

        return response
    else:
        return 'create profile'


'''
update profile
'''


@app.route('/updateprofile', methods=['GET', 'POST'])
def update_profile():
    if 'user_id' in session:
        user_id = session['user_id']
        if request.method == 'POST':
            content = request.get_json(force=True)

            email = content['email']
            password = content['password']
            name = content['name']
            surname = content['surname']
            birthday = content['birthday']
            nationality = content['nationality']
            url_picture = content['url_picture']

            # email = request.form['email']
            # password = request.form['password']
            # name = request.form['name']
            # surname = request.form['surname']
            # birthday = request.values['birthday']
            # nationality = request.form['nationality']
            # url_picture = request.form['url_picture']
            # picture = request.files.get('file')
            updateProfile(user_id, email, password, name, surname,
                          birthday, nationality, url_picture)
            return getUserInfo(user_id)
        else:
            return 'profile'
    else:
        return 'NOT_LOGGED'


'''
Login
'''
@app.route('/login', methods=['GET', 'POST'])
def login_1():
    if request.method == 'POST':
        content = request.get_json(force=True)

        email = content['email']
        password = content['password']

        result = db_actions.login(email, password)
        user_id = result['user_id']

        lat = content['lat']
        lon = content['lon']

        if user_id != None and user_id != []:
            session['user_id'] = user_id
            # updateLocation(user_id,lat,lon)
            response = jsonify(user_id)

            return response
        else:
            return 'wrong email or password'
    else:
        return 'login'


'''
Logout
'''
@app.route('/logout')
def logout():
    print(session.get('user_id'))
    if 'user_id' in session:
        session.pop('user_id', None)
        return 'logged out'
    else:
        return 'not logged'


'''
Gets messages of a conversation
'''
@app.route('/getchatmessages', methods=['GET', 'POST'])
def get_chat_messages():
    if request.method == 'POST':
        if 'conv_id' in session:
            conv_id = session['conv_id']
            chats = getChatMessages(conv_id)
            return chats
        else:
            return 'no chat selected'
    else:
        return 'getchatmessages'


'''
get list of user's chats
'''
# TODO solve persistance session
@app.route('/getlistchats/', methods=['GET', 'POST'])
def get_list_chats():
    if request.method == 'POST':
        if 'user_id' in session:
            chats = getListChats(session['user_id'])
            return chats
        else:
            content = request.get_json(force=True)
            user_id = content['user_id']
            chats = getListChats(user_id)

            conversations = []
            for chat in chats:
                if chat['user_id1'] != user_id:
                    name = getUserInfo(chat['user_id2'])['name']
                else:
                    name = getUserInfo(chat['user_id1'])['name']

                conv = {'conv_id': chat['conv_id'], 'name': name}
                conversations.append(conv)

            response = jsonify(conversations)
            return response
    else:
        return 'lala'


'''
send message
'''


@app.route('/addmessage', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        if 'conv_id' in session and 'user_id' in session:
            conv_id = session['conv_id']
            user_id = session['user_id']
            text = request.form['text']
            url_resource = request.form['url_resource']
            mes_id = addMessage(conv_id, user_id, text, url_resource)
            return mes_id
        else:
            return 'no chat selected/not logged'


@app.route('/getuserinfo/<user>')
def get_user_info(user):
    if 'user_id' in session:
        print(session['user_id'])
        user_info = getUserInfo(user)
        if user_info != None:
            return str(user_info)
        else:
            return 'ID_NOT_VALID'
    else:
        return 'NOT_LOGGED'

# =================TESTSSSSS===========
@app.route('/testcreateprofile', methods=['GET', 'POST'])
def test_create_profile():
    return render_template('test_createprofile.html')


@app.route('/testlogin', methods=['GET', 'POST'])
def test_login():
    if 'user_id' in session:
        return 'already logged in'
    else:
        return render_template('test_login.html')


@app.route('/testlogout', methods=['GET', 'POST'])
def test_logout():
    return render_template('test_logout.html')


@app.route('/testgetlistchats', methods=['GET', 'POST'])
def test_get_list_chats():
    return render_template('test_getlistchats.html')


@app.route('/testgetuserinfo', methods=['GET', 'POST'])
def test_get_user_info():
    return render_template('test_getuserinfo.html')


@app.route('/testsearchpeople', methods=['GET', 'POST'])
def test_search_people():
    return render_template('test_searchpeople.html')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


if __name__ == '__main__':
    app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"
    app.run(debug=True)
