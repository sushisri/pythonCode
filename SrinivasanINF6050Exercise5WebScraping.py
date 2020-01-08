 # !/usr/bin/env python3  
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:43:59 2018

@author: Sushila Srinivasan
Course: INF6050 Intro Computer Programming
School: School of Information Science, Wayne State University
Assignment: Exercise #5 - Web Scraping
"""   
# import modules
from urllib.request import urlopen
from bs4 import BeautifulSoup

#user defined functions
def printToFile(url, arg1, arg2, arg3):
    
    #dataFromWeatherDotCom.txt
    #dataFromWayneDotEdu.txt
    #dataFromMtvDotCom.txt
    #dataFromUXMagDotCom.txt
    #dataFromUXPTADotCom.txt
    with open('dataFromPTADotCom.txt', 'w') as f:
        f.write("URL: "+url+"\n\n\n")
        f.write(arg1)
        f.write("\n")
        f.write(arg2)
        f.write("\n")
        f.write(arg3)
    f.close()
    
# url to scrape
page1="https://wayne.edu/about/"
page2="http://mtv.com/app"
page3="https://forecast.weather.gov/MapClick.php?CityName=Novi&state=MI&site=DTX&lat=42.4755&lon=-83.4905#.W_9QOGhKjIU"
page4="http://uxmag.com/"
page5="https://www.pta.org/home/programs/reflections"

# opening the url into webpage based on the url
webpage = urlopen(page5)

# parse the webpage
soup = BeautifulSoup(webpage.read(), 'html.parser')

# id to parse
page1_id="content"
page2_id="header"
page3_id="seven-day-forecast"
page4_id="content"
page5_id="page-container"

# id related info
main_output = soup.find(id=page5_id)


# class to parse
page1_class="content-container"
page2_class="site_menu_inner"
page3_class="tombstone-container"
page4_class="field-content"
page5_class="page-nav__sf-wrapper"

#class related info under the above id
output_details = main_output.find_all(class_=page5_class)

# getting details from the list
output_item = output_details[0]  

# getting second value
# arguments specific to mtv.com
#arg2 = output_item.find('ul')['itemtype']
#arg3 = output_item.find('a')['href']

#arguments to other url's
#arg2 = output_item.find('img')['src']
#arg3 = output_item.find('img')['alt']

#arguments specific to pta.com
arg2 = output_item.find('ul')['id']
arg3 = output_item.find('a')['href']

# making the out put indendent
arg1 = output_item.prettify()

#output to screen
print(arg1)
print(arg2)
print(arg3)

#out put to file
printToFile(page5, arg1, arg2, arg3)