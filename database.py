import pandas as pd

class database:

    def __init__(self):
        self.__drivers = pd.read_csv("drivers.csv")
        self.__driver_standings = pd.read_csv("driver_standings.csv")
        self.__laptimes = pd.read_csv("lap_times.csv")
        self.__qualifying = pd.read_csv("qualifying.csv")
        self.__circuits = pd.read_csv("circuits.csv")
        self.__races = pd.read_csv("races.csv")
        self.__seasons = pd.read_csv("seasons.csv")
        self.__constructors = pd.read_csv("constructors.csv")
        self.__contructor_standings = pd.read_csv("constructor_standings.csv")
        self.__constructor_results = pd.read_csv("constructor_standings.csv")
        self.__pitstops = pd.read_csv("pit_stops.csv")
        self.__sprint_results = pd.read_csv("sprint_results.csv")
        self.__status = pd.read_csv("status.csv")

    def getDrivers(self):
        return self.__drivers
    def getDriverStandings(self):
        return self.__driver_standings
    def getLaptimes(self):
        return self.__laptimes
    def getQualifying(self):
        return self.__qualifying
    def getCircuits(self):
        return self.__circuits
    def getRaces(self):
        return self.__races
    def getSeasons(self):
        return self.__seasons
    def getConstructors(self):
        return self.__constructors
    def getConstructorStandings(self):
        return self.__contructor_standings
    def getConstructorResults(self):
        return self.__constructor_results
    def getPitstops(self):
        return self.__pitstops
    def getSprintResults(self):
        return self.__sprint_results
    def getStatus(self):
        return self.__status
    