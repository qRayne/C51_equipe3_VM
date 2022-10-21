import sqlite3

FK_ON = 'PRAGMA foreign_keys = 1'

BD_GEST_MEDIA = 'gestion_media.db'


# ***************** ADRESSE *********************
CREER_ADRESSE = '''
CREATE TABLE IF NOT EXISTS adresse
(
    id_adresse INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    rue TEXT,
    numero INTEGER,
    appartement TEXT,
    ville TEXT,
    province_etat TEXT,
    pays TEXT,
    code_postal TEXT
)
'''
DROP_ADRESSE = 'DROP TABLE IF EXISTS adresse'
INSERT_ADRESSE = 'INSERT INTO adresse(rue, numero, appartement, ville, province_etat, pays, code_postal) VALUES(?, ?, ?, ?, ?, ?, ?)'
SELECT_ADRESSE = 'SELECT * FROM ADRESSE'


# ***************** PERSONNE *********************
CREER_PERSONNE = '''
CREATE TABLE IF NOT EXISTS personne
(
    id_personne INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    courriel TEXT UNIQUE NOT NULL,
    adresse INTEGER REFERENCES adresse(id_adresse),
    telephone TEXT
)
'''
DROP_PERSONNE = 'DROP TABLE IF EXISTS personne'
INSERT_PERSONNE = 'INSERT INTO personne(nom, prenom, courriel, rue, numero, appartement, ville, province, pays, codepostal, telephone) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)' 
SELECT_PERSONNE = 'SELECT * FROM personne'


# ***************** MODULE *********************
CREER_MODULE = '''
CREATE TABLE IF NOT EXISTS module
(
    id_module INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT,
    version INTEGER,
    prix_jour REAL
)
'''
DROP_MODULE = 'DROP TABLE IF EXISTS module'
INSERT_MODULE = 'INSERT INTO module(nom, version, prixjour) VALUES(?, ?, ?)'
SELECT_MODULE = 'SELECT * FROM module'


# ***************** LOCATEUR *********************
CREER_LOCATEUR = '''
CREATE TABLE IF NOT EXISTS locateur
(
    id_locateur INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom_compagnie TEXT UNIQUE NOT NULL,
    telephone TEXT,
    adresse INTEGER REFERENCES adresse(id_adresse)
)
'''
DROP_LOCATEUR = 'DROP TABLE IF EXISTS locateur'
INSERT_LOCATEUR = 'INSERT INTO locateur(nom_compagnie, telephone, adresse) VALUES(?, ?, ?)'
SELECT_LOCATEUR = 'SELECT * FROM locateur'

# ***************** USAGER *********************

CREER_USAGER = '''
CREATE TABLE IF NOT EXISTS usager
(
    id_usager INTEGER PRIMARY KEY AUTOINCREMENT,
    usager INTEGER NOT NULL REFERENCES personne(id_personne),
    locateur INTEGER NOT NULL REFERENCES locateur(id_locateur),
    identifiant TEXT NOT NULL,
    mdp TEXT,
    permission TEXT NOT NULL
)
'''
DROP_USAGER = 'DROP TABLE IF EXISTS usager'
INSERT_USAGER = 'INSERT INTO membre(usager, locateur, identifiant, mdp, permission) VALUES(?, ?, ?, ?, ?)'
SELECT_USAGER = 'SELECT * FROM usager'


# ***************** EQUIPEMENT *********************
CREER_EQUIPEMENT = '''
CREATE TABLE IF NOT EXISTS equipement
(
    id_equipement INTEGER PRIMARY KEY AUTOINCREMENT,
    type_equipement TEXT,
    modele_equipement TEXT
)
'''
DROP_EQUIPEMENT = 'DROP TABLE IF NOT EXISTS equipement'
INSERT_EQUIPEMENT = 'INSERT INTO equipement(type_equipement,modele_equipement) VALUES (?,?)'
SELECT_EQUIPEMENT = 'SELECT * FROM equipement'


