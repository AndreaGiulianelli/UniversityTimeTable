from core.subject import Subject

def format_subject(subject):
    row_format = "│ {:22} │ {:40} │ {:17} │"
    subject_params = Subject.get_params(subject)
    
    time = subject_params.get("start_time") + "-" + subject_params.get("end_time");
    course = subject_params.get("title")
    place = subject_params.get("aula_text")
    
    print(row_format.format(time, course, place))


def put_table_header(current_date):
    date_format = "┤ {:^20} ├"
    date_format = date_format.format(current_date.strftime('%m/%d/%Y') + f" {current_date.strftime('%A')}")
    ret = """                                                                                              
               ┌──────────────────────┐                                                   
┌──────────────""" + date_format +  """─────────────────────────────┬───────────────────┐
│       Time   └─────────┬────────────┘    Course                   │       Place       │
├────────────────────────┼──────────────────────────────────────────┼───────────────────┤""";

    print(ret)

def put_table_footer():
    ret = "└────────────────────────┴──────────────────────────────────────────┴───────────────────┘";

    print(ret)