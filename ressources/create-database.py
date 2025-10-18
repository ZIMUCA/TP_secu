import sys
import json
import sqlite3

json_file_path = 'patients.json'

def create_database(json_file_path):
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        ID INTEGER PRIMARY KEY,
        Nom TEXT,
        Age INTEGER,
        Sexe TEXT,
        Diagnostic TEXT,
        Profession TEXT,
        Code_Postal TEXT
    )
    ''')

    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for patient in data:
        cursor.execute('''
        INSERT INTO patients (
            ID, Nom, Age, Sexe, Diagnostic, Profession, Code_Postal
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            patient['ID'],
            patient['Nom'],
            patient['Age'],
            patient['Sexe'],
            patient['Diagnostic'],
            patient['Profession'],
            patient['Code_Postal'],
        ))

    conn.commit()
    conn.close()

create_database(json_file_path)