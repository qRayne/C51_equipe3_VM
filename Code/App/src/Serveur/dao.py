import sqlite3

FK_ON = 'PRAGMA foreign_keys = 1'

BD_GEST_MEDIA = 'gestion_media.db'


# ***************** MODULE *********************
CREER_MODULE = '''
CREATE TABLE IF NOT EXISTS module
(
    id_module INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT,
    version NUMERIC NOT NULL,
    prixjour DECIMAL
)'''
DROP_MODULE = 'DROP TABLE IF EXISTS module'
INSERT_MODULE = 'INSERT INTO module(nom, version, prixjour) VALUES(?, ?, ?)'
SELECT_MODULE = 'SELECT * FROM module'


# ***************** ADRESSE *********************
CREER_ADRESSE = '''
CREATE TABLE IF NOT EXISTS adresse
(
    id_adresse INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    rue TEXT,
    numero NUMERIC,
    appartement TEXT,
    ville TEXT,
    province_etat TEXT,
    pays TEXT,
    codepostal TEXT
)
'''
DROP_ADRESSE = 'DROP TABLE IF EXISTS adresse'
INSERT_ADRESSE = 'INSERT INTO adresse(rue, numero, appartement, ville, province_etat, pays, codepostal) VALUES(?, ?, ?, ?, ?, ?, ?)'
SELECT_ADRESSE = 'SELECT * FROM ADRESSE'


# ***************** PERSONNE *********************
CREER_PERSONNE = '''
CREATE TABLE IF NOT EXISTS personne
(
    id_personne INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    courriel TEXT NOT NULL,
    adresse NUMERIC,
    telephone TEXT
)
'''
DROP_PERSONNE = 'DROP TABLE IF EXISTS personne'
INSERT_PERSONNE = 'INSERT INTO personne(nom, prenom, courriel, rue, numero, appartement, ville, province, pays, codepostal, telephone) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)' 
SELECT_PERSONNE = 'SELECT * FROM personne'


# ***************** LOCATEUR *********************
CREER_LOCATEUR = '''
CREATE TABLE IF NOT EXISTS locateur
(
    id_locateur INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nomcompagnie TEXT,
    adresse NUMERIC,
    telephone TEXT,
    admin NUMERIC
)
'''
DROP_LOCATEUR = 'DROP TABLE IF EXISTS locateur'
INSERT_LOCATEUR = 'INSERT INTO locateur(nomcompagnie, adresse, telephone, admin) VALUES(?, ?, ?, ?)'
SELECT_LOCATEUR = 'SELECT * FROM locateur'


# ***************** PERSONNE_MODULE *********************
CREER_PERSONNE_MODULE = '''
CREATE TABLE IF NOT EXISTS personne_module
(
    id_personne_module INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    personne NUMERIC NOT NULL, 
    module NUMERIC NOT NULL
)
'''
DROP_PERSONNE_MODULE = 'DROP TABLE IF EXISTS personne_module'
INSERT_PERSONNE_MODULE = 'INSERT INTO personne_module(personne, module) VALUES(?, ?, ?)'
SELECT_PERSONNE_MODULE = 'SELECT * FROM personne_module'
                

# ***************** ROLE *********************
CREER_ROLE = '''
CREATE TABLE IF NOT EXISTS role
(
    idrole  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    role TEXT
)
'''
DROP_ROLE = 'DROP TABLE IF EXISTS role'
INSERT_ROLE = 'INSERT INTO role(role) VALUES(?)'
SELECT_ROLE = 'SELECT * FROM role'


# ***************** FACTURE *********************
CREER_FACTURE = '''
CREATE TABLE IF NOT EXISTS facture
(
    id_facture INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    client NUMERIC,
    projet NUMERIC,
    montant DECIMAL,
    etat TEXT  
)
'''
DROP_FACTURE = 'DROP TABLE IF EXISTS facture'
INSERT_FACTURE = 'INSERT INTO facture(client, projet, montant, etat) VALUES(?, ?)'
SELECT_FACTURE = 'SELECT * FROM facture'


# ***************** MESSAGE *********************
CREER_MESSAGE = '''
CREATE TABLE IF NOT EXISTS message
(
    id_message INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    contenu TEXT,
    expediteur NUMERIC,
    destinataire NUMERIC
)
'''
DROP_MESSAGE = 'DROP TABLE IF EXISTS message'
INSERT_MESSAGE = 'INSERT INTO messsage(contenu, expediteur, destinataire) VALUES(?, ?, ?)'
SELECT_MESSAGE = 'SELECT * FROM message'



# ***************** PROJET *********************

