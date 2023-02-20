import os
from pathlib import Path
import csv

class Human:
    "Базовый класс для определения человека"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def getName(self, newName):
        self.name = newName
        return self.name

    def getAge(self, newAge):
        if 0 < newAge < 100:
            self.age = newAge
        return self.age

    def getGender(self, newGender):
        if newGender == 'Male':
            self.gender = newGender
        elif newGender == 'Female':
            self.gender = newGender
        return self.gender

class OfficeWorker(Human):
    pass