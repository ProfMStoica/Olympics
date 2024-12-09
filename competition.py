"""Defines the Competition class that holds the list of athletes"""

from athlete import Athlete
class Competition:
    """Defines the competition properties and the list of athletes"""

    #constant that defines the name of the file
    ATHLETE_DATA_FILE_NAME = "data/olympics.csv"

    def __init__(self):
        #1 to many HAS-A relationship between Competition and Athelete
        self._athleteList = []

    def load(self):
        """Loads the data file with all the althlete information"""
        #open the file
        athleteFile = open(Competition.ATHLETE_DATA_FILE_NAME, "r")

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
            athlete = Athlete()

            #set its properties with the data read from the file
            athleteData = athleteRecord[:-1].split(",")
            athlete.setName(athleteData[0])
            athlete.setGender(athleteData[1])
            athlete.setAge(athleteData[2])
            athlete.setTeam(athleteData[3])
            athlete.setEvent(athleteData[4])
            athlete.setMedal(athleteData[5])

            #add the athelete the competition list
            self._athleteList.append(athlete)

        #close file
        athleteFile.close() 


    def save(self):
        """Saves the atlehte information back to the data file"""
        pass

    def printCompetitors(self):
        for athlete in self._athleteList:
            print()
            print(f"Name: {athlete.getName()}\n")
            print(f"Gender: {athlete.getGender()}\n")
            print(f"Gender: {athlete.getGender()}\n")
            print(f"Age: {athlete.getAge()}\n")
            print(f"Team: {athlete.getTeam()}\n")
            print(f"Event: {athlete.getEvent()}\n")
            print(f"Medal: {athlete.getMedal()}\n")
            