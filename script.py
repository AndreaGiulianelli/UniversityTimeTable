#!/usr/bin/env python3
'''
    This is the main script.
    I will use the web service of UNIBO that returns JSON data in order to take the week timetable.

    url json service: https://corsi.unibo.it/laurea/IngegneriaScienzeInformatiche/orario-lezioni/@@orario_reale_json?anno=3&curricula=&start=2020-09-21&end=2020-09-28
'''
from datetime import date, timedelta,datetime
import requests
from core.subject import Subject
#from colorama import Fore,init
import sys, getopt
import core.table_formatter as formatTable


def print_help():
    print(f"Usage\n-y <value> or --year <value> : specify custom year (between 1 and 3)\n-c : disable colors")


#Default is third year
year = 3
colors = True

#Handle arguments
try:
    opts, args = getopt.getopt(sys.argv[1:],"hy:c",["year"])
except getopt.GetoptError:
    print_help()
    sys.exit(2)

for opt,arg in opts:
    if opt == "-h":
        print_help()
    elif opt in ("-y","--year"):
        if not arg in ("1","2","3"):
            print_help()
            sys.exit(2)
        year = arg
    elif opt == "-c":
        colors = False


today = date.today()
#Get the info for the next 7 days
url = "https://corsi.unibo.it/laurea/IngegneriaScienzeInformatiche/orario-lezioni/@@orario_reale_json?anno="+str(year)+"&curricula=&start="+ str(today).strip() +"&end=" + str(today + timedelta(days=7))
#url = "https://corsi.unibo.it/laurea/IngegneriaScienzeInformatiche/orario-lezioni/@@orario_reale_json?anno=3&curricula=&start=2020-09-21&end=2020-09-28"

#Load the service
result = requests.get(url);
data = result.json()

#Init Colorama, for Windows :(
#init()

current_day = ""
#Cicle over all the subjects
for index in range(0, len(data)):
    json_data_subject = data[index]
    subject = Subject(json_data_subject)

    #If the day is different from previous, so this is another day
    if json_data_subject["start"][:10] != current_day[:10]:

        #New day
        #Close previous table
        formatTable.put_table_footer()
        #Open new table
        current_day = json_data_subject["start"]
        current_date = datetime.strptime(current_day,'%Y-%m-%dT%H:%M:%S')
        formatTable.put_table_header(current_date)
        
        """print((Fore.BLUE if colors == True else "") + f"\n\n{current_date.day}", end="/")
        print((Fore.GREEN if colors == True else "") + f"{current_date.month}", end="/")
        print((Fore.YELLOW if colors == True else "") + f"{current_date.year}", end=" ")
        print((Fore.CYAN if colors == True else "") + f"{current_date.strftime('%A')}")"""

    formatTable.format_subject(subject)
    
#Close last table
formatTable.put_table_footer()

    # Print the base subject info
    #print((Fore.RED if colors == True else "") + f"{subject}")


