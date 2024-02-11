while True:
    score = int(input("Insert your Score: "))
    if score == 50:
        print("Grade = 4")
    elif 50 <= score < 60:
        print("Grade = 5")
    elif 60 <= score < 70:
        print("Grade = 6")
    elif 70 <= score < 80:
        print("Grade = 7")
    elif 80 <= score < 90:
        print("Grade = 8")
    elif 90 <= score < 95:
        print("Grade = 9")
    elif 95 <= score <= 100:
        print("Grade = 10")
    else:
        print("Error")
