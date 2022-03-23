score = int(input("Insert your Score: "))

if score == 50:
    print("Grade = 4")
elif score >= 50 and score < 60:
    print("Grade = 5")
elif score >= 60 and score < 70:
    print("Grade = 6")
elif score >= 70 and score < 80:
    print("Grade = 7")
elif score >= 80 and score < 90:
    print("Grade = 8")
elif score >= 90 and score < 95:
    print("grade = 9")
elif score >= 95 and score < 101:
    print("Grade = 10")
else:
    print("Error")
