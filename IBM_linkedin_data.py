#import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pyperclip as pc
import regex as re

#Driver setup

#Page request

edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True 
edge_options.add_argument("user-data-dir=C:\\Users\\AMD HOME\\AppData\\Local\\Microsoft\\Edge\\User Data")
edge_options.add_argument("profile-directory=Default")

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options = edge_options)


driver.get("https://www.linkedin.com/company/ibm/posts/?feedView=all")
driver.find_elements(By.XPATH, """/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[1]/div/button[2]""")[0].click()

#time.sleep(5)#Time for loading
##driver.find_elements(By.XPATH, """/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/button""")[0].click()
##time.sleep(2)
##driver.find_elements(By.XPATH, """/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div/div/ul/li[2]/div/button""")[0].click()
##time.sleep(2)
#driver.execute_script("window.scrollTo(0, 1800)")

a = 0
b = 0
for i in range(1,10):
    
    print(f"----------------------------{i}th - post str-----------------------------------")
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div""")))
    text = driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div""")[0].text
    #print(text)
    fol = re.findall('\d(?:\d|,|)+\d followers*', text)
    react = re.findall('\d(?:\d|,|)*\d\s(?:\d|,|)*\d comments*\s(?:\d|,|)*\d reposts*', text)
    edit = re.findall('\d(\?:d|,|)*\d followers\s.*• Edited •', text)
    
    try:

        #/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[3]/div/button
        #/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[3]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/button
        #/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[3]/div/button
        driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/button""")[0].click()
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/div/div/ul/li[2]""")))
        driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/div/div/ul/li[2]""")[0].click()
        
        ##/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[3]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/div/div/ul/li[2]
        #/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[3]/div/div/div/ul/li[2]
        #driver.execute_script("arguments[0].click();", g)
        time.sleep(1)
        link = pc.paste()
        postID = re.findall('[0-9]{19}', link)

        size = driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]""")[0].size
        #print(size)

        
        b += size['height']
        driver.execute_script(f"window.scrollTo({a}, {b})")
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i+1}]/div/div/div/div/div""")))
        a = b

        #print("yus i executed")
        #print('fol: \n',fol,'\nreact: \n',react,'\nedit: \n',edit,'\npostID:\n',postID)
        ind = text.rfind('•')

        print("Post ID: "+postID[0],text[ind:ind+30].casefold().replace('\n',' '),"followers: "+fol[0],"Reaction: "+react[0],"Edited : "+('yes' if len(edit)>0 else 'no'),"Link: "+link,sep='\n')

    except Exception as e:
        print("not real post")
        print(traceback.format_exc())
        print(e)
    
        
##        driver.execute_script(f"window.scrollTo({a}, {b})")
##        time.sleep(5)
##        a = b
##        b = b+80
##        print("I also")


    print(f"---------------------------{i}th - post end-------------------")



        






