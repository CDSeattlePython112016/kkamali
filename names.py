def print_students(students):
    for student in students:
        print student["first_name"], student["last_name"]

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

print_students(students)

def print_students_dict(users):
    count = 1
    for key in users.keys():
        for element in users[key]:
            name_length = len(element["first_name"]) + len(element["last_name"])
            print str(count) + " - " + element["first_name"].upper() + " " +  element["last_name"].upper() + " - " + str(name_length)
            count += 1

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print_students_dict(users)
