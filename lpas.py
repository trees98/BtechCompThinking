# -------------------------
# learning platform access system
# -------------------------

courses = {} #empty dict to store courses added by admin
quizzes = {} # empty dict storing questions for quizzes in memory (will not persist if you close program)
notifications = [] # messages list 

#nested dictionary containing user dictionaries with their data
users = {
    "user1": {
        "Username": "john_d",
        "FirstName": "John",
        "LastName": "Deere",
        "Password": "12345",
        "Role": "Student",
        "Grades": {"Math": 85, "Science": 92}
    },
    "user2": {
        "Username": "bill_j",
        "FirstName": "Bill",
        "LastName": "John",
        "Password": "12345",
        "Role": "Student",
        "Grades": {"Math": 78}
    },
    "user3": {
        "Username": "bob_p",
        "FirstName": "Bob",
        "LastName": "Paul",
        "Password": "12345",
        "Role": "Student",
        "Grades": {}
    },
    "user4": {
        "Username": "matt_g",
        "FirstName": "Matt",
        "LastName": "Garstka",
        "Password": "12345",
        "Role": "Student",
        "Grades": {}
    },
    "user5": {
        "Username": "jay_p",
        "FirstName": "Jay",
        "LastName": "Postones",
        "Password": "12345",
        "Role": "Student",
        "Grades": {}
    },
    "user6": {
        "Username": "willie_n",
        "FirstName": "Willie",
        "LastName": "Nelson",
        "Password": "12345",
        "Role": "Student",
        "Grades": {}
    },
    "prof1": {
        "Username": "jim_b",
        "FirstName": "Jim",
        "LastName": "Bob",
        "Password": "54321",
        "Role": "Teacher"
    },
    "prof2": {
        "Username": "ron_b",
        "FirstName": "Ron",
        "LastName": "Bill",
        "Password": "54321",
        "Role": "Teacher"
    },
    "prof3": {
        "Username": "mike_p",
        "FirstName": "Mike",
        "LastName": "Portnoy",
        "Password": "54321",
        "Role": "Teacher"
    },
    "admin1": {
        "Username": "Admin",
        "FirstName": "Admin",
        "LastName": "Admin",
        "Password": "00000",
        "Role": "Admin"
    }
}

#------------------------
# course functions
#------------------------

#create course function
def create_course():
    course_id = input("Enter new course ID: ").strip() #prompt admin to enter course ID, removing accedental spaces leading or following
    if course_id in courses: #check if entered course ID key is in the courses dictionary
        print("Course already exists.") #if it is let the user know
        return #exit function early back to user menu to avoid overwriting existing course 
    course_name = input("Enter course name: ").strip() #if course ID is new, prompt for course name

    #add new course to courses dictionary
    courses[course_id] = { #store it as a nested dictionary 
        "Name": course_name,
        "Professors": [], #empty list for professors names
        #"Students": [] -- maybe later?
    }
    print(f"Course {course_id} - {course_name} created.") #print message to admin

#cancel course function 
def cancel_course():
    course_id = input("Enter course ID to cancel: ").strip() #prompt user to enter course ID, strip space at beginning and end of string
    if course_id in courses: #if the entered course is found
        del courses[course_id] # delete it 
        print(f"Course {course_id} has been canceled.") #confirm to user
    else:
        print("Course not found.") #or else let them know it wasn't found

#assign professor to course function 
def assign_professors():
    course_id = input("Enter course ID: ").strip() #prompt user for course ID, stripping white space
    
    if course_id not in courses: #check if the course ID exists in courses dictionary
        print("Course not found.") #if not let the user know and exit the function
        return  

    professor_id = input("Enter professor's user ID to assign: ").strip() #promt the use to enter in user ID, stripping white space
    professor = users.get(professor_id)  #try and get the profs user dict(value) from the users dictionary using their ID(key), store in variable
    if professor and professor.get("Role") == "Teacher": #check if the user is found and the value of the Role key is Teacher in their user dict
        full_name = f"{professor['FirstName']} {professor['LastName']}" #set full name of professor for display so it doesnt just display user ID when assigning to course

        if full_name in courses[course_id]["Professors"]: #access nested course dict within courses dict with the given course ID, access list of profs assigned to course, check if theyre already in list
            print(f"Professor {full_name} is already assigned to this course.") #if prof is already in professors list, let user know theyre already assigned
        else:
            courses[course_id]["Professors"].append(full_name) #or else append the full name of prof to the professor list, within the nested course dict
            print(f"Professor {full_name} assigned to course {course_id}.") #let user know the prof has been assigned to course
    else:
        print("Professor not found or user is not a teacher.") #or else let the user know prof not found or has wrong role to be assigned to course

