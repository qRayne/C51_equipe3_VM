from asyncio.windows_events import NULL
from dao import Dao


def initial(dao): #hard codes des valeurs de base dans le DAO

   
    dao.creer_locateur('Bell', '345-345-1234', 'a')   
    dao.creer_locateur('Videotron', '345-145-3456', 'b')   
    dao.creer_locateur('Fido', '345-536-6234', 'c')   
    dao.creer_locateur('Telus', '345-414-1582', 'd')   
    dao.creer_locateur('koodo', '345-346-3976', 'e')   
    

   
    if not dao.trouver_personne('boubou@gmail.com'):
       dao.creer_personne('boubou', 'babou', 'boubou@gmail.com', '123-1234-1234', '220 rue robert-cliche')
    
    dao.enregistrer_usager('boubou@gmail.com', 'Bell', 'root', 'root', 'admin')
       
         
    if not dao.trouver_personne('boul.com'):
           dao.creer_personne('bou', 'bou', 'boul.com', '123-1234', '220 rert-cliche')
   
    dao.enregistrer_usager('boul.com', 'Bell', 'bou', '145', 'user')
            
    
            
    
def insert_usager(dao, nom, prenom, email, numTel, adresse, locateur, mdp, access):
    # problème binding 
    #Dao().select_locateur
    
    if not dao.trouver_personne(email):
        dao.creer_personne(nom, prenom, email, numTel, adresse)
    
    dao.enregistrer_usager(email, locateur, nom, mdp, access)
       
    
def select(dao):
 
    c = dao.select_personne()
    print(c)
    l = dao.select_locateur()
    print(l)
    usage = dao.select_usager()
    print(usage)
    
    


def main():
    bd = Dao()
    initial(bd)
    insert_usager(bd, 'bricoleur', 'bob', 'bob@gmail.com', '256-254-2478', 'rue construction', 'Bell', '68223', 'admin')
    insert_usager(bd, 'bricoleur', 'roger', 'roger@gmail.com', '256-254-2478', 'rue construction', 'Bell', '68223', 'admin')
    insert_usager(bd, 'bricoleur', 'alice', 'alice@gmail.com', '256-254-2478', 'rue construction', 'Bell', '68223', 'admin')
    insert_usager(bd, 'bricoleur', 'fune', 'fune@gmail.com', '256-254-2478', 'rue construction', 'Bell', '68223', 'admin')
    select(bd)

    print('\nIdentifier l\'usager')
    print(bd.identifier_usager('boubou', '12345'))
    
    bd.creer_personne('client','client','client','514-4109','client')
    
    bd.creer_client(1,4)
    
    print(bd.get_client(1))
    
    print(bd.get_employee(1))
    print(bd.get_personne_info(1))
    print(bd.get_client(1))

    return 0

#print('Dans le module tester_table: ', __name__)
if __name__ == '__main__':
    quit(main())