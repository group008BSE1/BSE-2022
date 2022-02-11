def computegrade(score):
    try:
        if score >= 0.9 and score < 1:
            grade = 'A'
        elif score >= 0.8 and score < 1:
            grade = 'B'
        elif score >= 0.7 and score < 1:
            grade = 'C'
        elif score >= 0.6 and score < 1:
            grade = 'D'
        elif score < 0.6 and score > 0:
            grade = 'F'
        print('Grade:', grade)
    except:
        print("Bad score")

computegrade(0.75)