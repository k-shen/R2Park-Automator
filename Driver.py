from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Request import Request
import time

URL = "https://www.register2park.com/register"

def driver(request: Request) :
    print("Starting app...")
    
    try: 
        DRIVER = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())
    except Exception as e: 
        print(e)
        print("Something went wrong at setting up chrome driver, please check if the chrome driver has been successfully downloaded")
        print("Maybe re run `bash install.sh`")
        raise GeneralException()
    print("Successfully set up chrome")
    
    try:
        DRIVER.get(URL)
    except Exception as e: 
        print(e)
        print("Something went wrong when trying to access the website.")
        print("Maybe the URL is broken?")
        raise GeneralException() 
    
    #page 1
    try: 
        clickAndType(DRIVER, xpath="//form//input[@id='propertyName']", message=request.property)
        clickAndType(DRIVER, xpath="//form//button[@id='confirmProperty']")
    except Exception as e: 
        print(e)
        print("Something went wrong on the property name page...")
        raise GeneralException()
    print("Successfully typed in the property name: " + request.property)
    
    #page2
    try:
        clickAndType(DRIVER, xpath="//form//input[@name='property']")
        clickAndType(DRIVER, xpath="//form//button[@id='confirmPropertySelection']")
    except Exception as e: 
        print(e)
        print("Something went wrong on the property selection page...")
        raise GeneralException() 
    print("Successfully selected the first property")
    
    #page3
    try: 
        clickAndType(DRIVER, xpath="//button[@id='registrationTypeVisitor']")
    except Exception as e: 
        print(e)
        print("Something went wrong on the registration type page...")
        raise GeneralException() 
    print("Successfully selected the registration type (visitor parking)")
    
    #page4 
    try: 
        clickAndType(DRIVER, xpath="//form//input[@id='accessCode']", message=request.password)
        clickAndType(DRIVER, xpath="//form//button[@id='propertyPassword']")
        time.sleep(2)
    except Exception as e: 
        print(e)
        print("Something went wrong on the type in password page...")
        raise GeneralException() 
    print("Successfully typed in password " + request.password)
    
    if (DRIVER.find_element(By.ID, "error-modal").is_displayed()):
        print("Wrong access password please re enter the password")
        raise NoneException() 

    #page5
    try: 
        clickAndType(DRIVER, xpath="//form//input[@id='vehicleApt']", message=request.apt)
        clickAndType(DRIVER, xpath="//form//input[@id='vehicleMake']", message=request.vehicleMake)
        clickAndType(DRIVER, xpath="//form//input[@id='vehicleModel']", message=request.vehicleModel)
        clickAndType(DRIVER, xpath="//form//input[@id='vehicleLicensePlate']", message=request.vehicleLicense)
        clickAndType(DRIVER, xpath="//form//input[@id='vehicleLicensePlateConfirm']", message=request.vehicleLicense)
        clickAndType(DRIVER, xpath="//form//button[@id='vehicleInformation']")
    except Exception as e: 
        print(e)
        print("Something went wrong on the vehicle information page...")
        raise GeneralException() 
    print("Successfully registered the vehicle: " + request.vehicleMake + " " + request.vehicleModel + " " + request.vehicleLicense 
          + " for apartment " + request.apt)
    
    #page6
    try: 
        clickAndType(DRIVER, xpath="//button[@id='email-confirmation']")
        clickAndType(DRIVER, xpath="//form//input[@id='emailConfirmationEmailView']", message=request.email)
        clickAndType(DRIVER, xpath="//button[@id='email-confirmation-send-view']")
    except Exception as e: 
        print(e)
        print("Something went wrong on the email confirmation page...")
        raise GeneralException()
    print("Successfully sent the confirmation to email: " + request.email)
    
    DRIVER.close()

def clickAndType(driver, xpath: str, message=""):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()
    if message:
        element.send_keys(message)
    
class GeneralException(Exception):
    pass

class NoneException(Exception):
    pass