#Creation de la classe "EvolutionNormal" et de ses valeurs par défauts

class EvolutionNormal():
    age: str
    poids: str
    taille: str
    perimetre_cranien: str

    Evolution_Normale = []
    dic_garcon = {}

    dic_garcon["Garcon_Phase1"] = '0 jour', '<4.3kg & >2.5kg', '<54cm & >45 cm', '<36 cm & >32 cm'
    dic_garcon["Garcon_Phase2"] = '1 semaine', '<4.7kg & >2.7kg', '<47cm & >37 cm', 'cc'
    dic_garcon["Garcon_Phase3"] = '1 mois', '<5.kg & >2.5kg', '<42 cm & >37 cm', 'cc'

    #a terminer par la suite
    
    Evolution_Normale.append(dic_garcon)

    print(Evolution_Normale)