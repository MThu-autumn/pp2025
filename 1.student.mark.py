students = []
courses = []
marks = {}

def input_number_of_students():
    n = int(input("Enter number of students: "))
    return n
def input_students_info(n):
    for _ in range(n):
        sid=input(" Enter students ID: ")
        name=input("Enter students name: ")
        dob=input("Enter students DOB (mm/dd/yy): ")
        students.append({"sid": sid, "name": name, "dob": dob})

def input_number_of_courses():
    n= int(input("Enter number of courses: "))
    return n
def input_courses_info(n):
    for _ in range(n):
        cid= input("Enter courses ID: ")
        name= input("Enter courses name: ")
        courses.append({"cid": cid, "name": name})

def input_marks_for_courses():
    global marks
    global courses
    course_id=input("Enter courses ID to input marks: ")

    if course_id not in [c['cid'] for c in courses]:
        print("Courses not found!!!")
        return
    if course_id not in marks:
        marks[course_id] = []

    for s in students:
        mark = float(input(f"Enter mark for {s['name']} ( ID: {s['sid']}): "))
        marks[course_id].append((s['sid'], mark))

def list_courses():
    print("\nCourses:")
    for c in courses:
        print(f"ID: {c['cid']}, Name: {c['name']}")

def list_students():
    print("\nStudents: ")
    for s in students: 
        print(f"ID: {s['sid']}, Name: {s['name']}, DoB: {s['dob']}")

def show_students_marks():
    course_id=input("Enter courses ID to show marks ")

    if course_id not in marks: 
        print(" NO marks recorded for this courses!!")
        return
    print(f"\nMarks for courses {course_id}: ")

    for sid, mark in marks[course_id]: 
        name = next(s['name'] for s in students if s['sid'] == sid)
        print(f"{name} (ID:{sid}): Mark:{mark}")

def main():
    while True:
        print("1. Input students")
        print("2. Input courses")
        print("3. input marks for a courses")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a courses")
        print("0. Exit")

        choice = input("choose an option ")
        if choice == '1':
            n = input_number_of_students()
            input_students_info(n)
        elif choice =='2':
            n = input_number_of_courses()
            input_courses_info(n)
        elif choice == '3':
            input_marks_for_courses()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_students_marks()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid option")
if __name__ == "__main__":
    main()