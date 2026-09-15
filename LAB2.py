log1 = "masha"
pass1 = "masha2009"
grades1 = [3, 12, 8, 10]
log2 = "ola"
pass2 = "ola2011"
grades2 = [2, 8, 1, 9]
log3 = "pasha"
pass3 = "pasha2008"
grades3 = [5, 4, 10, 1]
log4 = "vlad"
pass4 = "vlad1488"
grades4 = [4, 3, 2, 11]
a = True
while a == True:
    log = input("pishi login: ")
    password = input("pishi parol: ")
    grades = []
    if log == log1 and password == pass1:
        grades = grades1
        print("Grades:", grades)

        goodgrades = 0
        badgrades = 0

        for i in grades:
            if i >= 5 and i <= 12:
                goodgrades = goodgrades + 1
            elif i >= 1 and i <= 4:
                badgrades = badgrades + 1

        print("horosho (5-12):", goodgrades)
        print("pogano (1-4):", badgrades)
        a = False
    elif log == log2 and password == pass2:
        grades = grades2
        print("Grades:", grades)

        goodgrades = 0
        badgrades = 0

        for i in grades:
            if i >= 5 and i <= 12:
                goodgrades = goodgrades + 1
            elif i >= 1 and i <= 4:
                badgrades = badgrades + 1

        print("horosho (5-12):", goodgrades)
        print("pogano (1-4):", badgrades)
        a = False
    elif log == log3 and password == pass3:
        grades = grades3
        print("Grades:", grades)

        goodgrades = 0
        badgrades = 0

        for i in grades:
            if i >= 5 and i <= 12:
                goodgrades = goodgrades + 1
            elif i >= 1 and i <= 4:
                badgrades = badgrades + 1

        print("horosho (5-12):", goodgrades)
        print("pogano (1-4):", badgrades)
        a = False
    elif log == log4 and password == pass4:
        grades = grades4
        print("Grades:", grades)

        goodgrades = 0
        badgrades = 0

        for i in grades:
            if i >= 5 and i <= 12:
                goodgrades = goodgrades + 1
            elif i >= 1 and i <= 4:
                badgrades = badgrades + 1

        print("horosho (5-12):", goodgrades)
        print("pogano (1-4):", badgrades)
        a = False
    else:
        print("Ne to pishesh\n")
    continue

