import pandas as pd
import numpy as np
import os
import _sqlite3
import lxml as lx
import random as newRandom

sq = _sqlite3.connect("E:/sqlite/database.sqlite")


s = sq.cursor()
s.execute("SELECT * FROM genres")
# Adds Tuples to variable s from SQlite Database

p = sq.cursor()
p.execute("SELECT * FROM reviews")
# Adds Tuples to variable p from SQlite Database

firstSearch = input("Enter favorite genre: ")
# Takes input from user to a genre

newlist = s.fetchall()
# Adds Tuples to newList

newlist1 = p.fetchall()
# Adds Tuples to newList1

condensedSearchLists = []
# New list that will contain Tuples that contain user selected genre.
condensedSearchLists1 = []
# New list that will contain Tuples that contain highest rated albums.
newnum = 0
for item in newlist:
    if item[1] == firstSearch:
        condensedSearchLists += item
        newnum += 1
# Iterates over list to find number of tuples that match user selected genre and makes a new list with the selected genre.

newnum1 = 0
best_Album = ''
for item in newlist1:
    if (item[4] > newnum1):
        newnum1 = item[4]
        best_Album = item[1]

print(newnum1)
print(best_Album)







