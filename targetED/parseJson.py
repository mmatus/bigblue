#Convert JSON structures into Python objects

import json

def as_singleEntry(dct):
    value = dct.values()
    return value[0]

def as_quiz(dct):
    qType = dct["quizType"]
    sID = dct["sessionID"]
    qText = dct["questionText"]
    qChoices = dct["questionChoices"]
    qAnswer = dct["questionAnswer"]
    return qType,sID,qText,qChoices,qAnswer

def as_response(dct):
    qID = dct["quizID"]
    sID = dct["sessionID"]
    studLogin = dct["studentLogin"]
    studResp = dct["resp"]
    return qID,sID,studLogin,studResp
