import sys
import json
import sqlite3

def select(args):
    connexion = sqlite3.connect("ressources/patients.db")
    curs = connexion.cursor()

    query = '''
    SELECT {}
    FROM patients 
    WHERE 1=1
    '''.format(args[0])  # Utilisation de la première valeur pour le SELECT

    conditions = []
    parameters = []

    # Ajoute les conditions basées sur les entrées de l'utilisateur
    if args[1]:
        conditions.append("Nom = ?")
        parameters.append(args[1])
    if args[2]:
        conditions.append("Age = ?")
        parameters.append(args[2])
    if args[3]:
        conditions.append("Sexe = ?")
        parameters.append(args[3])
    if args[4]:
        conditions.append("Diagnostic = ?")
        parameters.append(args[4])
    if args[5]:
        conditions.append("Profession = ?")
        parameters.append(args[5])
    if args[6]:
        conditions.append("Code_Postal = ?")
        parameters.append(args[6])

    # Ajoute les conditions à la requête si elles existent
    if conditions:
        query += " AND " + " AND ".join(conditions)

    res = curs.execute(query, parameters)

    result = res.fetchall()

    return result

def user_input():
    columns = input("Entrez les colonnes à sélectionner (ex: * ou Nom, Age): ")    
    nom = input("Entrez le nom (laisser vide pour ignorer) : ")
    age = input("Entrez l'âge (laisser vide pour ignorer) : ")
    sexe = input("Entrez le sexe (laisser vide pour ignorer) : ")
    diagnostic = input("Entrez le diagnostic (laisser vide pour ignorer) : ")
    profession = input("Entrez la profession (laisser vide pour ignorer) : ")
    code_postal = input("Entrez le code postal (laisser vide pour ignorer) : ")

    args = [
        columns,
        nom,
        age if age else None,
        sexe,
        diagnostic,
        profession,
        code_postal
    ]

    res = select(args)
    
    if len(res) == 0 :
        print()
        print("Personne n'a été identifié")
        print()
    else :
        print()
        print("***************** Personnes identifiées *****************")
        for e in res :
            print(e)
            print()



user_input()