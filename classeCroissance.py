from _typeshed import Self
import datetime
from classPersonne import *
from classeElectroencephalogramme import *


class Croissance:
    patient: Enfant
    age: str
    poids: float
    taille: float
    cortex_cerebral: Electroencephalogramme

    def __init__(self, patient, age, poids, taille, cortex_cerebral):
        self.patient = patient
        self.age = age
        self.poids = poids
        self.taille = taille
        self.cortex_cerebral = cortex_cerebral
    
    def rapport_croissance(self):
        dic_croissance = dict()

        dic_croissance["Patient"] = Self.patient
        dic_croissance["Age"] = Self.age
        dic_croissance["Poids"] = Self.poids
        dic_croissance["Taille"] = Self.taille
        dic_croissance["Cortex cérébral"] = Self.cortex_cerebral

        return dic_croissance