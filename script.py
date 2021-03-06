#!/usr/bin/env python3
'''
    This is the main script.
    I will use the web service of UNIBO that returns JSON data in order to take the week timetable.

    url json service: https://corsi.unibo.it/laurea/IngegneriaScienzeInformatiche/orario-lezioni/@@orario_reale_json?anno=3&curricula=&start=2020-09-21&end=2020-09-28
'''
from datetime import date, timedelta
import requests
from colorama import init
import sys, getopt
import core.printer as printer

def print_help():
    print(f"Usage\n-y <value> or --year <value> : specify custom year (between 1 and 3)\n-c : disable colors\n-t or --tabular : show tabular view")


#Default is third year
year = 3
colors = True
tabular = False

#Handle arguments
try:
    opts, args = getopt.getopt(sys.argv[1:],"hy:ct",["year","tabular"])
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
    elif opt in ("-t","--tabular"):
        tabular = True

today = date.today()
#Get the info for the next 7 days
url = "https://corsi.unibo.it/laurea/IngegneriaScienzeInformatiche/orario-lezioni/@@orario_reale_json?anno="+str(year)+"&curricula=&start="+ str(today).strip() +"&end=" + str(today + timedelta(days=7))
#url = "https://corsi.unibo.it/laurea/IngegneriaScienzeInformatiche/orario-lezioni/@@orario_reale_json?anno=3&curricula=&start=2020-09-21&end=2020-09-28"

#Load the service
result = requests.get(url);
data = result.json()

#Init Colorama, for Windows :(
init()

if tabular is True:
    printer.print_tabular_subject(data, colors);
else:
    printer.print_listing_subject(data, colors);