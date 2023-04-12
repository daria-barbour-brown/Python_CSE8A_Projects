

# Make sure you don't use the version of CSE8ACSV from PA 8!
from CSE8ACSV import *

# The data is imported for you. Keep in mind, the BLM dataset 
# and graduate datasets are lists of dictionaries,
# and the diversity data is a dictionary of dictionaries.

blm_protest_data = get_blm_data("blm_state.csv")
tech_diversity_data = get_diversity_data("tech_diversity.csv")
graduate_data = get_graduates_data("graduates.csv")

#PART 1

# Task 1: Given a list of states, return the average protest attendance
#         in each state as a list of tuples shown below


def get_avg_attendance(states):
    result = []
    for stateData in blm_protest_data: #we have a current state's dictionary
    	state = stateData["State"] #which state am I?
    	if state in states:
    		if stateData["TotalProtests"] == 0:
    			result.append((stateData["State"], 0))
    		else:
    			avg = (stateData["TotalAttendance"]) / (stateData["TotalProtests"])
    			result.append((stateData["State"], avg))

    return result 

# Sample run
#print(get_avg_attendance(["Wisconsin", "California", "Nebraska"]))
# [('California', 297.5432098765432), ('Nebraska', 0), ('Wisconsin', 121.78947368421052)]

#PART 2

# Task 2: Return the company with highest percentage of
# underrepresented minorities from the diversity dataset
def top_representation():
    top_company = ""
    topUM = 0
    for company in tech_diversity_data: #iterate through all keys 
    	companyData = tech_diversity_data[company] #retuns dict of current company key
    	
    	if companyData["underrepresented_minorities"] > topUM:
    		top_company = company
    		topUM = companyData["underrepresented_minorities"]

    return top_company


#print(top_representation())

#PART 3

# Task 3: Given an year and a list of majors, find the ratio of total males to
# females that graduated in that year across all the given majors. The function
# should return a list of tuples as shown below.

def male_to_female(year, majors):
    result = []
    filteredData = []
    for majorData in graduate_data:
    	if majorData["Year"] == year:
    		filteredData.append(majorData)
    for majorData in filteredData:
    	if majorData["Education.Major"] in majors:
    		ratio = majorData["Demographics.Gender.Males"] / majorData["Demographics.Gender.Females"]
    		result.append((majorData["Education.Major"], ratio))

    			

    return result 


# Sample runs:
#print(male_to_female(2010, ["Anthropology and Archeology", "Computer Science and Math",  "Botany"]))
# [('Anthropology and Archeology', 0.5103669568616079), ('Botany', 1.0550163465467919), ('Computer Science and Math', 2.089531826503529)]

print(male_to_female(2013, ["Linguistics",  "Civil Engineering"]))
# [('Civil Engineering', 4.874114500900507), ('Linguistics', 0.5518491270254267)]
