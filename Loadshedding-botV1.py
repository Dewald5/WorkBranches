# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 15:23:32 2021

@author: Dewald
"""
from bs4 import BeautifulSoup
import requests
import time
websites = ['https://www.aldoshoes.co.za/find-a-store/','https://www.guess.co.za/find-a-store/']
websitesOnline = ['https://www.aldoshoes.co.za','https://www.guess.co.za','https://pringleofscotland.co.za/','https://www.callitspring.co.za/','https://www.mrtekkie.co.za/']#,'https://www.frontierco.co.za/frasers/','https://www.frontierco.co.za/busby-leather/ Ping seems to be disabled on frontierco
StoreName = []
StoreFinal = []
Province = ['eastern-cape','free-state','gauteng','kwazulu-natal','limpopo','mpumalanga','western-cape','namibia']
Up = []
Down = []
def Stores(): 
  for a in websites:
   print(a+'\n')
   for z in Province:
    URL = "{f}{ff}".format(f=a,ff=z)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    Pdata = soup.find(id='store')
    # find all option tag inside select tag
    Pdata2 = Pdata.find_all('option')
    # Iterate through all option tags and get inside text
    for z in Pdata2:
         StoreName.append(z.text)
         
def StoreCleanup():
 t = 0 
 t2 = 0
 Display = input("Enter Location \n")
 for a in StoreName:
    if a == 'Select Store':
     t2 +=1    
    else:
     StoreFinal.append(a)
 
 for b in StoreFinal:
  Storestr = b.split(',')
  if Storestr[1].upper() == " "+ str(Display.upper()):
   print("Store nr: "+str(t)+" "+StoreFinal[t])
  elif Display.upper() == "ALL":
      print("Store nr: "+str(t)+" "+StoreFinal[t])
  t += 1

def PingLive():
   for x in websitesOnline:
    try:
        response = requests.get(x)
        #print(int(response.status_code))
        if response.status_code == 200:
            Up.append(x)
        else:
            Down.append(x)
        time.sleep(1)
    except Exception as e:
        print("NO INTERNET"+ str(x)) 
        Down.append(x)
Stores()
StoreCleanup()
Websitelive = input("Check websites if live (Y/N)\n")
if Websitelive.upper() == "Y":
 PingLive()
 for i in Up:
  print("Online: "+str(i)+"\n")
  for e in Down:
   print("Offline: "+str(e)+"\n") 