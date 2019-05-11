import unittest
from db_actions import createUser,updateProfile,login,addChat,getListChats,addMessage,getChatMessages, getUserInfo

class DBActionsTest(unittest.TestCase):
    def test_createUser(self):
        user_id = createUser("email","password","name","surname","1998-11-06","nationality","url_picture")
        self.assertEqual(user_id,1)
    
    def test_updateProfile(self):
        user_id = updateProfile('1',"email","password","nameUpdated","surname","birthday","nationality","url_picture")
        self.assertEqual(user_id,'1')

    def test_login(self):
        user_id = login("email","password")
        self.assertEqual(user_id,'1')

    def test_addChat(self):
        conv_id = addChat('1','2')
        self.assertEqual(conv_id,1)

    def test_getListChats(self):
        conversations = getListChats('1')
        print(conversations)

    def test_addMessage(self):
        mes_id = addMessage('3','1',"text","url_resource")
        self.assertEqual(mes_id,'1')

    def test_getChatMessages(self):
        messages = getChatMessages(1)
        print(messages)

    def test_getUserInfo(self):
        user_info = getUserInfo('1')
        print(user_info)


if __name__ == '__main__':
    unittest.main()