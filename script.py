'''
    This is the main script.
    I will use the web service of UNIBO that returns JSON data in order to take the week timetable.

    url json service: https://corsi.unibo.it/laurea/IngegneriaScienzeInformatiche/orario-lezioni/@@orario_reale_json?anno=3&curricula=&start=2020-09-21&end=2020-09-28
'''
from datetime import date, timedelta,datetime
import requests
from core.subject import *

today = date.today()
#Get the info for the next 7 days
url = "https://corsi.unibo.it/laurea/IngegneriaScienzeInformatiche/orario-lezioni/@@orario_reale_json?anno=3&curricula=&start="+ str(today) +"&end=" + str(today + timedelta(days=7))
#url = "https://corsi.unibo.it/laurea/IngegneriaScienzeInformatiche/orario-lezioni/@@orario_reale_json?anno=3&curricula=&start=2020-09-21&end=2020-09-28"

#Load the service
result = requests.get(url);
data = result.json()

current_day = ""
#Cicle over all the subjects
for index in range(0, len(data)):
    json_data_subject = data[index]

    subject = Subject(json_data_subject)

    #If the day is different from previus, so this is another day
    if json_data_subject["start"][:10] != current_day[:10]:
        #New day
        current_day = json_data_subject["start"]
        current_date = datetime.strptime(current_day,'%Y-%m-%dT%H:%M:%S')
        print("\n\n" + str(current_date.day) + "/" + str(current_date.month) + "/" + str(current_date.year))
    
    #Print the base subject info
    print(subject)
