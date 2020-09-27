from core.subject import Subject
from termcolor import colored

def format_subject(subject, colors):
    
    subject_params = Subject.get_params(subject)
    time = subject_params.get("start_time") + "-" + subject_params.get("end_time")
    course = subject_params.get("title")
    place = subject_params.get("aula_text")

    if colors is True:
        time = colored(time, 'red')
        course = colored(course, 'blue')
        place = colored(place, 'green')
        row_format = "│ {:31} │ {:49} │ {:26} │"
    else:
        row_format = "│ {:22} │ {:40} │ {:17} │"
    
    print(row_format.format(time, course, place))


def put_table_header(current_date, colors):

    date_format = "┤ {:^20} ├"
    date_format = date_format.format(" ".join([current_date.strftime('%m/%d/%Y'), current_date.strftime('%A')]))

    if colors is True:
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