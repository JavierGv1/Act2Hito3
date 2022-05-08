import random
import string
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove

def replace(file_path, Avengers, Finxters):
   fd, abs_path = mkstemp()
   with fdopen(fd,'w') as new_file:
       with open(file_path,'r') as old_file:
           for line in old_file:
               new_file.write(line.replace(Avengers,Finxters))
   copymode(file_path, abs_path)
   remove(file_path)
   move(abs_path, file_path)

BD = open("UsersCreu.txt","r").read()
lines = BD.splitlines()
line = random.choice(lines)
split = line.split(',')
email = split[0]
psw = split[1]

letras = string.ascii_letters + string.digits
newpsw = ''.join(random.choice(letras) for i in range(20))

newline= email+','+newpsw

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get("https://www.creushop.com/es/")

Wait5 = WebDriverWait(driver,5)
Wait20 = WebDriverWait(driver,20)

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i")))
driver.find_element(By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/div/ul/li[1]/a/span")))
driver.find_element(By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/div/ul/li[1]/a/span").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/form/div[3]/input")))
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/form/div[3]/input").send_keys(email)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/form/div[4]/input").send_keys(psw)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/form/div[6]/button/span[2]").click()

sleep(3)

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i")))
driver.find_element(By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/a/i").click()
element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/div/ul/li[2]/a")))
driver.find_element(By.XPATH,"/html/body/main/header/div/div[2]/div/div/div[3]/div[3]/div/ul/li[2]/a").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/section/div/div/div/section/section/div/div[1]/ul/li[1]/a/span")))
driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/section/section/div/div[1]/ul/li[1]/a/span").click()

element = Wait5.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/section/div/div/div/section/section/form/section/div[4]/div[1]/div/input")))
driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/section/section/form/section/div[4]/div[1]/div/input").send_keys(psw)
driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/section/section/form/section/div[5]/div[1]/div/input").send_keys(newpsw)

driver.find_element(By.XPATH,"//*[@id='cookieNoticeContent']/table/tbody/tr[1]/td[2]/span").click()

WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.CLASS_NAME, "closeButtonNormal")))
element = Wait5.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#customer-form > footer > button")))
driver.find_element(By.XPATH,"//*[@id='customer-form']/section/div[7]/div[1]/span/label").click()
driver.find_element(By.XPATH,"//*[@id='customer-form']/footer/button").click()

replace("UsersD2.txt",line,newline)