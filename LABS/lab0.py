def kmToMiles(distKm):
    distMiles = distKm / 1.609
    return distMiles



distMarathonKm = float(input('Enter distance in Km: '))
distMarathonMiles = kmToMiles(distMarathonKm)
print("distance of marathon in miles is: " + str(distMarathonMiles))
print("Hello bitch")