# ***************** LOCAL *********************
CREER_LOCAL = '''
CREATE TABLE IF NOT EXISTS local
(
    id_local INTEGER PRIMARY KEY AUTOINCREMENT,
    adresse INTEGER REFERENCES adresse(id_adresse)
)
'''
# FOREIGN KEY A ajouter (adresse)
DROP_LOCAL = 'DROP TABLE IF NOT EXISTS local'
INSERT_LOCAL = 'INSERT INTO local(adresse) VALUES (?)'
SELECT_LOCAL = 'SELECT * FROM LOCAL'


# ***************** PROJET *********************

CREER_PROJET = '''
CREATE TABLE IF NOT EXISTS projet
(
    id_projet INTEGER PRIMARY KEY AUTOINCREMENT,
    locateur INTEGER REFERENCES locateur(id_locateur),
    debut NUMERIC,
    fin NUMERIC
)
'''
# 1 FOREIGN KEY À METTRE (locateur)
DROP_PROJET = 'DROP TABLE IF EXISTS projet'
INSERT_PROJET = 'INSERT INTO projet(locateur,debut, fin) VALUES(?, ?, ?)'
SELECT_PROJET = 'SELECT * FROM projet'


# ***************** FACTURE_LOCATEUR *********************
CREER_FACTURE_LOCATEUR = '''
CREATE TABLE IF NOT EXISTS facture_locateur
(
    id_facture_locateur INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    locateur INTEGER REFERENCES locateur(id_locateur),
    detail TEXT,
    montant REAL,
    statut TEXT  
)
'''
DROP_FACTURE_LOCATEUR = 'DROP TABLE IF EXISTS facture_locateur'
INSERT_FACTURE_LOCATEUR = 'INSERT INTO facture_locateur(client, detail, montant, statut) VALUES(?, ?, ?, ?)'
SELECT_FACTURE_LOCATEUR = 'SELECT * FROM facture_locateur'


# ***************** STATISTIQUE *********************
CREER_STATISTIQUE = '''
CREATE TABLE IF NOT EXISTS statistique
(
    id_statistique INTERGER PRIMARY KEY AUTOINCREMENT,
    module INTEGER REFERENCES module(id_module),
    nb_utilistateur INTEGER
)
'''
# FOREIGN KEY A ajouter (module)
DROP_STATISTIQUE = 'DROP TABLE IF NOT EXISTS statistique'
INSERT_STATISTIQUE = 'INSERT INTO statistique(module,nb_utilisateur) VALUES (?,?)'
SELECT_STATISTIQUE = 'SELECT * FROM statistique'


# ***************** ROLE *********************
CREER_ROLE = '''
CREATE TABLE IF NOT EXISTS role
(
    id_role  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    role TEXT
)
'''
DROP_ROLE = 'DROP TABLE IF EXISTS role'
INSERT_ROLE = 'INSERT INTO role(role) VALUES(?)'
SELECT_ROLE = 'SELECT * FROM role'


# ***************** MESSAGE *********************
CREER_MESSAGE = '''
CREATE TABLE IF NOT EXISTS message
(
    id_message INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    contenu TEXT,
    expediteur INTEGER REFERENCES personne(id_personne),
    destinataire INTEGER REFERENCES personne(id_personne)
)
'''
DROP_MESSAGE = 'DROP TABLE IF EXISTS message'
INSERT_MESSAGE = 'INSERT INTO messsage(contenu, expediteur, destinataire) VALUES(?, ?, ?)'
SELECT_MESSAGE = 'SELECT * FROM message'


# ***************** PERSONNE_MODULE *********************
CREER_PERSONNE_MODULE = '''
CREATE TABLE IF NOT EXISTS personne_module
(
    id_personne_module INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    personne INTEGER REFERENCES personne(id_personne), 
    module INTEGER REFERENCES module(id_module)
)
'''
DROP_PERSONNE_MODULE = 'DROP TABLE IF EXISTS personne_module'
# FK
#INSERT_PERSONNE_MODULE = 'INSERT INTO personne_module(personne, module) VALUES(?, ?, ?)'
SELECT_PERSONNE_MODULE = 'SELECT * FROM personne_module'


