import random
import string
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

BD = open("UsersD2.txt","r").read()
lines = BD.splitlines()
line = random.choice(lines)
split = line.split(',')
email = split[0]
psw = split[1]
splitmail = email.split('@')
correo = split[0]

letras = string.ascii_letters + string.digits
newpsw = ''.join(random.choice(letras) for i in range(20))

newline= email+','+newpsw

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()


driver.get("https://dust2.gg/mi-cuenta/lost-password/")
Dust2 = driver.current_window_handle
driver.find_element(By.ID,"user_login").send_keys(email)
driver.find_element(By.ID,"user_login").send_keys(Keys.ENTER)

pagina = 'https://yopmail.com/es/?login='+correo
driver.execute_script("window.open('"+pagina+"')")

sleep(3)

driver.quit()