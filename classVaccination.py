from _typeshed import Self
import datetime
from classPersonne import *

class Vaccinnation:
    periode: str
    date_vaccination: datetime
    patient: Enfant
    vaccin: str
    pathologie_traite: str

    def __init__(self, periode, date_vaccination, patient, vaccin, pathologie_traite):
        self.periode = periode
        self.date_vaccination = date_vaccination
        self.vaccin = vaccin
        self.pathologie_traite = pathologie_traite
        self.patient = patient
    
    print("Informations sur l'enfant:")

    nom = input("Nom : ")
    prenom = input("Prenom : ")
    Nom_vaccin = input("Vaccin : ")
    age = input("Age : ")

    while age <= 0:
        age = int(input("Age : "))
        if age > 0:
            while sexe != 'M' or sexe != 'F':
                sexe = input("Sexe (Veuillez saisir M pour Homme et F pour Femme) : ")
                if (sexe == 'M') or (sexe == 'F'):
                        print("Informations du patient enregistrées !")
                        break
                break