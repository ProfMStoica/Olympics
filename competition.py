"""Defines the Competition class that holds the list of athletes"""

from athlete import Athlete

import json

class Competition:
    """Defines the competition properties and the list of athletes"""

    #constant that defines the name of the file
    ATHLETE_DATA_FILE_NAME = "data/olympics.json"

    #constant that defines the name of the medalists file
    MEDALISTS_DATA_FILE_NAME = "data/medalists.json"

    def __init__(self):
        #1 to many HAS-A relationship between Competition and Athelete
        self._athleteList = []

    def load(self):
        """Loads the data file with all the althlete information"""
        #open the file
        athleteFile = None
        with open(Competition.ATHLETE_DATA_FILE_NAME, "r") as athleteFile:
            #read all the lines in the file
            competitionData = json.load(athleteFile)

            #go through each of the lines in the file
            for athleteRecord in competitionData:
                #create an Athlete object
                athlete = Athlete(athleteRecord)

                #add the athelete the competition list
                self._athleteList.append(athlete)


    def save(self):
        """Saves the athlete information back to the data file"""
        pass

    def saveMedalists(self):
        """Saves all the athlets that have a medal"""
        with open(Competition.MEDALISTS_DATA_FILE_NAME, "w") as medalistsFile:
            #build up the collection to save as JSON
            competitionData = []
            
            #repeat for each athlete in the competition
            for athlete in self._athleteList:
                #check whether the athlete has a medal
                if athlete.wonMedal():
                    #add the athlete's record into the competition data to be saved
                    competitionData.append(athlete.toDict())

            #save the competition data into the JSON file
            json.dump(competitionData, medalistsFile, indent = 4)
        
        #NOTE: the file does not need to be closed because we used a context manager with the "with" statement


    def printCompetitors(self):
        for athlete in self._athleteList:
            print()
            print(f"Name: {athlete.getName()}")
            print(f"Gender: {athlete.getGender()}")
            print(f"Gender: {athlete.getGender()}")
            print(f"Age: {athlete.getAge()}")
            print(f"Team: {athlete.getTeam()}")
            print(f"Event: {athlete.getEvent()}")
            print(f"Medal: {athlete.getMedal()}")
            