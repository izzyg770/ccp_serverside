PRAGMA foreign_keys = ON;

CREATE TABLE users (
    username VARCHAR(20) NOT NULL PRIMARY KEY,
    fullname VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL,
    filename VARCHAR(64) NOT NULL,
    alt VARCHAR(256) NOT NULL,
    password VARCHAR(256) NOT NULL
);

CREATE TABLE pets (
    petid INTEGER PRIMARY KEY AUTOINCREMENT,
    petname VARCHAR(64) NOT NULL,
    filename VARCHAR(64) NOT NULL,
    alt VARCHAR(256) NOT NULL,
    owner VARCHAR(20) NOT NULL,
    FOREIGN KEY (owner) REFERENCES users(username) ON DELETE CASCADE
);

CREATE TABLE pet_likes (
    petlikeid INTEGER PRIMARY KEY AUTOINCREMENT,
    petid INTEGER NOT NULL,
    text VARCHAR (40) NOT NULL,
    FOREIGN KEY (petid) REFERENCES pets(petid) ON DELETE CASCADE
);

CREATE TABLE pet_blurbs (
    petblurbid INTEGER PRIMARY KEY AUTOINCREMENT,
    petid INTEGER NOT NULL,
    text VARCHAR(20000) NOT NULL,
    FOREIGN KEY (petid) REFERENCES pets(petid) ON DELETE CASCADE
);

CREATE TABLE pet_media (
    petmediaid INTEGER PRIMARY KEY AUTOINCREMENT,
    petid INTEGER NOT NULL,
    filename VARCHAR(64) NOT NULL,
    alt VARCHAR(256) NOT NULL,
    FOREIGN KEY (petid) REFERENCES pets(petid) ON DELETE CASCADE
);

CREATE TABLE recipes (
    recipeid INTEGER PRIMARY KEY AUTOINCREMENT,
    recipename VARCHAR(64) NOT NULL,
    origin VARCHAR(20) NOT NULL,
    source VARCHAR(20) NOT NULL,
    category VARCHAR(20) NOT NULL,
    filename VARCHAR(64) NOT NULL,
    alt VARCHAR(256) NOT NULL,
    owner VARCHAR(20) NOT NULL,
    FOREIGN KEY (owner) REFERENCES users(username) ON DELETE CASCADE
);

CREATE TABLE recipe_blurbs (
    recipeblurbid INTEGER PRIMARY KEY AUTOINCREMENT,
    recipeid INTEGER NOT NULL,
    text VARCHAR(10000) NOT NULL,
    FOREIGN KEY (recipeid) REFERENCES recipes(recipeid) ON DELETE CASCADE
);

CREATE TABLE ingredients (
    ingredientid INTEGER PRIMARY KEY AUTOINCREMENT,
    recipeid INTEGER NOT NULL,
    text VARCHAR(1024) NOT NULL,
    FOREIGN KEY (recipeid) REFERENCES recipes(recipeid) ON DELETE CASCADE
);

CREATE TABLE steps (
    stepid INTEGER PRIMARY KEY AUTOINCREMENT,
    recipeid INTEGER NOT NULL,
    text VARCHAR(1024) NOT NULL,
    FOREIGN KEY (recipeid) REFERENCES recipes(recipeid) ON DELETE CASCADE
);

CREATE TABLE recipe_media (
    recipemediaid INTEGER PRIMARY KEY AUTOINCREMENT,
    recipeid INTEGER NOT NULL,
    filename VARCHAR(64) NOT NULL,
    alt VARCHAR(256) NOT NULL,
    FOREIGN KEY (recipeid) REFERENCES recipes(recipeid) ON DELETE CASCADE
);

CREATE TABLE travel (
    travelid INTEGER PRIMARY KEY AUTOINCREMENT,
    travelname VARCHAR(40) NOT NULL,
    location VARCHAR(60) NOT NULL,
    owner VARCHAR(20) NOT NULL,
    FOREIGN KEY (owner) REFERENCES users(username) ON DELETE CASCADE
);

CREATE TABLE travel_main (
    mainid INTEGER PRIMARY KEY AUTOINCREMENT,
    travelid INTEGER NOT NULL,
    still VARCHAR(64) NOT NULL,
    moving VARCHAR(64) NOT NULL,
    alt VARCHAR(256) NOT NULL,
    FOREIGN KEY (travelid) REFERENCES travel(travelid) ON DELETE CASCADE
);

CREATE TABLE travel_blurbs (
    travelblurbid INTEGER PRIMARY KEY AUTOINCREMENT,
    travelid INTEGER NOT NULL,
    text VARCHAR(10000) NOT NULL,
    FOREIGN KEY (travelid) REFERENCES travel(travelid) ON DELETE CASCADE
);

CREATE TABLE travel_media (
    travelmediaid INTEGER PRIMARY KEY AUTOINCREMENT,
    travelid INTEGER NOT NULL,
    filename VARCHAR(64) NOT NULL,
    alt VARCHAR(256) NOT NULL,
    caption VARCHAR(10000) NOT NULL,
    FOREIGN KEY (travelid) REFERENCES travel(travelid) ON DELETE CASCADE
);

CREATE TABLE following (
  username1 VARCHAR(20) NOT NULL,
  username2 VARCHAR(20) NOT NULL,
  PRIMARY KEY (username1, username2),
  FOREIGN KEY (username1) REFERENCES users(username) ON DELETE CASCADE,
  FOREIGN KEY (username2) REFERENCES users(username) ON DELETE CASCADE
);
