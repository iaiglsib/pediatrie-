from _typeshed import Self
import datetime
from classPersonne import *
from classVaccination import *
from classeCroissance import *



#Creation de la classe Controle Progression Croissance
class CPC:
    patient: Enfant
    evolution: Croissance
    traitement: Vaccinnation
    prochaineVaccination: datetime.date

    def __init__(self, patient, evolution, traitement, prochaineVaccination):
        self.patient = patient
        self.evolution = evolution
        self.traitement = traitement
        self.prochaineVaccination = prochaineVaccination


    # enregistrer les données de consultation dans le fichier json consultation
    def Ajout_Nouveau_CPC(data):
        with open("CPC.json","rw", encoding="utf8") as file:
            d = json.load(file)
            for i, j in data.items() :
                d['consultation'][i] = j
            file.seek(0)
            json.dump(d,file,indent=4,ensure_ascii=False)