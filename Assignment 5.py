#Edison Kolaj
#Assignment 5

name_list = ["bob","jimmy","max b","bernie","jordan","future hendrix"]
evens = []
odds = []
def index():
    for i in name_list:
        if len(i)%2 == 0 :
            evens.append(i)
        else:
            odds.append(i)
index()
print(evens)
print(odds)

