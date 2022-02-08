

#Creation de la classe super-classe "Diagnostique_apgar" et de ses attributs
class Diagnostique_apgar:
    score: int
    pronostique: str

    def __init__(self, score, pronostique):
        self.score = score
        self.pronostique = pronostique

#Creation d'une classe fille "Couleur_de_peau" heritant de la classe mere "Diagnostique_apgar"
class Couleur_de_peau(Diagnostique_apgar):
    def __init__(self, score, pronostique):
        super().__init__(score, pronostique)

        if (score == 0):
            pronostique = "Le nourrisson a la peau; la paume de la main ou la plante du pied bleu pâle !"

        elif (score == 1):
            pronostique = "Le nourrison a le corps rose avec des extrémités bleutées !"

        elif (score == 2):
            pronostique = "Le nourrisson a la peau entièrement rose!"
        
        else:
            pronostique = "Aucun pronostique; Score APGAR d'apparence invalide."

#Creation d'une sous-classe "Pouls" heritant de la super-classe "Diagnostique_apgar"
class Pouls(Diagnostique_apgar):
    def __init__(self, score, pronostique):
        super().__init__(score, pronostique)
        
        if (score == 0):
            pronostique = "Désolé, aucune fréquence cardiaque noté; le nourrisson n'a aucun battement de coeur!"

        elif (score == 1):
            pronostique = "Le nourrison possède des battements cardiaques, à raison de moins de 100 battements par minute !"

        elif (score == 2):
            pronostique = "Le nourrison possède des battements, avec une fréquence cardiaque supérieure à 100 battements par minute !"
        
        else:
            pronostique = "Aucun pronostique; Score APGAR du Rythme Cardiaque invalide."

#Creation d'une sous-classe "Reponse_grimace" heritant de la super-classe "Diagnostique_apgar"
class Reponse_grimace(Diagnostique_apgar):
    def __init__(self, score, pronostique): 
        super().__init__(score, pronostique)
        
        if (score == 0):
            pronostique = "Le nourrisson ne montre aucune réaction, aucun réflexe aux stimulations!"

        elif (score == 1):
            pronostique = "Le nourrisson réagit avec des grimaces aux stimulations!"

        elif (score == 2):
            pronostique = "Le nourrisson a des grimaces et une toux, un éternuement ou un cri vigoureux!"
        
        else:
            pronostique = "Aucun pronostique; Score APGAR d'irritabilité réflexe invalide."


#Creation d'une classe fille "Activite" heritant de la classe mere "Diagnostique_apgar"
class Activite(Diagnostique_apgar):
    def __init__(self, score, pronostique):
        super().__init__(score, pronostique)

        if (score == 0):
            pronostique = "Les muscles du nourrisson sont lâches et souples!"

        elif (score == 1):
            pronostique = "Le nourrisson possède un certain tonus musculaire!"

        elif (score == 2):
            pronostique = "Le nourrisson a des mouvements vifs et actifs!"
        
        else:
            pronostique = "Aucun pronostique; Score APGAR de Tonus musculaire invalide."

#Creation d'une classe fille "Respiration" heritant de la classe mere "Diagnostique_apgar"
class Respiration(Diagnostique_apgar):
    def __init__(self, score, pronostique):
        super().__init__(score, pronostique)

        if (score == 0):
            pronostique = "Désolé, l'enfant ne respire pas !"

        elif (score == 1):
            pronostique = "L'enfant a une respiration lente ou irrégulière !"

        elif (score == 2):
            pronostique = "L'enfant pleure assez donc, respire bien !"
        
        else:
            pronostique = "Aucun pronostique; Score APGAR de respiration invalide."


#Creation de la classe Apgar avec declaration de ses attributs et initialisation du constructeur
class Apgar():
    morphologie: str
    etat: str
    apparence: Couleur_de_peau
    frequence_cardiaque: Pouls
    reflexe: Reponse_grimace
    tonicite_musculaire: Activite
    effort_respiratoire: Respiration

    def __init__(self, morphologie, etat, apparence, frequence_cardiaque, reflexe, tonicite_musculaire, effort_respiratoire):
        self.morphologie = morphologie
        self.etat = etat
        self.apparence = apparence
        self.frequence_cardiaque = frequence_cardiaque
        self.reflexe = reflexe
        self.tonicite_musculaire = tonicite_musculaire
        self.effort_respiratoire = effort_respiratoire