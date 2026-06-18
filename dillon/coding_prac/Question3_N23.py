from datetime import date

class Character:
    def __init__(self, CharacterName: str, DateOfBirth: date, Intelligence: float, Speed: int):
        self.CharacterName = CharacterName 
        self.DateOfBirth = DateOfBirth 
        self.Intelligence = Intelligence 
        self.Speed = Speed 

    def GetIntelligence(self):
        return self.Intelligence

    def GetName(self):
        return self.CharacterName

    def SetIntelligence(self, intel: float):
        self.Intelligence = intel

    def Learn(self):

