from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


chromepath = r"c:\chrome/chromedriver.exe";
driver = webdriver.Chrome(chromepath)
driver.get("https://www.facebook.com")
email = driver.find_element_by_name("email")
email.send_keys("<Your Facebook UserName>")
password = driver.find_element_by_name("pass")
password.send_keys('Your Password')
password.send_keys(Keys.ENTER)
driver.get('https://www.facebook.com/groups')
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
     match=True

matches = ['6' , 'اكتوبر','أكتوبر','السابع','الثامن','متميز' , 'سوميد']
links = driver.find_elements_by_css_selector("a[href*='/groups/']")
count=0
for elem in links:
    
     if any(x in elem.text for x in matches):
         elem.send_keys(Keys.CONTROL+Keys.ENTER)
         count=count+1
         
print(count)

