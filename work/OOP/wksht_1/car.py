class Car:
    def __init__(self, registration: str, make: str):
         self.__registration: str = registration
         self.__make: str = make
         self.__mileage: int = 0
         self.__date: str | None = None

    def get_registration(self):
        return self.__registration
    
    def get_make(self):
        return self.__make

    def get_mileage(self):
        return self.__mileage

    def get_date_of_inspection(self):
        return self.__date
    
    def set_inspection_data(self, mileage: int, date: str):
        self.__mileage = mileage
        self.__date = date
