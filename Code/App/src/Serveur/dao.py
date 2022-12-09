import sqlite3

FK_ON = 'PRAGMA foreign_keys = 1'

#BD_GEST_MEDIA = 'C:\\travail\\C51_equipe3_VM\\Code\\App\\src\\Serveur\\gestion_media.db'
BD_GEST_MEDIA = 'gestion_media.db'


# ***************** ADRESSE *********************
# Table Adresse à enlever
# CREER_ADRESSE = '''
# CREATE TABLE IF NOT EXISTS adresse
# (
#     id_adresse INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     rue TEXT,
#     numero INTEGER,
#     appartement TEXT,
#     ville TEXT,
#     province_etat TEXT,
#     pays TEXT,
#     code_postal TEXT
# )
# '''
# DROP_ADRESSE = 'DROP TABLE IF EXISTS adresse'
# INSERT_ADRESSE = 'INSERT INTO adresse(rue, numero, appartement, ville, province_etat, pays, code_postal) VALUES(?, ?, ?, ?, ?, ?, ?)'
# SELECT_ADRESSE = 'SELECT * FROM ADRESSE'


# ***************** PERSONNE *********************
CREER_PERSONNE = '''
CREATE TABLE IF NOT EXISTS personne
(
    id_personne INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    courriel TEXT UNIQUE NOT NULL,
    telephone TEXT,
    adresse TEXT

)
'''
# ('adresse', (SELECT id_adresse from adresse WHERE rue=? AND numero=? AND appartement=? AND code_postal=?)))''' 
DROP_PERSONNE = 'DROP TABLE IF EXISTS personne'
INSERT_PERSONNE = '''INSERT INTO personne(nom, prenom, courriel, telephone, adresse) VALUES(?, ?, ?, ?, ?)'''
SELECT_PERSONNE = 'SELECT * FROM personne'
SELECT_PERSONNE_COURRIEL = 'SELECT * FROM personne WHERE courriel = ?'


# ***************** MODULE *********************
CREER_MODULE = '''
CREATE TABLE IF NOT EXISTS module
(
    id_module INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT UNIQUE NOT NULL,
    num_version INTEGER,
    prix_jour REAL
)
'''
DROP_MODULE = 'DROP TABLE IF EXISTS module'
INSERT_MODULE = 'INSERT INTO module(nom, num_version, prix_jour) VALUES(?, ?, ?)'
SELECT_MODULE = 'SELECT * FROM module'


# ***************** LOCATEUR *********************
CREER_LOCATEUR = '''
CREATE TABLE IF NOT EXISTS locateur
(
    id_locateur INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom_compagnie TEXT UNIQUE NOT NULL,
    telephone TEXT,
    adresse TEXT
)
'''
#('adresse', (SELECT id_adresse from adresse WHERE rue=? AND numero=? AND appartment=? AND code_postal=?)))'''
DROP_LOCATEUR = 'DROP TABLE IF EXISTS locateur'
INSERT_LOCATEUR = '''INSERT INTO locateur(nom_compagnie, telephone, adresse) VALUES(?, ?, ?)'''
SELECT_LOCATEUR = 'SELECT * FROM locateur'

# ***************** USAGER *********************
# revoir si l'identifiant ne peut pas être le courriel de personne et si oui pourquoi le mettre 
# dans la table la FK personne peut nous le donner
# peut-être récupérer le email et strip la partie @....

CREER_USAGER = '''
CREATE TABLE IF NOT EXISTS usager
(
    id_usager INTEGER PRIMARY KEY AUTOINCREMENT,
    personne INTEGER NOT NULL REFERENCES personne(id_personne),
    locateur INTEGER NOT NULL REFERENCES locateur(id_locateur),
    identifiant TEXT UNIQUE NOT NULL, 
    mdp TEXT NOT NULL,
    permission TEXT NOT NULL
)
'''


