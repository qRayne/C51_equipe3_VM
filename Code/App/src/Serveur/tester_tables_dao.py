from asyncio.windows_events import NULL
from dao import Dao

def insert(dao):
    # problème binding 
    #Dao().select_locateur
    
    if not dao.trouver_personne('boubou@gmail.com'):
        dao.creer_personne('boubou', 'babou', 'boubou@gmail.com', '123-1234-1234', '220 rue robert-cliche')
    
    if not dao.trouver_locateur('Bell'):
        dao.creer_locateur('Bell', '345-3456-3456', '')     
    
    dao.enregistrer_usager('boubou@gmail.com', 'Bell', 'boubou', '12345', 'admin')
        
        
    if not dao.trouver_personne('boul.com'):
            dao.creer_personne('bou', 'bou', 'boul.com', '123-1234', '220 rert-cliche')
    
    if not dao.trouver_locateur('Bell'):
        dao.creer_locateur('Bell', '345-3456-3456', '')     
    
    dao.enregistrer_usager('boul.com', 'Bell', 'bou', '145', 'admin')
            
    
    # dao.insert_compagnie('Totologie')
    # dao.insert_compagnie('Tatalogie')
    # dao.insert_membre(2, 'toto', 'totototo', 'admin', 'mr')
    # dao.insert_membre(1, 'tata', 'tatatata', 'user', 'mrs')

def select(dao):
    # print('\nCompagnie')
    # for rangee in dao.select_compagnie():
    #     print(rangee)
        
    # print('\nMembre')
    # for rangee in dao.select_membre():
    #     print(rangee)
    
 
    c = dao.select_personne()
    print(c)
    l = dao.select_locateur()
    print(l)
    usage = dao.select_usager()
    print(usage)
    


def main():
    bd = Dao()
    insert(bd)
    select(bd)

    # print('\nIdentifier l\'usager')
    # print(bd.identifier_usager('toto', 'totototo'))

    return 0

#print('Dans le module tester_table: ', __name__)
if __name__ == '__main__':
    quit(main())