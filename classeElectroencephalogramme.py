

import datetime
from classPersonne import *


#Classe Electroencephalogramme avec ses attributs type_ElectroEncephaloGramme,Frequence_onde,rythme, diagnostique,pronostique et d'un patient defint comme un enfant(de la classe enfant)
class Electroencephalogramme:
    type_EEG: str
    frequence_onde: str
    rythme: str
    diagnostique: str
    pronostique: str
    patient: Enfant

    def __init__(self, patient, type_EEG, frequence_onde, rythme, diagnostique, pronostique):
        self.patient = patient
        self.type_EEG = type_EEG
        self.frequence_onde = frequence_onde
        self.rythme = rythme
        self.diagnostique = diagnostique
        self.pronostique = pronostique