# ***************** LOCATEUR_EMPLOYE *********************
CREER_LOCATEUR_EMPLOYE = '''
CREATE TABLE IF NOT EXISTS locateur_employe
(
    id_locateur_employe INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    locateur INTEGER REFERENCES locateur(id_locateur),
    employe INTEGER REFERENCES personne(id_personne),
    salaire REAL
)
'''
DROP_LOCATEUR_EMPLOYE = 'DROP TABLE IF EXISTS locateur_employe'
# FK
#INSERT_LOCATEUR_EMPLOYE = 'INSERT INTO locateur_employe(locateur, employe, salaire) VALUES(?, ?, ?)'
SELECT_LOCATEUR_EMPLOYE = 'SELECT * FROM locateur_employe'


# ***************** EMPLOYE_ROLE *********************
CREER_EMPLOYE_ROLE = '''
CREATE TABLE IF NOT EXISTS employe_role
(
    id_employe_role INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    employe INTEGER REFERENCES personne(id_personne),
    role INTEGER
)
'''
DROP_EMPLOYE_ROLE = 'DROP TABLE IF EXISTS employe_role'
# FK
#INSERT_EMPLOYE_ROLE = 'INSERT INTO employe_role(employe, role) VALUES(?, ?)'
SELECT_EMPLOYE_ROLE = 'SELECT * FROM employe_role'


# ***************** LOCATEUR_EQUIPEMENT *********************
CREER_LOCATEUR_EQUIPEMENT = '''
CREATE TABLE IF NOT EXISTS locateur_equipement
(
    id_locateur_equipement INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    locateur INTEGER REFERENCES locateur(id_locateur),
    equipement INTEGER REFERENCES equipement(id_equipement),
    rangement INTEGER REFERENCES local(id_local),
    no_serie TEXT,
    date_achat NUMERIC,
    valeur_achat REAL,
    valeur_location REAL
)
'''
DROP_LOCATEUR_EQUIPEMENT = 'DROP TABLE IF EXISTS LOCATEUR_EQUIPEMENT'
# FK
#INSERT_LOCATEUR_EQUIPEMENT = 'INSERT INTO locateur_equipement(locateur, equipement, rangement, no_serie, date_achat, valeur_achat, valeur_location) VALUES(?, ?, ?, ?, ?, ?, ?)'
SELECT_LOCATEUR_EQUIPEMENT = 'SELECT * FROM locateur_equipement'


# ***************** LOCATEUR_CLIENT *********************
CREER_LOCATEUR_CLIENT = '''
CREATE TABLE IF NOT EXISTS locateur_client
(
    id_locateur_client INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    locateur INTEGER REFERENCES locateur(id_locateur),
    client INTEGER REFERENCES personne(id_personne)
)
'''
DROP_LOCATEUR_CLIENT = 'DROP TABLE IF EXISTS locateur_client'
# FK
#INSERT_LOCATEUR_CLIENT = 'INSERT INTO locateur_client(locateur, personne) VALUES(?, ?)'
SELECT_LOCATEUR_CLIENT = 'SELECT * FROM locateur_client'


# ***************** PROJET_EMPLOYE *********************
# TABLE DE LIAISON
CREER_PROJET_EMPLOYE = '''
CREATE TABLE IF NOT EXISTS projet_employe
(
    id_projet_employe INTEGER PRIMARY KEY AUTOINCREMENT,
    projet INTEGER REFERENCES projet(id_projet),
    employe INTEGER REFERENCES personne(id_personne),
    locateur INTEGER REFERENCES locateur(id_locateur)
)
'''
DROP_PROJET_EMPLOYE = 'DROP TABLE IF EXISTS projet_employe'
# FK
# INSERT_PROJET_EMPLOYE = FOREIGN KEY À FUSIONNER AFIN DE CRÉER UN ITEM
SELECT_PROJET_EMPLOYE = 'SELECT * FROM projet_employe'


