
import datetime  
import time   
import requests  
from plyer import notification 
  
 
covidStats = None  
try:  
    covidStats = requests.get("https://corona-rest-api.herokuapp.com/Api/india")  
except:  
   
    print("Consider Checking the internet connection")  
  
 
if (covidStats != None):  
 
    jsonData = covidStats.json()['Success']  
      
    
    while(True):  
        notification.notify(  
              
            title = "COVID19 Stats on {}".format(datetime.date.today()),  
          
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths : {todaydeaths}\nTotal active : {active}".format(  
                        totalcases = jsonData['cases'],  
                        todaycases = jsonData['todayCases'],  
                        todaydeaths = jsonData['todayDeaths'],  
                        active = jsonData["active"]),  
          
        
            app_icon = "virus.ico",  
            
            timeout  = 30  
        )  
      
        time.sleep(60 * 60 * 12)  
