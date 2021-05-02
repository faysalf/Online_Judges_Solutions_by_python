n = int(input())
for i in range(n):
    grade = int(input())
    if grade<40 and 40-grade < 3:
        print(40)
    elif grade<45 and 45-grade < 3:
        print(45)
    elif grade<50 and 50-grade < 3:
        print(50)
    elif grade<55 and 55-grade < 3:
        print(55)
    elif grade<60 and 60-grade < 3:
        print(60)
    elif grade<65 and 65-grade < 3:
        print(65)
    elif grade<70 and 70-grade < 3:
        print(70)
    elif grade<75 and 75-grade < 3:
        print(75)
    elif grade<80 and 80-grade < 3:
        print(80)
    elif grade<85 and 85-grade < 3:
        print(85)
    elif grade<90 and 90-grade < 3:
        print(90)
    elif grade<95 and 95-grade < 3:
        print(95)
    elif grade<100 and 100-grade < 3:
        print(100)
    else:
        print(grade)
