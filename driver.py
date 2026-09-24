from database import database
class driver():

    def __init__(self,name,database: database):
        self.__name = name
        self.__driverDF= database.getDrivers().query(f"driverRef == '{self.__name}' ")
        self.__id = self.__driverDF['driverId']

    def getName(self):
        return self.__name
    def getDriverRecord(self):
        return self.__driverDF
    def getDriverID(self):
        return self.__id