DROP_USAGER = 'DROP TABLE IF EXISTS usager'
INSERT_USAGER = '''INSERT INTO usager (personne, locateur, identifiant, mdp, permission) VALUES
	    ( ((SELECT id_personne from personne WHERE courriel = ?)),
	      ((SELECT id_locateur from locateur WHERE nom_compagnie = ?)),? , ?, ?)'''

SELECT_USAGER = 'SELECT * FROM usager'


# ***************** EQUIPEMENT *********************
# Utilistation du type d'equipement et du modele d'equipment 
CREER_EQUIPEMENT = '''
CREATE TABLE IF NOT EXISTS equipement
(
    id_equipement INTEGER PRIMARY KEY AUTOINCREMENT,
    type_equipement TEXT,
    modele_equipement TEXT,
    marque TEXT
)
'''
DROP_EQUIPEMENT = 'DROP TABLE IF EXISTS equipement'
INSERT_EQUIPEMENT = 'INSERT INTO equipement(type_equipement ,modele_equipement,marque) VALUES (?,?,?)'
SELECT_EQUIPEMENT = 'SELECT * FROM equipement'


# ***************** LOCAL *********************
CREER_LOCAL = '''
CREATE TABLE IF NOT EXISTS local
(
    id_local INTEGER PRIMARY KEY AUTOINCREMENT,
    adresse TEXT,
    no_local INTEGER
)
'''
# FOREIGN KEY A ajouter (adresse)
#('adresse', (SELECT id_adresse from adresse WHERE rue=? AND numero=? AND appartment=? AND code_postal=?),?)'''
DROP_LOCAL = 'DROP TABLE IF EXISTS local'
INSERT_LOCAL = '''INSERT INTO local (adresse,no_local) VALUES (?,?)'''
SELECT_LOCAL = 'SELECT * FROM LOCAL'


# ***************** PROJET *********************

CREER_PROJET = '''
CREATE TABLE IF NOT EXISTS projet
(
    id_projet INTEGER PRIMARY KEY AUTOINCREMENT,
    locateur INTEGER REFERENCES locateur(id_locateur),
    debut NUMERIC,
    fin NUMERIC,
    nom_projet TEXT
)
'''
# 1 FOREIGN KEY À METTRE (locateur)
DROP_PROJET = 'DROP TABLE IF EXISTS projet'
INSERT_PROJET = '''INSERT INTO projet(locateur,debut, fin,nom_projet) VALUES
    ('locateur', (SELECT id_locateur from locateur WHERE nom_compagnie=?)), ?, ?, ?)'''
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
INSERT_FACTURE_LOCATEUR = '''INSERT INTO facture_locateur(locateur, detail, montant, statut) VALUES
    ('locateur', (SELECT id_locateur from locateur WHERE nom_compagnie=?)), ?, ?, ?)'''
SELECT_FACTURE_LOCATEUR = 'SELECT * FROM facture_locateur'


# ***************** STATISTIQUE *********************
CREER_STATISTIQUE = '''
CREATE TABLE IF NOT EXISTS statistique
(
    id_statistique INTEGER PRIMARY KEY AUTOINCREMENT,
    module INTEGER REFERENCES module(id_module),
    nb_utilistateur INTEGER
)
'''

