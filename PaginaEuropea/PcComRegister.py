from lib2to3.pgen2 import driver
from time import sleep
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get("https://yopmail.com/es/email-generator")

email = driver.find_element(By.ID,"egen").text
split = email.split('@')
psw = split[0]
psw = psw.capitalize()
Wait5 = WebDriverWait(driver,5)
Wait20 = WebDriverWait(driver,20)
driver.get("https://culers.fcbarcelona.com/auth/oauth/authenticate?response_type=code&client_id=7d560885-1c44-4206-a1cb-8169e3ea0522&redirect_uri=https:%2F%2Fsso.fcbarcelona.es%2Fsso-redirect&post_logout_uri=https:%2F%2Fsso.fcbarcelona.es%2Fsso-logout-redirect&scope=openid%20member_write&lang=es-ES&flow_id=register_only&ottRequest=0")


element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='fcbarcelona-button-accept']")))
driver.find_element(By.XPATH,"//*[@id='fcbarcelona-button-accept']").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-login/div/app-form-layout/div/div[2]/div[3]/div/aside[1]/div/div/form/div/div/div/div[2]/div/div/app-input/div/div[1]/input")))
driver.find_element(By.XPATH,"/html/body/app-root/app-login/div/app-form-layout/div/div[2]/div[3]/div/aside[1]/div/div/form/div/div/div/div[2]/div/div/app-input/div/div[1]/input").send_keys(email)
driver.find_element(By.XPATH,"//html/body/app-root/app-login/div/app-form-layout/div/div[2]/div[3]/div/aside[1]/div/div/form/div/div/div/div[4]/div/div/div/div/app-button/button").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-register/div/div/div/app-form-layout/div/div[2]/div[3]/div/aside[1]/div/form/div[1]/app-field[2]/div/div/app-field-input/div/input")))
driver.find_element(By.XPATH,"/html/body/app-root/app-register/div/div/div/app-form-layout/div/div[2]/div[3]/div/aside[1]/div/form/div[1]/app-field[2]/div/div/app-field-input/div/input").send_keys(psw)
driver.find_element(By.XPATH,"/html/body/app-root/app-register/div/div/div/app-form-layout/div/div[2]/div[3]/div/aside[1]/div/form/div[3]/div/div/app-button/button/span[1]").click()
sleep(3)

pagina = 'https://yopmail.com/es/?login='+email
driver.get(pagina)

element = Wait20.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='ifmail']")))
element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/div/div/div/table/tbody/tr[3]/td/div/a")))
driver.find_element(By.XPATH,"/html/body/main/div/div/div/table/tbody/tr[3]/td/div/a").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-onboarding-start/div/app-form-layout/div/div[2]/div[3]/div/aside[1]/div/div[3]/div/span")))
driver.find_element(By.XPATH,"/html/body/app-root/app-onboarding-start/div/app-form-layout/div/div[2]/div[3]/div/aside[1]/div/div[3]/div/span").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-onboarding-start/div/div[2]/app-form-layout[1]/div/div[2]/div[3]/div/aside[1]/form/div[2]/app-field[1]/div/div/app-field-input/div/input[2]")))
driver.find_element(By.XPATH,"/html/body/app-root/app-onboarding-start/div/div[2]/app-form-layout[1]/div/div[2]/div[3]/div/aside[1]/form/div[2]/app-field[1]/div/div/app-field-input/div/input[2]").send_keys("Bender")
driver.find_element(By.XPATH,"/html/body/app-root/app-onboarding-start/div/div[2]/app-form-layout[1]/div/div[2]/div[3]/div/aside[1]/form/div[2]/app-field[2]/div/div/app-field-input/div/input[2]").send_keys("Doblador Rodriguez")
driver.find_element(By.XPATH,"/html/body/app-root/app-onboarding-start/div/div[2]/app-form-layout[1]/div/div[2]/div[3]/div/aside[1]/form/button").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-onboarding-start/div/div[2]/app-form-layout[2]/div/div[2]/div[3]/div/aside[1]/form/div[2]/app-field/div/div/app-field-input-address/div/input[4]]")))
driver.find_element(By.XPATH,"/html/body/app-root/app-onboarding-start/div/div[2]/app-form-layout[2]/div/div[2]/div[3]/div/aside[1]/form/div[2]/app-field/div/div/app-field-input-address/div/input[4]").send_keys("New York")
driver.find_element(By.XPATH,"/html/body/app-root/app-onboarding-start/div/div[2]/app-form-layout[2]/div/div[2]/div[3]/div/aside[1]/form/button").click()

BD = open("UsersPC.txt","a")
BD.write(email+','+psw+'\n')
BD.close()
    