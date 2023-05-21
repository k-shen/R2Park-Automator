from Driver import driver
from Request import Request
import time

def getNumDays():
    numDaysStr = input("Please enter the number of days you would like to register this vehicle for: ")
    
    while True:
        try: 
            numDaysInt = int(numDaysStr)
            return numDaysInt
        except: 
            print("please enter a whole number")
            numDaysStr = input("Please enter the number of days you would like to register this vehicle for: ")

def getRequest():
    print("Please fill out the vehicle registration form: ")
    propertyName = input("Property name: ")
    password = input("Access code: ")
    apt = input("Apartment: ")
    vehicleMake = input("Vehicle make: ")
    vehicleModel = input("Vehicle model: ")
    vehicleLicense = input("Vehicle license: ")
    confirmationEmail = input("Confirmation email: ")
    
    return Request(property=propertyName, password=password, apt=apt, vehicleMake=vehicleMake, vehicleModel=vehicleModel, vehicleLicense=vehicleLicense, email=confirmationEmail)

if __name__ == '__main__':
    defaultRequest = Request(
        property='copeland',
        password='Summer2511',
        apt='354',
        vehicleMake='Subaru',
        vehicleModel='Impreza',
        vehicleLicense='IXG260',
        email='kaiwenshen27@gmail.com'
    )
    
    #driver(defaultRequest)
    # request = getRequest()
    numDays = getNumDays()
    
    interval = 60
    for _ in range(numDays):
        #driver(request=request)
        print("test")
        time.sleep(interval)
    
    print("Completed... terminating program")
    