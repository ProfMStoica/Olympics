"""Defines the Athlete class"""

class Athlete:
    """Defines the athlete properties and functionality"""
    def __init__(self, initData = None):
        if initData == None:
            self._name = ""
            self._gender = ""
            self._age = 0
            self._team = None
            self._event = None
            self._medal = None
        else:
            #set its properties with the data read from the file
            self._name = initData["Name"]
            self._gender = initData["Gender"]
            self._age = int(initData["Age"])
            self._team = initData["Team"]
            self._event = initData["Event"]
            self._medal = initData["Medal"]            

    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name

    def getGender(self):
        return self._gender
    
    def setGender(self, gender):
        self._gender = gender

    def getAge(self):
        return self._age
    
    def setAge(self, age):
        self._age = age

    def getTeam(self):
        return self._team
    
    def setTeam(self, team):
        self._team = team

    def getEvent(self):
        return self._event
    
    def setEvent(self, event):
        self._event = event
        
    def getMedal(self):
        return self._medal
    
    def setMedal(self, medal):
        self._medal = medal

    def wonMedal(self):
        return self._medal != "NA"
    
    def toDict(self):
        return {
            "Name" : self._name,
            "Gender" : self._gender,
            "Age" : self._age,
            "Team" : self._team,
            "Event" : self._event,
            "Medal" : self._medal
        }                   
                    
    
    
    