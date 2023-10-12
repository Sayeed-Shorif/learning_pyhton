# take students grade and attendance and if student attendance 50% and average grade is 50
# then pass that student to form fill up.
def StudentGradeAverage():
    grades = []
    for subject in range(6):
        while True:
            grade = input(f"Enter the {subject + 1} grade : ")
            try:
                grade = int(grade)
                if 0 < grade < 100:
                    grades.append(grade)
                    break
                else:
                    print("Make sure the input grade is greater than 0 and less than 100.")

            except:
                print("Enter a valid input.")
    total = 0
    for i in grades:
        total += i
    average = total / len(grades)
    return average


def studentAttendance():
    while True:
        classes = input("Enter the number of classes : ")
        try:
            classes = int(classes)
            if 0 < classes < 100:
                break
            else:
                print("Enter a valid class number between 1 to 100.")

        except:
            print("Enter a valid number!")
    while True:
        attend = input("Enter the number of attendance : ")
        try:
            attend = int(attend)
            if 0 < attend < 100:
                break
            else:
                print("Enter a valid attendance number between 1 to 100.")

        except:
            print("Enter a valid number!")
    attendance = (attend / classes) * 100
    return attendance

if StudentGradeAverage() > 50 and studentAttendance() > 50:
    print("Congratulation, You meet the condition to attend the exam.")
else:
    print("Alas, You didn't meet the condition to attend the exam.")