#------------------------
# grade funtions
#------------------------

#function for updating student grade 
def update_grade():
    user_id = input("Enter student ID number: ") #prompt user for student ID number (user1, user2, etc)
    subject = input("Enter subject to update: ") #prompt user for subject (Science, Math)

    student = users.get(user_id) #search for user dict using provided user ID from the users dict
    if student and student["Role"] == "Student": #check if a user exists with that ID and theyre role is student
        full_name = f"{student['FirstName']} {student['LastName']}" #combine users first and last name for display
        print(f"\nStudent Name: {full_name}") #print out students full name
        print(f"Student ID: {user_id}") #print out student ID
        print(f"Subject: {subject}") #print out subject chosen to update
        print("--------------")
        grades = student.get("Grades", {}) #get users grades dict within their user dict, if none exist use an empty dict
        if subject not in grades: #if the subject is not in that users grades
            print(f"{subject} does not exist for this student. Use 'Add Grade' instead.") #let the user know to use add grade funtion instead
            return  #exit the function early if subject doesn't exist

        new_grade = input("Enter new grade: ") #prompt for new grade
        grades[subject] = int(new_grade) #assign new grade value to that subject key within the users grades dict
        print(f"{subject} grade updated to {new_grade}.") #inform user 
    else:
        print("Invalid student username.") # or else print invalid username

#delete grade function
def delete_grade():
    user_id = input("Enter student ID number: ") #promt user for ID number
    subject = input("Enter subject to delete: ") #prompt user for subject

    student = users.get(user_id) #look up the user dict from the users dict using entered user ID, asign to student var
    if student and student["Role"] == "Student": #if they exist and their role is student
        full_name = f"{student['FirstName']} {student['LastName']}" #combine first and last name for display
        print(f"\nStudent Name: {full_name}") #display students full name
        print(f"Student ID: {user_id}") #display student id
        print(f"Subject: {subject}") #display chosen subject
        print("--------------") #very cool lines
        
        grades = student.get("Grades", {}) #from the user dict find the grades dict within, if none exist create empty dict, assign to grades var
        if subject not in grades: #if the entered subject(key) is not within grades dict
            print(f"{subject} not found.") #let user know not found
            return #exit function early
        confirm = input(f"Are you sure you want to delete {full_name}'s {subject} grade? (Y/N): ") #if found confirm deletion of grade/subject with user
        if confirm.strip().lower() == 'y': #strip blank space and convert to lower case, if y
            del grades[subject] #delete entered subject from the grades dict
            print(f"{subject} grade deleted.") #let user know of great success
        else:
            print("Deletion cancelled.") #or else print deletion canceled 
    else:
        print("Invalid student ID.") # or else print invalid student ID

#add grade funtion 
def add_grade():
    user_id = input("Enter student ID number: ") #promt for ID number
    subject = input("Enter subject: ") #promt for subject
    grade = input("Enter grade: ") #prompt for grade

    student = users.get(user_id) #get that users dict from the users dict by their ID, assign to student var
    if student and student["Role"] == "Student": #if the user exists and they are a student
        if "Grades" not in student: #if grades dict does not exist in student dict
            student["Grades"] = {} # create the grades dict, assign empty dict to grades key in students dict
        if subject in student["Grades"]: #if subject exists in students grades dict within their user dict
            print(f"{subject} already exists. Use update instead.") #let the user know
        else:
            student["Grades"][subject] = int(grade) #or else, assign the entered grade as an int to the entered subject in the students grades dict
            print(f"{subject} grade added.") #let user know of great success
    else:
        print("Invalid student ID number.") #or else print invalid user ID

