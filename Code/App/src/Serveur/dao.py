import sqlite3

FK_ON = 'PRAGMA foreign_keys = 1'

BD_GEST_MEDIA = 'gestion_media.db'

# ***************** CLIENT *********************

CREER_CLIENT = '''
CREATE TABLE IF NOT EXISTS client
(
    idclient INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT,
    courriel TEXT,
    tel TEXT,
    compagnie TEXT,
    adresse TEXT,
    rue TEXT,
    ville TEXT
)'''
DROP_CLIENT = 'DROP TABLE IF EXISTS client'
INSERT_CLIENT = 'INSERT INTO client(nom, courriel, tel, compagnie, adresse, rue, ville) VALUES(?, ?, ?, ?, ?, ?, ?)'
SELECT_CLIENT = 'SELECT * FROM client'

# ***************** PROJET *********************

# CREER_PROJET = '''
# CREATE TABLE IF NOT EXISTS projet
# (
#     idprojet INTEGER PRIMARY KEY AUTOINCREMENT,
#     nomdeprojet TEXT UNIQUE,
#     client NUMERIC,
#     chargedeprojet NUMERIC,
#     datedelancement DATE,
#     datedefinprevue DATE
# )'''
# DROP_PROJET = 'DROP TABLE IF EXISTS projet'
# INSERT_PROJET = 'INSERT INTO projet(nomdeprojet, client, chargedeprojet, datedelancement, datedefinprevue) VALUES(?, ?, ?, ?, ?)'
# SELECT_PROJET = 'SELECT * FROM projet'

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

# ***************** MODULES *********************

CREER_MODULES = '''
CREATE TABLE IF NOT EXISTS modules
(
    idmodule INTEGER PRIMARY KEY AUTOINCREMENT,
    monmodule TEXT NOT NULL,
    version NUMERIC NOT NULL
)'''
DROP_MODULES = 'DROP TABLE IF EXISTS modules'
INSERT_MODULES = 'INSERT INTO modules(monmodule, version) VALUES(?, ?)'
SELECT_MODULES = 'SELECT * FROM modules'

# ***************** COMPAGNIE *********************

CREER_COMPAGNIE = '''
CREATE TABLE IF NOT EXISTS compagnie
(
    idcompagnie INTEGER PRIMARY KEY AUTOINCREMENT,
    nomcompagnie TEXT UNIQUE
)
'''
DROP_COMPAGNIE = 'DROP TABLE IF EXISTS compagnie'
INSERT_COMPAGNIE = 'INSERT INTO compagnie(nomcompagnie) VALUES(?)'
SELECT_COMPAGNIE = 'SELECT * FROM compagnie'

# ***************** MEMBRE *********************

CREER_MEMBRE = '''
CREATE TABLE IF NOT EXISTS membre
(
    idmembre INTEGER PRIMARY KEY AUTOINCREMENT,
    compagnie NUMERIC NOT NULL REFERENCES compagnie(idcompagnie),
    identifiant TEXT NOT NULL,
    mdp TEXT,
    permission TEXT NOT NULL,
    titre TEXT
)
'''
DROP_MEMBRE = 'DROP TABLE IF EXISTS membre'
INSERT_MEMBRE = 'INSERT INTO membre(compagnie, identifiant, mdp, permission, titre) VALUES(?, ?, ?, ?, ?)'
SELECT_MEMBRE = 'SELECT * FROM membre'

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



# TOUTES LES TABLES DE LIAISONS SERONTS MISE ICI 

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
