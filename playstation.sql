create table games(
    title varchar(250) PRIMARY KEY,
    console varchar(250),
    year int,
    developer varchar(250)
);

insert into games (title, console, year, developer) values ('Uncharted 2: Among Thieves', 'PlayStation 3', 2009, 'Naughty Dog');
insert into games (title, console, year, developer) values ('Red Dead Redemption 2', 'PlayStation 4', 2019, 'Rockstar');
insert into games (title, console, year, developer) values ('Yakuza: Like A Dragon', 'PlayStation 5', 2021, 'Ryu Ga Gotoku');
insert into games (title, console, year, developer) values ('Supermarket Shriek', 'PlayStation 4', 2020, 'Billy Goat Entertainment Ltd');
insert into games (title, console, year, developer) values ('F1 2021', 'PlayStation 5', 2021, 'Codemasters');