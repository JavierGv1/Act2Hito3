import random
import string
import fileinput
from time import sleep
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
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

BD = open("UsersPC.txt","r").read()
lines = BD.splitlines()
line = random.choice(lines)
split = line.split(',')
email = split[0]
psw = split[1]

letras = string.ascii_letters + string.digits
newpsw = ''.join(random.choice(letras) for i in range(20))

newline= email+','+newpsw

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"./chromedriver")
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
driver.get("https://www.pccomponentes.com/login")

sleep(2)
driver.find_element(By.ID,"username").send_keys(email)
sleep(3)
driver.find_element(By.ID ,"password").send_keys(psw)
sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']").click()

print("Email a utilizar : "+email)
print("Contraseña a utilizar : "+psw)
print("nueva contraseña a utilizar : "+newpsw)

driver.get("https://www.pccomponentes.com/usuarios/panel/mis-datos")
    
driver.find_element(By.NAME ,"user_password[password]").send_keys(psw)
driver.find_element(By.ID ,"userPassword_passwordConfirm").send_keys(newpsw)
driver.find_element(By.ID ,"userPassword_passwordConfirm2").send_keys(newpsw)
driver.find_element(By.ID,"user_password_create").send_keys(Keys.ENTER)

replace("UsersD2.txt",line,newline)

sleep(3)

driver.quit()