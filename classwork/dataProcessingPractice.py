#Sets the name and email for a single student.
def set_student_info(grades, pid, name, email):
	if pid not in grades:
		grades[pid] = {}
		grades[pid]["grades"] = {}
	
	grades[pid]["name"] = name
	grades[pid]["email"] = email


#Sets the grade of a student for a single PA.
def set_grade(grades, pid, pa, value):
	if pid not in grades:
		return "Student not in dictionary."

	grades[pid]["grades"][pa] = value
	return grades[pid][pa]



#Gets the grade of a student for a single PA.
def get_grade(grades, pid, pa):
	if pid not in grades:
		return "Student not in dictionary."

	result =[]
	for pa in grades[pid]["grades"].valies():
		result.append(pa)

	return result


#Gets all of the grades of a student and returns them in a list.
def get_grades_for_student(grades, pid):
    if pid not in grades:
        return "Student not dictionary"

    
    if pa not in grades[pid]['grades']:
        return "PA not in dictionary for this student"

    
    return grades[pid]["grades"][pa]

grades = {"A001": 
			{"name":"James", 
				"email":"james@fake.ucsd.edu", 
				"grades":
					{"pa1":100, 
						"pa2":95, 
						"pa3":90}
			}
		}

print(get_grade(grades, "A001", "pa3") )
set_grade(grades, "A001", "pa3", 95)
print( get_grade(grades, "A001", "pa3") )
print( get_grades_for_student(grades, "A001") )
print()
set_student_info(grades, "A001", "James", "test@ucsd.edu")
print(grades)