CREER_PROJET = '''
CREATE TABLE IF NOT EXISTS projet
(
    id_projet INTEGER PRIMARY KEY AUTOINCREMENT,
    locateur INTEGER,
    debut_lancement_projet TIMESTAMP,
    fin_lancement_projet TIMESTAMP
)'''
# 1 FOREIGN KEY À METTRE (locateur)
DROP_PROJET = 'DROP TABLE IF EXISTS projet'
INSERT_PROJET = 'INSERT INTO projet(locateur,debut_lancement_projet,fin_lancement_projet) VALUES(?, ?, ?)'
SELECT_PROJET = 'SELECT * FROM projet'


# ***************** LOCAL *********************
CREER_LOCAL = '''
CREATE TABLE IF NOT EXISTS local
(
    id_local INTEGER PRIMARY KEY AUTOINCREMENT,
    adresse VARCHAR
)
'''
# FOREIGN KEY A ajouter (adresse)
DROP_LOCAL = 'DROP TABLE IF NOT EXISTS local'
INSERT_LOCAL = 'INSERT INTO local(adresse) VALUES (?)'
SELECT_LOCAL = 'SELECT * FROM LOCAL'


# ***************** EQUIPEMENT *********************
CREER_EQUIPEMENT = '''
CREATE TABLE IF NOT EXISTS equipement
(
    id_equipement INTEGER PRIMARY KEY AUTOINCREMENT,
    type_equipement VARCHAR,
    modele_equipement VARCHAR
)'''
DROP_EQUIPEMENT = 'DROP TABLE IF NOT EXISTS equipement'
INSERT_EQUIPEMENT = 'INSERT INTO equipement(type_equipement,modele_equipement) VALUES (?,?)'
SELECT_EQUIPEMENT = 'SELECT * FROM equipement'


# ***************** STATISTIQUE *********************
CREER_STATISTIQUE = '''
CREATE TABLE IF NOT EXISTS statistique
(
    id_statistique INTERGER PRIMARY KEY AUTOINCREMENT,
    module INTEGER,
    nb_utilistateur INTEGER
)'''
# FOREIGN KEY A ajouter (module)
DROP_STATISTIQUE = 'DROP TABLE IF NOT EXISTS statistique'
INSERT_STATISTIQUE = 'INSERT INTO statistique(module,nb_utilisateur) VALUES (?,?)'
SELECT_STATISTIQUE = 'SELECT * FROM statistique'


# ***************** TABLES DE LIAISONS *******************


# ***************** LOCATEUR_EMPLOYE *********************
CREER_LOCATEUR_EMPLOYE = '''
CREATE TABLE IF NOT EXISTS locateur_employe
(
    id_locateur_employe INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    locateur NUMERIC,
    employe NUMERIC,
    salaire DECIMAL
)
'''
DROP_LOCATEUR_EMPLOYE = 'DROP TABLE IF EXISTS locateur_employe'
INSERT_LOCATEUR_EMPLOYE = 'INSERT INTO locateur_employe(locateur, employe, salaire) VALUES(?, ?, ?)'
SELECT_LOCATEUR_EMPLOYE = 'SELECT * FROM locateur_employe'


# ***************** EMPLOYE_ROLE *********************
CREER_EMPLOYE_ROLE = '''
CREATE TABLE IF NOT EXISTS employe_role
(
    id_employe_role INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    employe NUMERIC,
    role NUMERIC
)
'''
DROP_EMPLOYE_ROLE = 'DROP TABLE IF EXISTS employe_role'
INSERT_EMPLOYE_ROLE = 'INSERT INTO employe_role(employe, role) VALUES(?, ?)'
SELECT_EMPLOYE_ROLE = 'SELECT * FROM employe_role'


# ***************** LOCATEUR_CLIENT *********************
CREER_LOCATEUR_CLIENT = '''
CREATE TABLE IF NOT EXISTS locateur_client
(
    id_locateur_client INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    locateur NUMERIC,
    client NUMERIC
)
'''
DROP_LOCATEUR_CLIENT = 'DROP TABLE IF EXISTS locateur_client'
INSERT_LOCATEUR_CLIENT = 'INSERT INTO locateur_client(locateur, personne) VALUES(?, ?)'
SELECT_LOCATEUR_CLIENT = 'SELECT * FROM locateur_client'


# ***************** LOCATEUR_EQUIPEMENT *********************
CREER_LOCATEUR_EQUIPEMENT = '''
CREATE TABLE IF NOT EXISTS locateur_equipement
(
    id_locateur_equipement INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    locateur NUMERIC,
    equipement NUMERIC,
    rangement NUMERIC,
    no_serie TEXT,
    date_achat DATE,
    valeur_achat DECIMAL,
    valeur_location DECIMAL
)
'''
DROP_LOCATEUR_EQUIPEMENT = 'DROP TABLE IF EXISTS LOCATEUR_EQUIPEMENT'
INSERT_LOCATEUR_EQUIPEMENT = 'INSERT INTO locateur_equipement(locateur, equipement, rangement, no_serie, date_achat, valeur_achat, valeur_location) VALUES(?, ?, ?, ?, ?, ?, ?)'
SELECT_LOCATEUR_EQUIPEMENT = 'SELECT * FROM locateur_equipement'


