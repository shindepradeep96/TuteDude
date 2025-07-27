std_marks = {
    'Pradeep':85,
    'Alice':90,
    'Bob':80,
    'Charlie':70,
    'Daniel':60,
}
std_name=input("Enter the Student's name: ")
if std_name in std_marks:
    print(std_name + "'s marks:", std_marks[std_name])
else:
    print("Student not found.")
