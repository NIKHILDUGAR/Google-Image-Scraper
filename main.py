#This program uses web scraping to download images from google image search instantly and can be helpful in making image datasets.
#This uses web scraping and Selenium to scroll the webpage and get more images. Do not close the browser window that pops up, 
#it will close automatically. The images will be labelled 1.jpg,2.jpg,3.jpg and so on or by the item names given on Google 
#and will be download in a folder with the same name as what you have searched.
#NOTE:- THIS PROGRAM ASSUMES YOU HAVE CHROME VERSION 83 AS YOUR BROWSER AND YOU HAVE THE chromedriver.exe TOO FROM GITHUB INSTEAD OF JUST THIS PROGRAM ELSE IT WILL NOT WORK.


import os
import re
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup as soup
sear = input('What are you looking for? ')
n_images = int(input('How many images do you want? '))
saveby= int(input("Do you want to save files by item names(enter 0) or ordered numbers(enter 1)? "))
GOOGLE_IMAGE = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
searchurl = GOOGLE_IMAGE + 'q=' + sear.replace(" ","+")
print(searchurl)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get(searchurl)
import time
if not os.path.exists("D://images"):
    os.mkdir("D://images")
save_path = 'D://images//'

completeName = os.path.join(save_path,sear)
if not os.path.exists(completeName):
    os.mkdir(completeName)
# print(driver.title)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
try:
    sbutton = driver.find_element_by_class_name("mye4qd")
    sbutton.click()
except:
    print("")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
src=driver.page_source
driver.close()
page_soup = soup(src, "lxml")
j = os.path.join('D://images', sear)
linkcontainers = page_soup.findAll("img", {"class": "rg_i Q4LuWd tx8vtf"})
namecontainers=page_soup.findAll("div", {"class": "bRMDJf islir"})
n_images=min(n_images,len(namecontainers))
print("no. of images available:",len(namecontainers))
print("no. of images to be downloaded:",n_images)
for i in range(n_images):
    link=None
    try:
        link = linkcontainers[i][src]
    except:
        try:
            link = linkcontainers[i]["data-src"]
        except:
            try:
                link = linkcontainers[i]["src"]
            except:
                try:
                    link = linkcontainers[i]["src"][src]["data-src"]
                    break
                except:
                    print(linkcontainers[i])
    if saveby:
        completeName = os.path.join(j, str(i+1) + ".jpg")
    else:
        name = namecontainers[i].img['alt'].replace("|", ",").replace("\\\\", " ").replace(".", "")
        name = re.sub('[^a-zA-Z0-9 \n\.]', '', name)
        completeName = os.path.join(j, name + ".jpg")
    f = open(completeName, 'wb')
    if link:
        f.write(urllib.request.urlopen(link).read())
    else:
        print(i)
        print("NOT WORKING")
        print("If you are seeing this then email me at nikhil4709@gmail.com Thank you!")
        print(linkcontainers[i])
    f.close()
    print(i+1," Images downloaded till now")
print('Done')
