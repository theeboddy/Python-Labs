import os
from pathlib import Path
import csv

class Iterator:
    def __init__(self, start = 0):
        self.num = start
    def __iter__(self):
        return self
    def __next__(self):
        num = self.num
        self.num += 1
        return num

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

    @staticmethod
    def is_adult(getAge):
        if getAge >= 18:
            return getAge

    def getGender(self, newGender):
        if newGender == 'Male':
            self.gender = newGender
        elif newGender == 'Female':
            self.gender = newGender
        return self.gender

class OfficeWorker(Human):
    def __init__(self, name, age, gender, date, post):
        Human.__init__(self, name, age, gender)
        self.date = date
        self.post = post
    def move(self, date):
        pass