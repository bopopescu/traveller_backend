INSERT INTO data.login(mail,password) VALUES ("chiara@email.com","password");
INSERT INTO data.login(mail,password) VALUES ("michela@email.com","password");
INSERT INTO data.login(mail,password) VALUES ("fede@email.com","password");

INSERT INTO data.user (name,surname,birthday,nationality,url_picture,languages_list,interests_list) VALUES ("Chiara","Masci","1998/11/06","italian","avatar.jpg","italian,english","electronics,climbing,subway");
INSERT INTO data.user (name,surname,birthday,nationality,url_picture,languages_list,interests_list) VALUES ("Michela","Sbetta","1998/10/31","italian","avatar.jpg","italian,english","harry potter,pizza");
INSERT INTO data.user (name,surname,birthday,nationality,url_picture,languages_list,interests_list) VALUES ("Federica","Fiore","1997/05/19","italian","avatar.jpg","italian,english","tv series,food");

INSERT INTO data.locations (user_id,lat,lon) VALUES (1,46,11);
INSERT INTO data.locations (user_id,lat,lon) VALUES (2,46,11);
INSERT INTO data.locations (user_id,lat,lon) VALUES (3,46,11);

INSERT INTO data.conversation (user_id1,user_id2) VALUES (1,2);
INSERT INTO data.conversation (user_id1,user_id2) VALUES (1,3);
INSERT INTO data.conversation (user_id1,user_id2) VALUES (2,3);