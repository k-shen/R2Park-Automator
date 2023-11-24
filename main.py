from Driver import driver
from Request import Request
from Driver import NoneException
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
    propertyName = input("Property name (if multiple properties are returned, will default to first property in the result): ")
    password = input("Access code: ")
    apt = input("Apartment: ")
    vehicleMake = input("Vehicle make: ")
    vehicleModel = input("Vehicle model: ")
    vehicleLicense = input("Vehicle license: ")
    confirmationEmail = input("Confirmation email address: ")
    
    return Request(property=propertyName, password=password, apt=apt, vehicleMake=vehicleMake, vehicleModel=vehicleModel, vehicleLicense=vehicleLicense, email=confirmationEmail)

if __name__ == '__main__':
    #default, used for testing
    request = Request(
        property='copeland',
        password='Summer2511',
        apt='354',
        vehicleMake='Subaru',
        vehicleModel='Impreza',
        vehicleLicense='IXG260',
        email='kaiwenshen27@gmail.com'
    ) 
    numDays = 2
    interval = 20
    
    # comment this section out for debug
    request = getRequest()
    numDays = getNumDays()
    interval = 23 * 60 * 60
    
    day = 0
    while day < numDays:
        try: 
            
            driver(request=request)
            if numDays == 1:
                break
            print("Registration complete, will re-register in 23 hours. ")
            time.sleep(interval)
            day += 1
        except NoneException:
            password = input("Please re enter the access password: ")
            request.password = password
            
        except: 
            print("Something went wrong, see the above error")
            print("Please fix the error then run the program again")
            print("Exiting...")
            exit()
    
    print("Completed... terminating program")
    