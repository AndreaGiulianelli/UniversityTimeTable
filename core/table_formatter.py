from core.subject import Subject
from termcolor import colored

def format_subject(subject):
    row_format = "│ {:31} │ {:49} │ {:26} │"
    subject_params = Subject.get_params(subject)
    
    time = colored(subject_params.get("start_time") + "-" + subject_params.get("end_time"), 'red')
    course = colored(subject_params.get("title"), 'blue')
    place = colored(subject_params.get("aula_text"), 'green')
    
    print(row_format.format(time, course, place))


def put_table_header(current_date):
    date_format = "┤ {:^20} ├"
    date_format = date_format.format(current_date.strftime('%m/%d/%Y') + f" {current_date.strftime('%A')}")
    date_format = colored(date_format, 'cyan')
    
    ret = """                                                                                              
               ┌──────────────────────┐                                                   
┌──────────────""" + date_format +  """─────────────────────────────┬───────────────────┐
│       Time   └─────────┬────────────┘    Course                   │       Place       │
├────────────────────────┼──────────────────────────────────────────┼───────────────────┤""";

    print(ret)

def put_table_footer():
    ret = "└────────────────────────┴──────────────────────────────────────────┴───────────────────┘";

    print(ret)