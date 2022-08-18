import csv
from cs50 import SQL

open ("songs.db","w").close # creates the db file

database = SQL("sqlite:///songs.db") #v locates the path for the database

database.execute("""CREATE TABLE tracks (
    track_id INTEGER PRIMARY KEY,
    title TEXT,
    year TEXT,
    length TEXT
    );""")

database.execute("""CREATE TABLE genres (
    genre_id INTEGER PRIMARY KEY,
    genre TEXT,
    track_id INTEGER,
    FOREIGN KEY (track_id) REFERENCES tracks(track_id)
    );""")

database.execute("""CREATE TABLE artist (
    artist_id INTEGER PRIMARY KEY,
    artist_name TEXT
    );""")

database.execute("""CREATE TABLE Ranking (
    track_id INTEGER,
    energy TEXT,
    danceability TEXT,
    liveness TEXT,
    populalities TEXT,
    artist_id INTEGER,
    FOREIGN KEY (track_id) REFERENCES tracks(track_id),
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
    );""")

with open ("songs.csv","r") as file:  # opens the csv in read mode
    reader = csv.DictReader(file)

    for row in reader:
        title = row["title"].strip().capitalize()
        year = row["year"] 
        length = row["length"]
        genre_name = row["top genre"]
        Name = row["artist"]
        energy = row["energy"]
        dance = row["danceability"]
        liveness = row["liveness"]
        popularities = row["popularity"]
        database.execute("INSERT INTO tracks (title,year,length) VALUES (?,?,?)",title,year,length)  #inserting data into the tracks table
        database.execute("INSERT INTO genres (genre,track_id) VALUES (?,(SELECT track_id FROM tracks WHERE title = ?))",genre_name,title)  #inserting data into the genres table
        database.execute("INSERT INTO artist (artist_name) VALUES (?)",Name)   #inserting data into the artists table
        database.execute("INSERT INTO Ranking (track_id,energy,danceability,liveness,populalities,artist_id) VALUES ((SELECT track_id FROM tracks WHERE title = ?),?,?,?,?,(SELECT artist_id FROM artist WHERE artist_name = ?))",title,energy,dance,liveness,popularities,Name)