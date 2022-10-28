from dao import Dao

def insert(dao):
    # problème binding 
    
    if not Dao().trouver_personne('boubou@gmail.com'):
        Dao().creer_personne('boubou', 'babou', 'boubou@gmail.com', '123-1234-1234', '')
    if not Dao().trouver_locateur('Bell'):
        Dao().creer_locateur('Bell', '345-3456-3456', '')
    
    Dao().enregistrer_usager('boubou@gmail.com', 'Bell', 'boubouuuu', '12345', 'admin')
    # dao.insert_compagnie('Totologie')
    # dao.insert_compagnie('Tatalogie')

    # dao.insert_membre(2, 'toto', 'totototo', 'admin', 'mr')
    # dao.insert_membre(1, 'tata', 'tatatata', 'user', 'mrs')

def select(dao):
    print('\nCompagnie')
    for rangee in dao.select_compagnie():
        print(rangee)
        
    print('\nMembre')
    for rangee in dao.select_membre():
        print(rangee)


def main():
    bd = Dao()
    insert(bd)
    # select(bd)

    # print('\nIdentifier l\'usager')
    # print(bd.identifier_usager('toto', 'totototo'))

    return 0

#print('Dans le module tester_table: ', __name__)
if __name__ == '__main__':
    quit(main())