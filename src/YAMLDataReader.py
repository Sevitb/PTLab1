# -*- coding: utf-8 -*-
import yaml
from Types import DataType
from DataReader import DataReader


class YAMLDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            studentsList = yaml.safe_load(file)
        return studentsList

    def filterByMark(self, studentsList) -> str:
        subjectsCount = 0
        result = "Студенты не найдены"
        for studentDict in studentsList:
            for student in studentDict:
                studentSubjectsCount = len(studentDict[student])
                for mark in studentDict[student]:
                    if (studentDict[student][mark] != 90):
                        subjectsCount = 0
                        break
                    subjectsCount += 1
                if (studentSubjectsCount == subjectsCount):
                    return student
        return "Студенты не найдены."