#view student grades function
def view_student_grades():
    user_id = input("Enter student ID number: ") #prompt for user ID

    student = users.get(user_id) #get students dict from users dict assign to student var
    if student and student["Role"] == "Student": #if they exist and their role is student
        full_name = f"{student['FirstName']} {student['LastName']}" #combine first and last name for display
        print(f"\nStudent Name: {full_name}") #display student info
        print(f"Student ID: {user_id}")

        grades = student.get("Grades", {}) #get students grades dictionary or empty one if it doesnt exist
        if grades: #if student has any grades recorded 
            print("\nStudent Grades:") #print string
            for subject, grade in grades.items(): #for each key, value pair in students grades dict
                print(f"{subject}: {grade}") #print them to the screen for the user 
        else:
            print("No grades available.") #or else print no grades
    else:
        print("Invalid student username.") #or else print invalid username

# view own grades function(for students)
def view_own_grades(user):
    grades = user.get("Grades", {}) #get grades dict from students dict, use ampty dict as fallback
    if grades: #if there is data in grades dict
        print("\nYour Grades:") #print string
        for subject, grade in grades.items(): #for key(subject), value(grade) in students grades dict
            print(f"{subject}: {grade}") #print them for the user
    else:
        print("No grades available.") #or else let them know no grades available

#------------------------
# add/take quiz functions
#------------------------

#add quiz function
def add_quiz():
    subject = input("Enter quiz subject: ") #prompt user for quiz subject
    num_questions = int(input("How many questions? ")) #prompt user for number of questions

    if subject not in quizzes: #if the entered subject is not in quizzes dict
        quizzes[subject] = [] #assign an empty list to the entered subject(key) in the quizzes dict

    for _ in range(num_questions): #loop runs entered num_questions times, dont need to use index number of each question so using _ as loop var
        q = input("Enter question: ") #prompt for quiz question
        a = input("Enter answer: ") #prompt for quiz answer
        quizzes[subject].append({"question": q, "answer": a}) #store question(key) answer(value) pairs as dictionary, append it to list of given subject
        #each subject(key) in quizzes dict contains a list(value) of question and answer dicts
    print(f"{num_questions} questions added to {subject}.")  #let user know their questions were added 

#take quiz function
def take_quiz():
    subject = input("Enter quiz subject: ") #prompt user for subject
    quiz = quizzes.get(subject) #search quizzes dict for the list of question dicts for the entered subject

    if not quiz: #if no quizzes exist for the entered subject
        print("No quiz found for that subject.") #let user know
        return #exit function

    score = 0 #create score variable and assign 0
    for q in quiz: #loop through each question in quiz(list of question dicts)
        answer = input(q["question"] + " ") #prompt user with question and wait for answer adding white space after question
        if answer.strip().lower() == q["answer"].strip().lower(): #if the answer = the value of the answer key in that questions dict
            score += 1 #add 1 to score if answers correct

    print(f"You scored {score}/{len(quiz)}!") #print the score (will be value of score var after answering all questions, out of the length of the question list)

#------------------------
# notification funtions
#------------------------

#view notification function
def view_notifications():
    if not notifications:
        print("No notifications.") #if notifications list is empty, let the user know
    else:
        print("\n--- Notifications ---") #print header
        for note in notifications: #loop though each notification in nontifications list
            poster = users[note["posted_by"]]["FirstName"] #searches user ID of person who posted note dict in notifications list in the users dictionary and finds their first name
            print(f"From {poster}: {note['message']}") #print the posters name and the message keys value from that notes dict

#post notification function
def post_notification(user_id): #pass current user ID to function so we know who posted a notification without prompting
    message = input("Enter notification message: ") #prompt user for notification message
    notifications.append({"message": message, "posted_by": user_id}) #append a note dict to the notifications list containing the entered message and logged in users ID
    print("Notification posted.") 

