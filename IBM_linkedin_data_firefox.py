#import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime as dt
import pyperclip as pc
import regex as re
import csv

#Driver setup

#Page request

##edge_options = webdriver.Firefox()
##edge_options.use_chromium = True 
##edge_options.add_argument("user-data-dir=C:\\Users\\AMD HOME\\AppData\\Local\\Microsoft\\Edge\\User Data")
##edge_options.add_argument("profile-directory=Default")

#driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options = edge_options)

option = webdriver.FirefoxOptions()
#option.headless = True
#option.profile = webdriver.FirefoxProfile()
option.add_argument("-profile")
option.add_argument(r"C:\Users\AMD HOME\AppData\Roaming\Mozilla\Firefox\Profiles\jtkbs013.default-release-1")
#option.add_argument(r"profile-directory=jtkbs013.default-release-1")
#fp = webdriver.FirefoxProfile(r"C:\Users\AMD HOME\AppData\Local\Mozilla\Firefox\Profiles\jtkbs013.default-release-1")
driver = webdriver.Firefox(options=option)



driver.get("https://www.linkedin.com/company/ibm/posts/?feedView=all")
driver.find_elements(By.XPATH, """/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[1]/div/button[3]""")[0].click()
typ = driver.find_elements(By.XPATH, """/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[1]/div/button[3]""")[0].text

#time.sleep(5)#Time for loading
##driver.find_elements(By.XPATH, """/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/button""")[0].click()
##time.sleep(2)
##driver.find_elements(By.XPATH, """/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div/div/ul/li[2]/div/button""")[0].click()
##time.sleep(2)
#driver.execute_script("window.scrollTo(0, 1800)")
with open("IBM_post_data.csv","x", newline='') as file: 
            wr = csv.writer(file)
            wr.writerow(["postID", "tm_stamp", "typ", "fol", "react", "comments", "repost", "edit", "link", "exact_date"])
a = 0
b = 0
with open("text_data.txt","x") as file:
    pass
for i in range(1,500):
    
    print(f"{i} post str")
    WebDriverWait(driver, 200).until(
    EC.presence_of_element_located((By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div""")))
    text = driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div""")[0].text
    if 'IBM reposted this' in text:
        print('Repost wala')
        size = driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i+1}]""")[0].size
        b += size['height']
        driver.execute_script(f"window.scrollTo({a}, {b})")
        print('a: ',a," b: ",b)
        WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div""")))
        a = b
        with open("text_data.txt","a",encoding="utf-8") as file:
            file.write(f'{i} post str\n'+text+'\n{i} post end\n\n')
        continue
    with open("text_data.txt","a",encoding="utf-8") as file:
        file.write(f'{i} post str\n'+text+'\n{i} post end\n\n')
    #print(text)
    fol = int(re.findall('\d(?:\d|,|)+\d followers*', text)[0].split(' ')[0].replace(',',''))

    all_react = re.findall('\d(?:\d|,|)*\d\s(?:(?:.*?)others*\s)*(?:(?:\d|,|)*\d comments*\s)?(?:(?:\d|,|)*\d reposts*\s)?(?:.*?)\sComment\sRepost\sSend',text)[0].split('\n')
    if len(all_react)>7:
        print(all_react.pop(1))
    
    react = int(all_react[0].replace(',',''))
    
    if len(all_react)>5 and 'comment' in all_react[1]:
        comments = int(all_react[1].split(' ')[0].replace(',',''))
    else:
        comments = 0
        
    if len(all_react)>5 and ('repost' in all_react[2] or 'repost' in all_react[1]):
        pos = 2 if 'comment' in all_react[1] else 1
        repost = int(all_react[pos].split(' ')[0].replace(',',''))   
    else:
        repost = 0

        
    edit = 'yes' if len(re.findall('\d(\?:d|,|)*\d followers\s.*• Edited •', text))>0 else 'no'
    
    try:

        #/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[3]/div/button
        #/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[3]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/button
        #/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[3]/div/button
        driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/button""")[0].click()
        WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/div/div/ul/li[2]""")))
        driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/div/div/ul/li[2]""")[0].click()
        
        ##/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[3]/div/div[1]/div[{i}]/div/div/div/div/div/div[3]/div/div/div/ul/li[2]
        #/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[3]/div/div/div/ul/li[2]
        #driver.execute_script("arguments[0].click();", g)
        time.sleep(1)
        link = pc.paste()
        postID = re.findall('[0-9]{19}', link)
        tm_stamp = (int(postID[0]) >> len(bin(int(postID[0])))-43)//1000
        exact_date = dt.fromtimestamp(tm_stamp).strftime('%d-%m-%Y')
        #exact_date = time.ctime(tm_stamp)
        size = driver.find_elements(By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i+1}]""")[0].size
        #print(size)

        
        b += size['height']
        driver.execute_script(f"window.scrollTo({a}, {b})")
        print('a: ',a," b: ",b)
        WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, f"""/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[{i}]/div/div/div/div/div""")))
        a = b

        #print("yus i executed")
        #print('fol: \n',fol,'\nreact: \n',react,'\nedit: \n',edit,'\npostID:\n',postID)
        #ind = text.rfind('•')
        #txt = text[ind:ind+30].casefold().replace('\n',' ')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

        #print("Post ID: "+postID[0],"Type: "+typ,"followers: "+fol[0],"Reaction: "+react,"Edited : "+edit,"Link: "+link,sep='\n')
        row = [int(postID[0]), tm_stamp, typ, fol, react, comments, repost, edit, link, exact_date]
        #["postID", "tm_stamp", "typ", "fol", "react", "comments", "repost", "edit", "link", "exact_date"]
        #print(row)

        with open("IBM_post_data.csv","a",newline='') as file: 
            wr = csv.writer(file)
            wr.writerow(row)

    except Exception as e:
        print(f"not real post i value = {i}")
        print(traceback.format_exc())
        print(e)
    
        
##        driver.execute_script(f"window.scrollTo({a}, {b})")
##        time.sleep(5)
##        a = b
##        b = b+80
##        print("I also")


    print(f"{i}post end")

print("All done")



        






