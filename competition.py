"""Defines the Competition class that holds the list of athletes"""

from athlete import Athlete
class Competition:
    """Defines the competition properties and the list of athletes"""

    #constant that defines the name of the file
    ATHLETE_DATA_FILE_NAME = "data/olympics.csv"

    #constant that defines the name of the medalists file
    MEDALISTS_DATA_FILE_NAME = "data/medalists.csv"

    def __init__(self):
        #1 to many HAS-A relationship between Competition and Athelete
        self._athleteList = []

    def load(self):
        """Loads the data file with all the althlete information"""
        #open the file
        athleteFile = None
        with open(Competition.ATHLETE_DATA_FILE_NAME, "r") as athleteFile:
            #read all the lines in the file
            competitionData = athleteFile.readlines()

            #go through each of the lines in the file
            headerRead = False
            for athleteRecord in competitionData:
                #skip the first line because it is the header of the file
                if not headerRead:
                    #mark the header as read
                    headerRead = True

                    #skip the rest of this iteration
                    continue

                #create an Athlete object
                athlete = Athlete(athleteRecord[:-1].split(","))

                #add the athelete the competition list
                self._athleteList.append(athlete)


    def save(self):
        """Saves the athlete information back to the data file"""
        pass

    def saveMedalists(self):
        """Saves all the athlets that have a medal"""
        with open(Competition.MEDALISTS_DATA_FILE_NAME, "w") as medalistsFile:
            #write the CSV header
            medalistsFile.write("Name,Gender,Age,Team,Event,Medal\n")

            #repeat for each athlete in the competition
            for athlete in self._athleteList:
                #check whether the athlete has a medal
                if athlete.wonMedal():
                    #write the athlete information in the medalists file
                    athleteRecord = f"{athlete.getName()},{athlete.getGender()},{athlete.getAge()},{athlete.getTeam()},{athlete.getEvent()},{athlete.getMedal()}\n"
                    
                    #write the record into the file
                    medalistsFile.write(athleteRecord)

        #NOTE: the file does not need to be closed because we used a context manager with the "with"


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
            