# ***************** PROJET_LOCALISATION *********************

CREER_PROJET_LOCALISATION = '''
CREATE TABLE IF NOT EXISTS projet_localisation
(
    id_projet_localisation INTEGER PRIMARY KEY AUTOINCREMENT,
    projet INTEGER REFERENCES projet(id_projet),
    emplacement INTEGER REFERENES adresse(id_adresse),
    local INTEGER REFERENCES local(id_local)
)
'''
DROP_PROJET_LOCALISATION = 'DROP TABLE IF EXISTS projet_localisation'
# FK
# INSERT_PROJET_LOCALISATION = FOREIGN KEY À FUSIONNER AFIN DE CRÉER UN ITEM
SELECT_PROJET_LOCALISATION = 'SELECT * FROM projet_localisation'


# ***************** PROJET_EQUIPEMENT *********************
CREER_PROJET_EQUIPEMENT = '''
CREATE TABLE IF NOT EXISTS projet_equipement
(
    id_projet_equipement INTEGER PRIMARY KEY AUTOINCREMENT,
    projet INTEGER REFERENCES projet(id_projet),
    equipement INTEGER REFERENCES equipement(id_equipement)
)
'''

DROP_PROJET_EQUIPEMENT = 'DROP TABLE IF EXISTS projet_equipement'
# FK
# INSERT_PROJET_EQUIPEMENT = FOREIGN KEY À FUSIONNER AFIN DE CRÉER UN ITEM
SELECT_PROJET_EQUIPEMENT = 'SELECT * FROM projet_equipement'


# ***************** FACTURE_CLIENT *********************
CREER_FACTURE_CLIENT = '''
CREATE TABLE IF NOT EXISTS facture_client
(
    id_facture_client INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    client INTEGER REFERENCES personne(id_personne),
    projet INTEGER REFERENCES projet(id_projet),
    detail TEXT,
    montant REAL,
    statut TEXT  
)
'''
DROP_FACTURE_CLIENT = 'DROP TABLE IF EXISTS facture_client'
# FK
#INSERT_FACTURE_CLIENT = 'INSERT INTO facture_client(client, projet, detail, montant, statut) VALUES(?, ?, ?, ?, ?)'
SELECT_FACTURE_CLIENT = 'SELECT * FROM facture_client'


# TOUS LES FOREIGNS KEYS SERONTS MISE ICI 

# ALTER_PROJET_EQUIPEMENT = '''
#     ALTER TABLE projet_equipement ADD FOREIGN KEY (projet) REFERENCES projet(id)
#     ALTER TABLE projet_equipement ADD FOREIGN KEY (equipement) REFERENCES equipement(id)
#     '''

# ALTER_STATISTIQUE = '''
#     ALTER TABLE statistique ADD FOREIGN KEY (module) REFERENCES module(id)
#     '''

# ALTER_LOCATEUR_EQUIPEMENT = '''
#     ALTER TABLE locateur_equipement ADD FOREIGN KEY (locateur) REFERENCES locateur(id)
#     ALTER TABLE locateur_equipement ADD FOREIGN KEY (equipement) REFERENCES equipement(id)
#     ALTER TABLE locateur_equipement ADD FOREIGN KEY (rangement) REFERENCES rangement(id)
#     '''

# ALTER_PROJET = '''
#     ALTER TABLE projet ADD FOREIGN KEY (locateur) REFERENCES locateur(id)
#     '''

# ALTER_PERSONNE_MODULE = '''
#     ALTER TABLE personne_module ADD FOREIGN KEY (personne) REFERENCES personne(id)
#     ALTER TABLE personne_module ADD FOREIGN KEY (module) REFERENCES module(id)
#     '''

