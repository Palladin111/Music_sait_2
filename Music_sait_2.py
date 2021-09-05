import sqlalchemy

# создаем подключение к базе данных
engine = sqlalchemy.create_engine('postgresql://naum_1:123456@localhost:5432/music_sait_2')
connection = engine.connect()

# запрос - название и год выхода альбомов, вышедших в 2018 году
print(connection.execute("""SELECT title, year_of_issue FROM albums WHERE year_of_issue = 2018;""").fetchall())

# запрос - название и продолжительность самого длительного трека
print(connection.execute("""SELECT name_track, duration FROM tracks WHERE duration = 
(SELECT MAX(duration) FROM tracks);""").fetchall())

# запрос - название треков, продолжительность которых не менее 3,5 минуты
print(connection.execute("""SELECT name_track FROM tracks WHERE duration >= 210;""").fetchall())

# запрос - названия сборников, вышедших в период с 2018 по 2020 год включительно
print(connection.execute("""SELECT title FROM collections WHERE year_of_issue BETWEEN 2018 AND 2020;""").fetchall())

# запрос - исполнители, чье имя состоит из 1 слова
print(connection.execute("""SELECT name FROM performers WHERE name NOT  LIKE '%% %%';""").fetchall())

# запрос - название треков, которые содержат слово "мой"/"my"
print(connection.execute("""SELECT name_track FROM tracks WHERE lower(name_track) LIKE '%%my%%';""").fetchall())