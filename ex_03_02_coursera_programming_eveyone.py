score = input("Enter Score: ")
score = float(score)
if score >= 0.9 and score <1.0:
    print("A")
elif score >= 0.8 and score <0.9:
    print("B")
elif score >= 0.7and score <0.8:
    print("C")
elif score >= 0.6 and score <0.7:
    print("D")
elif score < 0.6 and score >=0.0:
    print("F")
else:
    print("unfortunatly the Input should be between 0.0 to 1.0")
