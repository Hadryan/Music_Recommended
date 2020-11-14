import _sqlite3

sq = _sqlite3.connect("database.sqlite")
s = sq.cursor()
s.execute("SELECT * FROM genres")
f = open('past_users.txt', 'a')


class user:
    def __init__(self, id, favorite_Genre):
        f.write('\n')
        f.write(id)
        f.write(', ')
        f.write(favorite_Genre)