# ***************** PROJET_LOCALISATION *********************
# TABLE DE LIAISON
PROJET_LOCALISATION = '''
CREATE TABLE IF NOT EXISTS projet_localisation
(
    id_projet_localisation INTEGER PRIMARY KEY AUTOINCREMENT,
    localisation INTEGER,
    projet INTEGER
)'''
# 2 FOREIGN KEY À METTRE (localisation, projet)
DROP_PROJET_LOCALISATION = 'DROP TABLE IF EXISTS projet_localisation'
# INSERT_PROJET_LOCALISATION = FOREIGN KEY À FUSIONNER AFIN DE CRÉER UN ITEM
SELECT_PROJET_LOCALISATION = 'SELECT * FROM projet_localisation'


# ***************** PROJET_EMPLOYE *********************
# TABLE DE LIAISON
PROJET_EMPLOYE = '''
CREATE TABLE IF NOT EXISTS projet_employe
(
    id_projet_employe INTEGER PRIMARY KEY AUTOINCREMENT,
    projet INTEGER,
    employe INTERGER,
    locateur INTERGER
)'''
# 3 FOREIGN KEY À METTRE (projet, employe, locateur)
DROP_PROJET_EMPLOYE = 'DROP TABLE IF EXISTS projet_employe'
# INSERT_PROJET_EMPLOYE = FOREIGN KEY À FUSIONNER AFIN DE CRÉER UN ITEM
SELECT_PROJET_EMPLOYE = 'SELECT * FROM projet_employe'


# ***************** PROJET_EQUIPEMENT *********************
PROJET_EQUIPEMENT = '''
CREATE TABLE IF NOT EXISTS projet_equipement
(
    id_projet_equipement INTEGER PRIMARY KEY AUTOINCREMENT,
    projet INTEGER,
    equipement INTEGER
)'''
# 2 FOREIGN KEY À METTRE 
DROP_PROJET_EQUIPEMENT = 'DROP TABLE IF EXISTS projet_equipement'
# INSERT_PROJET_EQUIPEMENT = FOREIGN KEY À FUSIONNER AFIN DE CRÉER UN ITEM
SELECT_PROJET_EQUIPEMENT = 'SELECT * FROM projet_equipement'



# TOUS LES FOREIGNS KEYS SERONTS MISE ICI 
"""

"""
# mettre à jour cette partie après le ménage des tables
class Dao():
    __creer = [
        CREER_CLIENT,
        CREER_PROJET,
        CREER_MODULES,
        CREER_COMPAGNIE,
        CREER_MEMBRE,
        CREER_LOCAL,
        CREER_EQUIPEMENT,
        CREER_STATISTIQUE
    ]
    __detruire = [
        DROP_CLIENT,
        DROP_PROJET,
        DROP_MODULES,
        DROP_MEMBRE,
        DROP_COMPAGNIE,
        DROP_LOCAL,
        DROP_EQUIPEMENT,
        DROP_STATISTIQUE
    ]
    
    #singleton pas possible car:
    
    # sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 12960 and this is thread id 14996.  
    def __init__(self):
        self.chemin_bd = BD_GEST_MEDIA
        self.connexion()    

    def __del__(self):
        self.deconnexion()

    def connexion(self):
        self.conn = sqlite3.connect(self.chemin_bd)
        self.cur = self.conn.cursor()
        self.cur.execute(FK_ON)

    def deconnexion(self):
        self.cur.close()
        self.conn.close()

    def creer_bd(self):
        for table in Dao.__detruire:
            self.cur.execute(table)
        for table in Dao.__creer:
            self.cur.execute(table)

    def insert_membre(self, compagnie, identifiant, mdp, permission, titre):
        self.cur.execute(INSERT_MEMBRE, (compagnie, identifiant, mdp, permission, titre))
        self.conn.commit()

    def insert_compagnie(self, nomcompagnie):
        self.cur.execute(INSERT_COMPAGNIE, (nomcompagnie,))
        self.conn.commit()

    def select_membre(self):
        self.cur.execute(SELECT_MEMBRE)
        return self.cur.fetchall()

    def select_compagnie(self):
        self.cur.execute(SELECT_COMPAGNIE)
        return self.cur.fetchall()

    def identifier_usager(self, nom, mdp):
        sql = '''
            SELECT
                membre.identifiant,
                membre.permission,
                membre.titre,
                compagnie.idcompagnie,
                compagnie.nomcompagnie
            FROM membre
            INNER JOIN compagnie
            ON membre.compagnie = compagnie.idcompagnie
            WHERE membre.identifiant = ? AND membre.mdp = ?  
        '''
        self.cur.execute(sql, (nom, mdp))
        return self.cur.fetchall()


def main():
    Dao().creer_bd()
    return 0
#main

#print('Dans le module Dao: ', __name__)
if __name__ == '__main__':
    quit(main())
