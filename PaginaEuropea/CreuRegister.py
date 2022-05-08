from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get("https://yopmail.com/es/email-generator")

email = driver.find_element(By.ID,"egen").text
split = email.split('@')
psw = split[0]
psw = psw.capitalize()
Wait5 = WebDriverWait(driver,5)
Wait20 = WebDriverWait(driver,20)
driver.get("https://www.creushop.com/es/")


element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i")))
driver.find_element(By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/div/ul/li[1]/a/span")))
driver.find_element(By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/div/ul/li[1]/a/span").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/form/div[7]/a")))
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/form/div[7]/a").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/form/div[3]/input")))
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/form/div[3]/input").send_keys("Bender")
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/form/div[4]/input").send_keys("Rodriguez")
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/form/div[5]/input").send_keys(email)
driver.find_element(By.XPATH,"//*[@id='index']/div[1]/div/div/div[2]/div[1]/div[2]/form/div[6]/input").send_keys(psw)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/form/div[7]/input").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/form/div[8]/button/span[2]").click()

sleep(5)
BD = open("UsersCreu.txt","a")
BD.write(email+','+psw+'\n')
BD.close()

element = Wait20.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i")))
driver.find_element(By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i").click()