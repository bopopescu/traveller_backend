
from db_actions import createUser,updateProfile, getUserInfo, login, getListChats, getChatMessages
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   if 'user_id' in session:
      user_id = session['user_id']
      return "logged as " + user_id
   else:
      return "not logged"

@app.route('/searchpeople')
def searchpeople():
   return 'Hello World’

'''
create new user
'''
#TODO add variables
@app.route('/createprofile', methods = ['GET', 'POST'])
def create_profile():
   if request.method == 'POST':
      user_id = createUser("email","password","name","surname","1998-11-06","nationality","url_picture")
      session['user_id'] = user_id
      return 'logged in'

'''
update profile
'''
#TODO add variables
@app.route('/updateprofile', methods = ['GET', 'POST'])
def update_profile():
   if 'user_id' in session:
      user_id = session['user_id']
      if request.method == 'POST':
         updateProfile(user_id,"email","password","nameUpdated","surname","birthday","nationality","url_picture")
         return getUserInfo(user_id)
   else:
      return 'not logged'


'''
Login
'''
#TODO: add variables and if condition not correct
@app.route('/login', methods = ['GET', 'POST'])
def hello_world():
   if request.method == 'POST':
      user_id = login("email","password")
      session['user_id'] = user_id
      return 'Logged in’

'''
Logout
'''
@app.route('/logout')
def hello_world():
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
def hello_world():
   if 'user_id' in session:
      chats = getListChats(session['user_id'])
      return chats
   else:
      return 'not logged'

#TODO add variables
@app.route('/addmessage', methods = ['GET', 'POST'])
def hello_world():
   return 'Hello World’

@app.route('/getuserinfo')
def hello_world():
   return 'Hello World’

if __name__ == '__main__':
   app.run()
