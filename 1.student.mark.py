students = []
courses = []

def input_student():
    sid = input("Enter id: ")
    sname = input("Enter name: ")
    dob = input("Enter date of birth: ")

    student = {
            'id': sid,
            'name': sname,
            'dob': dob
            }
    
    students.append(student)

def input_course():
    cid = input("Enter course id: ")
    cname = input("Enter course name: ")

    course = {
        'id': cid,
        'name': cname,
    }

    courses.append(course)

def list_courses():
    print("List of courses")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")
    
def list_students():
    print("List of students")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def main():
    while True:
        print('\n Student Grade Management System')
        print("1.Add Student")
        print("2.Input courses")
        print("3.View Students")
        print("4.View Courses")
        print("5.Exit")
        
        choice = int(input("Enter your choice = "))
        if choice == 1:
            input_student()
        elif choice ==2:
            input_course()
        elif choice == 3:
            list_students()
        elif choice == 4:
            list_courses()
        elif choice == 5:
            print("Exiting program ...")
            break
        else:
            print("Invalid choice!")


main()
