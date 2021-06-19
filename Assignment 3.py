#Edison Kolaj
#Assignemnt #3

len("hello")
name = "joe"
len(name)
name_list = ["bob","jimmy","max b","bernie","jordan","future hendrix"]

count = 0
for i in name_list:
    if len(i) > count:
        count = len(i)
        longestword = i
print(longestword)