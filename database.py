import pandas as pd
from pathlib import Path

class database:

    def __init__(self):
        data_path = Path(__file__).parent / "data"
        self.__drivers = pd.read_csv(data_path / "drivers.csv")
        self.__driver_standings = pd.read_csv(data_path / "driver_standings.csv")
        self.__laptimes = pd.read_csv(data_path / "lap_times.csv")
        self.__qualifying = pd.read_csv(data_path / "qualifying.csv")
        self.__circuits = pd.read_csv(data_path / "circuits.csv")
        self.__races = pd.read_csv(data_path / "races.csv")
        self.__seasons = pd.read_csv(data_path / "seasons.csv")
        self.__constructors = pd.read_csv(data_path / "constructors.csv")
        self.__contructor_standings = pd.read_csv(data_path / "constructor_standings.csv")
        self.__constructor_results = pd.read_csv(data_path / "constructor_results.csv")
        self.__results = pd.read_csv(data_path / "results.csv")
        self.__pitstops = pd.read_csv(data_path / "pit_stops.csv")
        self.__sprint_results = pd.read_csv(data_path / "sprint_results.csv")
        self.__status = pd.read_csv(data_path / "status.csv")

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
    def getResults(self):
        return self.__results
    def getPitstops(self):
        return self.__pitstops
    def getSprintResults(self):
        return self.__sprint_results
    def getStatus(self):
        return self.__status
    