# ALTER_PROJET_LOCALISATION = '''
#     ALTER TABLE projet_localisation ADD FOREIGN KEY (projet) REFERENCES projet(id)
#     ALTER TABLE projet_localisation ADD FOREIGN KEY (emplacement) REFERENCES adresse(id)
#     ALTER TABLE projet_localisation ADD FOREIGN KEY (local) REFERENCES local(id)
# '''

# ALTER_PROJET_EMPLOYE = '''
#     ALTER TABLE projet_employe ADD FOREIGN KEY (projet) REFERENCES projet(id)
#     ALTER TABLE projet_employe ADD FOREIGN KEY (employe) REFERENCES personne(id)
#     ALTER TABLE projet_employe ADD FOREIGN KEY (locateur) REFERENCES locateur(id)
# '''

# ALTER_LOCATEUR = '''
#     ALTER TABLE locateur ADD FOREIGN KEY (admin) REFERENCES personne(id)
#     ALTER TABLE locateur ADD FOREIGN KEY (adresse) REFERENCES adresse(id)
# '''

# ALTER_LOCATEUR_CLIENT = '''
#     ALTER TABLE locateur_client ADD FOREIGN KEY (locateur) REFERENCES locateur(id)
#     ALTER TABLE locateur_client ADD FOREIGN KEY (client) REFERENCES personne(id)
# '''

# ALTER_FACTURE = '''
#     ALTER TABLE facture ADD FOREIGN KEY (client) REFERENCES personne(id)
#     ALTER TABLE facture ADD FOREIGN KEY (projet) REFERENCES projet(id)
# '''

# ALTER_MESSAGE = '''
#     ALTER TABLE message ADD FOREIGN KEY (expediteur) REFERENCES personne(id)
#     ALTER TABLE message ADD FOREIGN KEY (destinataire) REFERENCES destinataire(id)
# '''

# ALTER_EMPLOYE_ROLE = '''
#     ALTER TABLE employe_role ADD FOREIGN KEY (employe) REFERENCES personne(id) 
#     ALTER TABLE employe_role ADD FOREIGN KEY (role) REFERENCES role(id) 
# '''


# mettre à jour cette partie après le ménage des tables
class Dao():
    __creer = [
        CREER_ADRESSE,
        CREER_PERSONNE,
        CREER_MODULE,
        CREER_LOCATEUR,
        CREER_USAGER,
        CREER_EQUIPEMENT,
        CREER_LOCAL,
        CREER_PROJET,
        CREER_FACTURE_LOCATEUR,
        CREER_STATISTIQUE,
        CREER_ROLE,
        CREER_MESSAGE,
        CREER_PERSONNE_MODULE,
        CREER_LOCATEUR_EMPLOYE,
        CREER_EMPLOYE_ROLE,
        CREER_LOCATEUR_EQUIPEMENT,
        CREER_LOCATEUR_CLIENT,
        CREER_PROJET_EMPLOYE,
        CREER_PROJET_LOCALISATION,
        CREER_PROJET_EQUIPEMENT,
        CREER_FACTURE_CLIENT
    ]
    __detruire = [
        CREER_FACTURE_CLIENT,
        CREER_PROJET_EQUIPEMENT,
        CREER_PROJET_LOCALISATION,
        CREER_PROJET_EMPLOYE,
        CREER_LOCATEUR_CLIENT,
        CREER_LOCATEUR_EQUIPEMENT,
        CREER_EMPLOYE_ROLE,
        CREER_LOCATEUR_EMPLOYE,
        CREER_PERSONNE_MODULE,
        CREER_MESSAGE,
        CREER_ROLE,
        CREER_STATISTIQUE,
        CREER_FACTURE_LOCATEUR,
        CREER_PROJET,
        CREER_LOCAL,
        CREER_EQUIPEMENT,
        CREER_USAGER,
        CREER_LOCATEUR,
        CREER_MODULE,
        CREER_PERSONNE,
        CREER_ADRESSE,        
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
