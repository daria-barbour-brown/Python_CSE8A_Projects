from CSE8ACSV import *

#list of dictionaries
blm_protest_data = get_blm_data("blm_state.csv")

#dictionary of dictionaries
tech_diversity_data = get_diversity_data("tech_diversity.csv")

#dictionary
state_populations = get_state_pops()


#PART 1.1 --------------------------------------
#MINIMUM NUMBER OF BLM PROTEST ATTENDEES 

#takes in list of states
#returns min number of attendees 
def minimum_blm_protest_attendence(states):
    min = float("inf")
    for stateData in blm_protest_data: #we have a current state's dictionary
        state = stateData["State"] #which state am I?
        if len(states) == 0:
            min = 0
        if state in states:
            if stateData["TotalAttendance"] == 0:
                min = 0
            elif stateData["TotalAttendance"] < min:
                min = stateData["TotalAttendance"]

    return min 

# print(minimum_blm_protest_attendence([]))


#PART 1.2 --------------------------------------
#POPULATION BELOW POVERTY LINE

#takes in float threashold
#returns list of states
def below_poverty_line(threshold):
    result = []
    for stateData in blm_protest_data: #iterate though each dictionary in the list of dicts
        state = stateData["State"] #dict at key "state" identifies the current state
        popBelowPov = stateData["PovertyRate"] * state_populations[state] #calculate the pop below pov
        if popBelowPov < threshold: 
            result.append(state)
    

    return result

# print(below_poverty_line(2000000))


#PART 1.3 ---------------------------------------
#DIVERISY IN TECH

#takes in ratio (upper threshold of ratio) and fields (list of two)
#returns dictionary of company name : ratio of people in two categories 
def diversity_in_tech(ratio, fields):
    result = {}
    for company in tech_diversity_data: #iterates through each key in dict of dicts
        companyData = tech_diversity_data[company] #access the current keys value (a dictionary)
        calculated_ratio = companyData[fields[0]] / companyData[fields[1]] #calc ratio 
        if calculated_ratio < ratio:
            result[company] = calculated_ratio #update a new key-val pair to dict
    return result

#print(diversity_in_tech(5, ["white_female", "black_female"]))


#PART 1.4 ---------------------------------------
#STAR POINTS

#returns dictionary state : black population in states with more than 20 protests
def blackPopWithHighProtests(threshold): 
    result = {}
    for stateData in blm_protest_data:
        state = stateData["State"]
        if stateData["TotalProtests"] > threshold:
            result[state] = stateData["BlackPop"]
    return result


#print(blackPopWithHighProtests(20))











