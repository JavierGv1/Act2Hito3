import random
import string
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

BD = open("UsersD2.txt","r").read()
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
driver.get("https://dust2.gg/mi-cuenta/")

driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID ,"password").send_keys(psw)
driver.find_element(By.NAME,"login").send_keys(Keys.ENTER)
print("Email a utilizar : "+email)
print("Contraseña a utilizar : "+psw)
print("nueva contraseña a utilizar : "+newpsw)
driver.get("https://dust2.gg/mi-cuenta/edit-account/")
nombre = driver.find_element(By.ID,"account_first_name").get_attribute('value')
if not nombre:
    driver.find_element(By.ID ,"account_first_name").send_keys("Bender")
    driver.find_element(By.ID ,"account_last_name").send_keys("Bending Rodriguez")
    
driver.find_element(By.ID ,"password_current").send_keys(psw)
driver.find_element(By.ID ,"password_1").send_keys(newpsw)
driver.find_element(By.ID ,"password_2").send_keys(newpsw)
driver.find_element(By.NAME,"save_account_details").send_keys(Keys.ENTER)

replace("UsersD2.txt",line,newline)

sleep(3)

driver.quit()