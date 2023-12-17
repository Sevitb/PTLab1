# -*- coding: utf-8 -*-

class HandleData():

    def filterByMark(self, studentsList) -> str:
        subjectsCount = 0
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
