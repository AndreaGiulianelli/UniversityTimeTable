from datetime import datetime
from core.subject import Subject
from colorama import Fore
import core.table_formatter as formatTable

def print_tabular_subject(data, colors):

    current_day = ""
    #Cycle over all the subjects
    for index in range(0, len(data)):
        json_data_subject = data[index]
        subject = Subject(json_data_subject)

        #If the day is different from previous, so this is another day
        if json_data_subject["start"][:10] != current_day[:10]:

            #New day
            current_day = json_data_subject["start"]
            current_date = datetime.strptime(current_day,'%Y-%m-%dT%H:%M:%S')

            if(index != 0):
                #Close previous table (not at the first iteration)
                formatTable.put_table_footer()

            #Open new table
            formatTable.put_table_header(current_date, colors)

        formatTable.format_subject(subject, colors)

    #Close last table
    formatTable.put_table_footer()


def print_listing_subject(data, colors):

    current_day = ""
    #Cycle over all the subjects
    for index in range(0, len(data)):
        json_data_subject = data[index]
        subject = Subject(json_data_subject)

        #If the day is different from previous, so this is another day
        if json_data_subject["start"][:10] != current_day[:10]:

            #New day
            current_day = json_data_subject["start"]
            current_date = datetime.strptime(current_day,'%Y-%m-%dT%H:%M:%S')

            print((Fore.BLUE if colors == True else "") + f"\n\n{current_date.day}", end="/")
            print((Fore.GREEN if colors == True else "") + f"{current_date.month}", end="/")
            print((Fore.YELLOW if colors == True else "") + f"{current_date.year}", end=" ")
            print((Fore.CYAN if colors == True else "") + f"{current_date.strftime('%A')}")
                
        # Print the base subject info
        print((Fore.RED if colors == True else "") + f"{subject}")