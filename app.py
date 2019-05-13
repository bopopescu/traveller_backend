
import db_actions
from db_actions import createUser,updateProfile, getUserInfo, login, getListChats, getChatMessages
from flask import Flask,session,request,render_template


app = Flask(__name__)

#TODO session['user_id'] = [] ????

@app.route('/')
def hello_world():
   if 'user_id' in session:
      user_id = session['user_id']
      return "logged as " + str(user_id)
   else:
      return "not logged"

@app.route('/searchpeople')
def searchpeople():
   return 'TBD'

'''
create new user
'''

@app.route('/createprofile', methods = ['GET', 'POST'])
def create_profile():
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      name = request.form['name']
      surname = request.form['surname']
      birthday = request.form['birthday']
      nationality = request.form['nationality']
      url_picture = request.form['url_picture']
      user_id = createUser(email,password,name,surname,birthday,nationality,url_picture)
      session['user_id'] = user_id
      return 'logged in'
   else:
      return 'create profile'

'''
update profile
'''

@app.route('/updateprofile', methods = ['GET', 'POST'])
def update_profile():
   if 'user_id' in session:
      user_id = session['user_id']
      if request.method == 'POST':
         email = request.form['email']
         password = request.form['password']
         name = request.form['name']
         surname = request.form['surname']
         birthday = request.values['birthday']
         nationality = request.form['nationality']
         url_picture = request.form['url_picture']
         picture = request.files.get('file')
         updateProfile(user_id,email,password,name,surname,birthday,nationality,url_picture)
         return getUserInfo(user_id)
      else:
         return 'profile'
   else:
      return 'not logged'


'''
Login
'''
@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      user_id = db_actions.login(email,password)
      if user_id != None and user_id != []:
         session['user_id'] = user_id
         return 'Logged in'
      else:
         return 'wrong email or password'
   else:
      return 'login'

'''
Logout
'''
@app.route('/logout')
def logout():
   if 'user_id' in session:
      session.pop('user_id', None)
      return 'logged out'
   else:
      return 'not logged'

'''
Gets messages of a conversation
'''
@app.route('/getchatmessages')
def get_chat_messages():
   if 'conv_id' in session:
      conv_id = session['conv_id']
      chats = getChatMessages(conv_id)
      return chats
   else:
      return 'no chat selected'

'''
get list of user's chats
'''
@app.route('/getlistchats')
def get_list_chats():
   if 'user_id' in session:
      chats = getListChats(session['user_id'])
      return chats
   else:
      return 'not logged'

'''
send message
'''

@app.route('/addmessage', methods = ['GET', 'POST'])
def send_message():
   if request.method == 'POST':
      if 'conv_id' in session and 'user_id' in session:
         conv_id = session['conv_id']
         user_id = session['user_id']
         text = request.form['text']
         url_resource = request.form['url_resource']
         mes_id = addMessage(conv_id,user_id,text,url_resource)
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
         return 'user id is not valid'
   else:
      return 'not logged'

#=================TESTSSSSS===========
@app.route('/testcreateprofile', methods = ['GET', 'POST'])
def test_create_profile():
   return render_template('test_createprofile.html')

@app.route('/testlogin', methods = ['GET', 'POST'])
def test_login():
   if 'user_id' in session:
      return 'already logged in'
   else:
      return render_template('test_login.html')

@app.route('/testlogout', methods = ['GET', 'POST'])
def test_logout():
   return render_template('test_logout.html')

@app.route('/testgetlistchats', methods = ['GET', 'POST'])
def test_get_list_chats():
   return render_template('test_getlistchats.html')

@app.route('/testgetuserinfo', methods = ['GET', 'POST'])
def test_get_user_info():
   return render_template('test_getuserinfo.html')
   

if __name__ == '__main__':
   app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
   app.run(debug = True)
