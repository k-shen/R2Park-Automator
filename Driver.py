from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Request import Request

URL = "https://www.register2park.com/register"

def driver(request: Request) :
    print("Accessing website...")
    chrome_options = Options()
    DRIVER_MANAGER = ChromeDriverManager().install()
    DRIVER = webdriver.Chrome(service=Service(DRIVER_MANAGER), options=chrome_options)
    
    DRIVER.get(URL)
    #page 1
    try: 
        clickAndType(DRIVER, xpath="//form//input[@id='propertyName']", message=request.property)
        clickAndType(DRIVER, xpath="//form//button[@id='confirmProperty']")
    except: 
        print("Something went wrong on the property name page...")
        return 
    print("Successfully typed in the property name: " + request.property)
    
    #page2
    try:
        clickAndType(DRIVER, xpath="//form//input[@name='property']")
        clickAndType(DRIVER, xpath="//form//button[@id='confirmPropertySelection']")
    except: 
        print("Something went wrong on the property selection page...")
        return 
    print("Successfully selected the first property")
    
    #page3
    try: 
        clickAndType(DRIVER, xpath="//button[@id='registrationTypeVisitor']")
    except: 
        print("Something went wrong on the registration type page...")
        return 
    print("Successfully selected the registration type (visitor parking)")
    
    #page4 
    try: 
        clickAndType(DRIVER, xpath="//form//input[@id='accessCode']", message=request.password)
        clickAndType(DRIVER, xpath="//form//button[@id='propertyPassword']")
        
    except: 
        print("Something went wrong on the access password page...")
        return 
    print("Successfully typed in the registration password: " + request.password)
    
    #page5
    try: 
        clickAndType(DRIVER, xpath="//form//input[@id='vehicleApt']", message=request.apt)
        clickAndType(DRIVER, xpath="//form//input[@id='vehicleMake']", message=request.vehicleMake)
        clickAndType(DRIVER, xpath="//form//input[@id='vehicleModel']", message=request.vehicleModel)
        clickAndType(DRIVER, xpath="//form//input[@id='vehicleLicensePlate']", message=request.vehicleLicense)
        clickAndType(DRIVER, xpath="//form//input[@id='vehicleLicensePlateConfirm']", message=request.vehicleLicense)
        clickAndType(DRIVER, xpath="//form//button[@id='vehicleInformation']")
    except: 
        print("Something went wrong on the vehicle information page...")
        return 
    print("Successfully registered the vehicle: " + request.vehicleMake + " " + request.vehicleModel + " " + request.vehicleLicense 
          + " for apartment " + request.apt)
    
    #page6
    try: 
        clickAndType(DRIVER, xpath="//button[@id='email-confirmation']")
        clickAndType(DRIVER, xpath="//form//input[@id='emailConfirmationEmailView']", message=request.email)
        clickAndType(DRIVER, xpath="//button[@id='email-confirmation-send-view']")
    except: 
        print("Something went wrong on the email confirmation page...")
        return
    print("Successfully sent the confirmation to email: " + request.email)
    
    DRIVER.close()

def clickAndType(driver, xpath: str, message=""):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()
    if message:
        element.send_keys(message)
    
