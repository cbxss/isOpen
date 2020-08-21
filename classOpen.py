from selenium import webdriver
import time
from twilio.rest import Client
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import config
options = Options()
options.add_argument('--headless')    #comment this out if you want to see it in action
client = Client(config.account_sid, config.auth_token)
driver = webdriver.Chrome('./chromedriver', options=options)
driver.get('https://cmsweb.cms.csulb.edu/psc/CLBPRD/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGRD&EMPLID=017636084&INSTITUTION=LBCMP&STRM=2204')
driver.find_element_by_id("userid").send_keys(config.username)
driver.find_element_by_id("pwd").send_keys(config.password)
driver.find_element_by_name("Submit").click()
time.sleep(3)
def onPage():
    driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_SRCH").click()
    time.sleep(2)
    selec = Select(driver.find_element_by_id("SSR_CLSRCH_WRK_SUBJECT_SRCH$0"))
    selec.select_by_value(config.subject)
    driver.find_element_by_id("SSR_CLSRCH_WRK_CATALOG_NBR$1").send_keys(config.courseNumber)
    driver.find_element_by_id("CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH").click()
    time.sleep(2)
onPage()
i = True
while i:
    if "The search returns no results that match the criteria specified." in driver.page_source:
        print("classes full")
        time.sleep(900) #15 mins
        driver.get('https://cmsweb.cms.csulb.edu/psc/CLBPRD/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGRD&EMPLID=017636084&INSTITUTION=LBCMP&STRM=2204')
        time.sleep(2)
        onPage()
    else:
        print("theres a class open")
        message = client.messages.create(
            body='a class is open',
            from_=config.twilioNumber,
            to=config.myNumber
        )
        i = False
