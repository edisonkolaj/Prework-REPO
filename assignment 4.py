#Edison Kolaj
#Assignment 4

name_list = ["bob","jimmy","max b","bernie","jordan","future hendrix"]
def namelist():
    count = 0
    for i in name_list:
        if len(i) > count:
            count = len(i)
            longestword = i
    return (longestword)
big_name = namelist()
print(big_name)