from user import user
import random as r
import _sqlite3

sq = _sqlite3.connect("database.sqlite")
s = sq.cursor()
s.execute("SELECT * FROM genres")
newlists = s.fetchall()

newID = input('Insert user ID here. If you are a new user please insert your own unique ID:')
f = open('past_users.txt', 'r')
if f.read().__contains__(newID):
    print('i want out')
else:
    favorite = input('Favorite genre (rap, pop/r&b, jazz, electronic, experimental, rock, metal, folk/country):')
    randomInt = r.randint(0, 22725)
    for list in newlists:
        if list[0] == randomInt:
            print(list)
    new_user = user(newID, favorite)

