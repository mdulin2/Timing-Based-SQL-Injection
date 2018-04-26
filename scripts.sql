--scrips used in order to create the database

CREATE TABLE Login (
    user VARCHAR(50),
    password VARCHAR(50),
    PRIMARY KEY user
);

CREATE TABLE Blog (
    post_ID int AUTO_INCREMENT,
    user VARCHAR(50),
    title VARCHAR(400),
    post TEXT,
    PRIMARY KEY(post_ID),
    FOREIGN KEY (user) REFERENCES Login(user)
)

INSERT INTO Login(user,password) VALUES("yangerbanger","damson!")

INSERT INTO Blog(user,title,post) VALUES(some_val,username in Login,"string","string")

INSERT INTO Blog(user, title,post) VALUES("yangerbanger","Colorado","My home...this is where I go")
