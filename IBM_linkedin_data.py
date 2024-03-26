#import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import pyperclip as pc

#Driver setup

#Page request

edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True 
edge_options.add_argument("user-data-dir=C:\\Users\\AMD_LAPTOP\\AppData\\Local\\Microsoft\\Edge\\User Data")
edge_options.add_argument("profile-directory=Profile 2")

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options = edge_options)


driver.get("https://www.linkedin.com/company/ibm/posts/?feedView=all")
time.sleep(5)#Time for loading
driver.find_elements(By.XPATH, """/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/button""")[0].click()
time.sleep(2)
driver.find_elements(By.XPATH, """/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div/div/ul/li[2]/div/button""")[0].click()
time.sleep(2)
#driver.execute_script("window.scrollTo(0, 1800)")

a = 0
b = 768
for i in range(1,10):
    
    print(f"{i}th - post str")
    print(driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[3]/div/div[1]/div[{i}]/div/div/div/div""")[0].text)
    try:
        driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[3]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/button""")[0].click()
        #driver.execute_script("arguments[0].click();", d)
        time.sleep(4)
        driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[3]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/div/div/ul/li[2]""")[0].click()
        #driver.execute_script("arguments[0].click();", g)
        time.sleep(1)
        print(f"Link: {pc.paste()}")

    except Exception as e:
        print("not real post")
        print(e)

    driver.execute_script(f"window.scrollTo({a}, {b})")
    time.sleep(5)
    print(f"{i}th - post end")
    a = b
    b = b+768

'''
/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[3]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/button
/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[3]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/div/div/ul/li[2]
/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[3]/div/div[1]/div[9]/div/div/div/div/div/div[3]/div/button
/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[3]/div/div[1]/div[9]/div/div/div/div/div/div[3]/div/div/div/ul/li[2]
'''

        