#------------------------
# login funtion
#------------------------
def login():
    print("\n=== Login ===") #print header 
    entered_username = input("Username: ") #prompt user for username
    entered_password = input("Password: ") #prompt user for password

    #go through all users in users dictionary
    for user_id, user in users.items(): # for each key, value in the users dictionary
        if user["Username"] == entered_username and user["Password"] == entered_password: #if the entered username and password match whats in that users dictionary
            print(f"\nWelcome, {user['FirstName']} {user['LastName']}") #welcome the user pulling their first and last name from their dictionary
            return user_id, user #returns results of this function back to main 

    print("Invalid login. Try again.") #print message if loop finishes without finding a matching user
    return None, None #return none, none, for key, value back to main to let user know login failed

#---------------------------------
#---------MENUS-------------------
#---------------------------------

#funtion for student menu
def student_menu(user):
    while True: #keep showing student menu until user chooses to logout
        print("\n-- Student Menu --") #display student menu
        print("1. View Grades")
        print("2. Take Quiz")
        print("3. View Notifications")
        print("4. Logout")

        choice = input("Enter your choice: ") #prompt for menu selection

        if choice == "1":       #depending on choice call a certain function or logout to return to main
            view_own_grades(user)
        elif choice == "2":
            take_quiz()
        elif choice == "3":
            view_notifications()
        elif choice == "4":
            break
        else:
            print("Invalid choice.") #if option invalid let user know

#function for teacher menu
def teacher_menu(user_id):
    while True: #keep showing teacher menu until user chooses to logout
        print("\n-- Teacher Menu --") #display teacher menu
        print("1. View Student Grades")
        print("2. Update Student Grade")
        print("3. Delete Student Grade")
        print("4. Add Grade to Student")
        print("5. Add Quiz")
        print("6. Post Notification")
        print("7. Logout")

        choice = input("Enter your choice: ") #prompt for menu selection

        if choice == "1":       #depending on choice call a certain function or logout to return to main
            view_student_grades()
        elif choice == "2":
            update_grade()
        elif choice == "3":
            delete_grade()
        elif choice == "4":
            add_grade()
        elif choice == "5":
            add_quiz()
        elif choice == "6":
            post_notification(user_id)
        elif choice == "7":
            break
        else:
            print("Invalid choice.") #if option invalid let user know

#function for admin menu
def admin_menu(user_id):
    while True: #keep showing admin menu until user chooses to logout
        print("\n-- Admin Menu --") #display admin menu
        print("1. View Student Grades")
        print("2. Update Student Grades")
        print("3. Delete Student Grades")
        print("4. Add Grade to Student")
        print("5. Add Quiz")
        print("6. Post Notification")
        print("7. Create Course")
        print("8. Cancel Course")
        print("9. Assign Professors")
        print("10. Logout")

        choice = input("Enter your choice: ") #prompt for menu selection

        if choice == "1":       #depending on choice call a certain function or logout to return to main
            view_student_grades()
        elif choice == "2":
            update_grade()
        elif choice == "3":
            delete_grade()
        elif choice == "4":
            add_grade()
        elif choice == "5":
            add_quiz()
        elif choice == "6":
            post_notification(user_id)
        elif choice == ("7"):
            create_course()
        elif choice == ("8"):
            cancel_course()
        elif choice == ("9"):
            assign_professors()
        elif choice == "10":
            break
        else:
            print("Invalid choice.") #if option invalid let user know


#main program
def main():
    while True: #main loop keeps program running until user logs out
        print("\n=== School Management System ===") #display main menu
        print("1. Login")
        print("2. Quit")
        choice = input("Enter your choice: ") #prompt for choice

        if choice == "1":
            user_id, user = login() #call login function, expect two return values and store them for use below

            if user:
                role = user["Role"] #if login successsful(great success), get the users role
                if role == "Student": #depending on the users role, call the appropriate menu function
                    student_menu(user)
                elif role == "Teacher":
                    teacher_menu(user_id)
                elif role == "Admin":
                    admin_menu(user_id)
            else:
                print("Login failed.") #if login unsuccessful let user know
        
        elif choice == "2":
            print("Goodbye!") #if chosen break out of main loop ending program
            break
        else:
            print("Invalid choice. Enter 1 or 2.")

main() #launch main program