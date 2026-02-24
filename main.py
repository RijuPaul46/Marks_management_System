import csv
def display_students():
    with open("marks.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Roll No:", row["roll_no"])
            print("Name:", row["name"])
            print("Physics:", row["physics"])
            print("Chemistry:", row["chemistry"])
            print("Math:", row["math"])
            print("Total:", row["total"])
            print("----------------------")

display_students()
def update_mark(subject):
    students=[]
    with open("marks.csv","r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            students.append(row)
    roll=input("Enter roll number to update the mark")
    updated_mark=input("Enter the number which will be updated:")
    for student in students:
        if(student["roll_no"]==roll):
            student[subject]=updated_mark
            print("Marks Updated Successfully")
    with open("marks.csv","w",newline="") as file:
        fieldnm=["roll_no","name","physics","chemistry","math","total"]
        writer=csv.DictWriter(file,fieldnames=fieldnm)
        writer.writeheader()
        writer.writerows(students)
print("Login as Subject Teacher")
choice=input("Enter :\n 1 for Physics \n 2 for Chemistry \n 3 for Math ")
subject_map={
    "1":"physics",
    "2":"chemistry",
    "3":"math"
}
if choice in subject_map:
    subject=subject_map[choice]
    display_students()
    update_mark(subject)
else :
    print("Invalid Choice")
display_students()

