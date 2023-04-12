data = [[20,60,70],[30,80,90],[10,50,40]]


def lookUpSection(studentID, info):
	section = ["A00", "A01", "A02"]
	sectionIndex = 0

	for row in info:
		for item in row:
			if studentID == item:
				return section[sectionIndex]
		sectionIndex += 1

	
	return "student ID " + str(studentID) + " is not found."

print(lookUpSection(40, data))
print(lookUpSection(30, data))
print(lookUpSection(60, data))
print(lookUpSection(100, data))