from datetime import datetime

class Subject:
    '''
    Class that represent a subject
    '''

    def __init__(self,json_data):
        #Get subject title
        self.__title = json_data["title"]
        #Get subject room
        self.__aula = json_data["aule"]
        #Get date info
        self.__start_info = datetime.strptime(json_data["start"],'%Y-%m-%dT%H:%M:%S')
        self.__end_info = datetime.strptime(json_data["end"],'%Y-%m-%dT%H:%M:%S')
        #Get start and stop clock
        self.__start_time = self.__start_info.time()
        self.__end_time = self.__end_info.time()
        self.__aula_text = ""
        #If the aule list is empty so it's ONLINE
        if len(self.__aula) == 0:
            self.__aula_text = "Online - Teams"
        else:
            self.__aula_text = self.__aula[0]["des_edificio"]

    def __str__(self):
        return f"{self.__title:<60}{str(self.__start_time)[:-3]} - {str(self.__end_time)[:-3]} @ {self.__aula_text}"

    def get_params(self):
        params_dict = {
            "title" : self.__title,
            "aula" : self.__aula,
            "start_info" : self.__start_info,
            "end_info" : self.__end_info,
            "start_time" : self.__start_time.strftime('%H:%M'),
            "end_time" : self.__end_time.strftime('%H:%M'),
            "aula_text" : self.__aula_text
        }

        return params_dict
