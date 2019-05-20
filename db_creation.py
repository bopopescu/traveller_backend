import db_creation_fnc as database

db_man = database.DB_Manager("remotemysql.com",3306,"AP2pUlIJEe","1zP34rKdgi")

db = database.DB("AP2pUlIJEe","remotemysql.com",3306,"AP2pUlIJEe","1zP34rKdgi")

db.create_table("login",
["user_id int NOT NULL AUTO_INCREMENT PRIMARY KEY",
"mail VARCHAR(255) NOT NULL UNIQUE",
"password VARCHAR(255) NOT NULL"
])

db.create_table("user",
["user_id int AUTO_INCREMENT PRIMARY KEY",
"surname VARCHAR(255) NOT NULL",
"name VARCHAR(255) NOT NULL",
"birthday DATE NOT NULL",
"nationality VARCHAR(255) NOT NULL",
"url_picture VARCHAR(255) NOT NULL",
"languages_list VARCHAR(255)",
"interests_list VARCHAR(255)",
],"FOREIGN KEY (user_id) REFERENCES login (user_id)")

db.create_table("conversation",
["conv_id int NOT NULL AUTO_INCREMENT PRIMARY KEY",
"user_id1 int NOT NULL",
"user_id2 int NOT NULL"
],"FOREIGN KEY (user_id1) REFERENCES user(user_id), FOREIGN KEY (user_id2) REFERENCES user(user_id)")

db.create_table("message",
["mes_id int NOT NULL AUTO_INCREMENT PRIMARY KEY",
"conv_id int NOT NULL",
"sender_user_id int NOT NULL",
"text VARCHAR(255) NOT NULL",
"url_resource VARCHAR(255)"
], "FOREIGN KEY (conv_id) REFERENCES conversation(conv_id)")

db.create_table("locations",
["user_id int NOT NULL PRIMARY KEY",
"lat float NOT NULL", 
"lon float NOT NULL"],
"FOREIGN KEY (user_id) REFERENCES login(user_id)")