DROP_STATISTIQUE = 'DROP TABLE IF EXISTS statistique'
INSERT_STATISTIQUE = '''INSERT INTO statistique(module,nb_utilisateur) VALUES 
    ('module', (SELECT id_module from module WHERE nom = ?)),?)'''
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
INSERT_MESSAGE = '''INSERT INTO message(contenu, expediteur, destinataire) VALUES
    (?, 
    ('expediteur',(SELECT id_personne from personne WHERE courriel=?),
    ('destinataire',(SELECT id_personne from personne WHERE courriel=?))'''
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
INSERT_PERSONNE_MODULE = '''INSERT INTO personne_module(personne, module) VALUES
    ('personne',(SELECT id_personne from personne WHERE courriel=?),
    ('module',(SELECT id_module from module WHERE nom=?))'''
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
INSERT_LOCATEUR_EMPLOYE = '''INSERT INTO locateur_employe(locateur, employe, salaire) VALUES
    ('locateur',(SELECT id_locateur FROM locateur WHERE nom_compagnie = ?),
    ('employe',(SELECT id_personne FROM personne WHERE courriel = ?)),
    ?)'''
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
INSERT_EMPLOYE_ROLE = '''INSERT INTO employe_role(employe, role) VALUES
    ('employe',(SELECT id_personne FROM personne WHERE courriel = ?)),
    ?)'''
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
INSERT_LOCATEUR_EQUIPEMENT = '''INSERT INTO locateur_equipement(locateur, equipement, rangement, no_serie, date_achat, valeur_achat, valeur_location) VALUES
    ('locateur',(SELECT id_locateur FROM locateur WHERE nom_compagnie = ?),
    ('equipement',(SELECT id_equipement FROM equipement WHERE modele_equipement = ? AND marque = ?),
    ('rangement',(SELECT id_local FROM local WHERE no_local =  ?))'''
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
INSERT_LOCATEUR_CLIENT = '''INSERT INTO locateur_client(locateur, client) VALUES
    ((SELECT id_locateur FROM locateur WHERE id_locateur = ?),
    (SELECT id_personne FROM personne WHERE id_personne = ?))'''
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
INSERT_PROJET_EMPLOYE = '''INSERT INTO projet_employe(projet,employe,locateur) VALUES
    ('projet', (SELECT id_projet FROM projet WHERE nom_projet = ?),
    ('employe', (SELECT id_personne FROM personne WHERE courriel = ?),
    ('locateur', (SELECT id_locateur FROM locateur WHERE nom_compagnie = ?))'''
SELECT_PROJET_EMPLOYE = 'SELECT * FROM projet_employe'


# ***************** PROJET_LOCALISATION *********************

CREER_PROJET_LOCALISATION = '''
CREATE TABLE IF NOT EXISTS projet_localisation
(
    id_projet_localisation INTEGER PRIMARY KEY AUTOINCREMENT,
    projet INTEGER REFERENCES projet(id_projet),
    emplacement TEXT,
    local INTEGER REFERENCES local(id_local)
)
'''
 # ('emplacement', (SELECT id_adresse FROM adresse WHERE rue=? AND numero=? AND appartement=? AND code_postal=?),
DROP_PROJET_LOCALISATION = 'DROP TABLE IF EXISTS projet_localisation'
INSERT_PROJET_LOCALISATION = '''INSERT INTO projet_localisation(projet,emplacement,local) VALUES
    ('projet', (SELECT id_projet FROM projet WHERE nom_projet = ?),?,('local', (SELECT id_local FROM local WHERE no_local = ?))'''
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
INSERT_PROJET_EQUIPEMENT = '''INSERT INTO projet_equipement(projet,equipement) VALUES 
    ('projet', (SELECT id_projet FROM projet WHERE nom_projet = ?),
    ('equipement', (SELECT id_equipement FROM equipement WHERE modele_equipement = ? AND marque = ?))'''
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
INSERT_FACTURE_CLIENT = '''INSERT INTO facture_client(client, projet, detail, montant, statut) VALUES
    ('client', (SELECT id_personne FROM personne WHERE courriel = ?),
    ('projet', (SELECT id_projet FROM projet WHERE nom_projet = ?), ?, ?, ?))'''
SELECT_FACTURE_CLIENT = 'SELECT * FROM facture_client'

