from ctypes.wintypes import CHAR
import datetime
import json
from random import choice
from typing import Any

from Ophtalmo.Patient import Patient

#Creation de la classe Id pour la gestion de l'id
class Id:
    lettre : Any

    def __init__(self) :
        self.lettre = [ chr(i) for i in range(48,123) if i <= 57 or (i >= 65 and i <=90) or (i >= 97) ]
    
    #methode pour genere l'id
    def id_genere(self):
        id = ''
        for i in range(4):
            if id != '':
                id += '-'
            for j in range(5):
                id += choice( self.lettre )
                
        return id

#Creation de la classe Personne
class Personne:
    id: str
    nom: str
    prenom: str
    sexe: CHAR(1)
    date_naissance: datetime
    lieu_naissance: str
    groupage: str
    adresse: str
    contact: int

    def __init__(self, nom, prenom, sexe, date_naissance, lieu_naissance, groupage, adresse, contact):
        indiq = Id()
        self.id = indiq.id_genere()
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.lieu_naissance = lieu_naissance
        self.groupage = groupage
        self.adresse = adresse
        self.contact = contact

#Creation de la classe Parent heritant de la classe Personne
class Parent(Personne):
    id: str
    type_heredite: str
    heredite: str

    def __init__(self, nom, prenom, sexe, date_naissance, lieu_naissance, groupage, heredite, type_heredite):
        indiq = Id()
        self.id = indiq.id_genere()
        self.heredite = heredite       
        self.type_heredite = type_heredite

        super().__init__(nom, prenom, sexe, date_naissance, lieu_naissance, groupage)


#Classe Enfant heritant de personne
class Enfant(Personne):
    pere: Parent
    mere: Parent

    def __init__(self, nom, prenom, sexe, date_naissance, lieu_naissance, groupage, pere, mere):
        indiq = Id()
        self.id = indiq.id_genere()
        self.pere = pere
        self.mere = mere
        super().__init__(nom, prenom, sexe, date_naissance, lieu_naissance, groupage)

    #Fonction qui retourne les informations concernant l'enfant
    def __repr__(self):
        return "Enfant: ({}) ({}) de sexe ({}) né le ({}) à ({}) possède un groupage de type ({})".format(self.nom, self.prenom, self.sexe, self.date_naissance, self.lieu_naissance, self.groupage)

#classe consultation
class Consultation:
    id: str
    nom: str
    prenom: str
    age: int
    sexe: CHAR(1)
    groupe_sanguin: str
    adresse: str
    contact: str
    taille: float
    poids: float
    taux_glycemie: float
    symptomes: str
    nom_medecin: str
    prenom_medecin: str
    contact_medecin: int

    nom_patient = input("Nom du patient: ")
    prenom_patient = input("Prenom du patient: ")
    age_patient = input("Qge du patient: ")
    nom_patient = input("Nom du patient: ")
    taille = float(input("Taille: "))
    poids = float(input("Poids: "))
    taux_glycemie = float(input("Taux de glycémie: "))
    symptomes = input("Symtôme(s) éventuel(s): ")
    nom_medecin = input("Nom du médécin pratiquant: ")
    prenom_medecin = input("Prénom du médécin pratiquant: ")
    contact_medecin = input("contact(s) du médécin pratiquant: ")

    # enregistrer les données de consultation dans le fichier json consultation
    def Ajout_Nouvelle_Consultation(data):
        with open("Consultation.json","rw", encoding="utf8") as file:
            d = json.load(file)
            for i, j in data.items() :
                d['consultation'][i] = j
            file.seek(0)
            json.dump(d,file,indent=4,ensure_ascii=False)

    # consulter les patients
    def consult(self, nom_medecin, prenom_medecin, contact_medecin) : 
        indiq = Id()
        code = indiq.id_genere()
        date = datetime.datetime.now()
        obj = {
            code : {
                "Enfant" : {
                    "nom" : self.nom,
                    "prenom" : self.prenom,
                    "age" : self.age,
                    "adresse" : self.adresse,
                    "contact" : self.contact,
                    "poids" : self.poids,
                    "taux_glycemie" : self.taux_glycemie,
                    "groupe_sanguin" : self.groupage,
                    "symp" : self.symptomes
                },
                "date_consult": date.date,
                "medecin" : {
                    "nom" : nom_medecin,
                    "prenom" : prenom_medecin,
                    "contact" : contact_medecin
                }
            }
        }
        obj.Ajout_Nouvelle_Consultation()
        return True

    # charger les données de consultation du fichier json consultation
    def Chargement_Consultation() :
        data = open("Consultation.json","r", encoding="utf8")
        store = json.loads(data.read())
        data.close()
        return store