class Dao():
    __creer = [
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
        DROP_FACTURE_CLIENT,
        DROP_PROJET_EQUIPEMENT,
        DROP_PROJET_LOCALISATION,
        DROP_PROJET_EMPLOYE,
        DROP_LOCATEUR_CLIENT,
        DROP_LOCATEUR_EQUIPEMENT,
        DROP_EMPLOYE_ROLE,
        DROP_LOCATEUR_EMPLOYE,
        DROP_PERSONNE_MODULE,
        DROP_MESSAGE,
        DROP_ROLE,
        DROP_STATISTIQUE,
        DROP_FACTURE_LOCATEUR,
        DROP_PROJET,
        DROP_LOCAL,
        DROP_EQUIPEMENT,
        DROP_USAGER,
        DROP_LOCATEUR,
        DROP_MODULE,
        DROP_PERSONNE
    ]
    
    
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


    def identifier_usager(self, identifiant, mdp):
        sql = '''
            SELECT
                usager.identifiant,
                usager.locateur,
                usager.personne,
                usager.permission
            FROM usager
            WHERE usager.identifiant = ? AND usager.mdp = ?  
        '''
        self.cur.execute(sql, (identifiant, mdp))
        return self.cur.fetchall()
    
    def trouver_personne(self,courriel):
        sql = '''
            SELECT
                personne.courriel
            FROM personne
            WHERE personne.courriel = ?
        '''
        self.cur.execute(sql,(courriel,))
        return self.cur.fetchall()
        
    def creer_personne(self,nom,prenom,courriel,telephone,adresse): #employe ou clients
        
        sql = INSERT_PERSONNE
        # adresse à voir
        self.cur.execute(sql,(nom,prenom,courriel,telephone,adresse))
        self.conn.commit()
     
    def trouver_locateur(self, nom_compagnie):
        sql = '''
            SELECT
                locateur.nom_compagnie
            FROM locateur
            WHERE locateur.nom_compagnie = ?
        ''' 
        self.cur.execute(sql,(nom_compagnie,))
        return self.cur.fetchall()

    
    def creer_locateur(self,nom_compagnie,telephone_compagnie,adresse):
        sql = INSERT_LOCATEUR
        self.cur.execute(sql,(nom_compagnie,telephone_compagnie,adresse))
        self.conn.commit()
    
    def enregistrer_usager(self, personne_email, locateur_nom_compagnie, identifiant, mdp, permission):
        sql = INSERT_USAGER
        self.cur.execute(sql, (personne_email, locateur_nom_compagnie, identifiant, mdp, permission))
        self.conn.commit()

        
    def select_usager(self):
        sql = SELECT_USAGER
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def select_personne(self):
        sql = SELECT_PERSONNE
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def select_locateur(self):
        sql = SELECT_LOCATEUR
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    
    
    def get_personne_info(self, personne): #clients ou employee
        sql = ''' SELECT * FROM personne WHERE personne.id_personne = ? '''
        self.cur.execute(sql, (personne,))
        return self.cur.fetchall() 

    def get_personne_courriel(self, courriel): #clients ou employee
        sql = ''' SELECT * FROM personne WHERE personne.courriel = ? '''
        self.cur.execute(sql, (courriel,))
        return self.cur.fetchall() 

    
    def get_employee(self, locateur):
        sql = ''' SELECT personne, identifiant FROM usager WHERE usager.locateur = ? '''
        self.cur.execute(sql, (locateur,))
        return self.cur.fetchall()
    
    def creer_client(self,locateur,client):
        sql = INSERT_LOCATEUR_CLIENT
        self.cur.execute(sql, (locateur,client))
        self.conn.commit()
        

    def get_client(self, locateur):
        sql = ''' SELECT client FROM locateur_client WHERE locateur_client.locateur = ? '''
        self.cur.execute(sql, (locateur,))
        return self.cur.fetchall() 
    
    def get_utilisateur(self, identifiant): 
        sql = ''' SELECT * FROM usager WHERE usager.identifiant = ? '''
        self.cur.execute(sql, (identifiant,))
        return self.cur.fetchall()
    
        
    def get_locateur(self, id): 
        sql = ''' SELECT * FROM locateur WHERE locateur.id_locateur = ? '''
        self.cur.execute(sql, (id,))
        return self.cur.fetchall()
    
 

        

def main():
    Dao().creer_bd()
    return 0



if __name__ == '__main__':
    quit(main())


