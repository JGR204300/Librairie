MENU_OPTIONS = {
    1: 'Ajouter un livre',
    2: 'Retirer un livre',
    3: 'Afficher les livres',
    4: 'Afficher le nombre de livre',
    5: 'Modifier le prix d\'un livre',
    6: 'Modifier la quantité d\'un livre',
    7: 'Quitter'
}


def add_book():
    '''Ajout d'un nouveau titre'''
    global library
    new_library = library
    print('Saisir les paramètres du nouveau livre')
        # Saisi du nouveau titre
    new_title = input('Titre: ') 
        # Saisi du nouveau prix                                             
    while True:
        try:
            new_price = round(float(input('Prix: ')),2)                                     
            if 0 <= new_price:
                break
            else:
                print('Sairsir un prix superieur ou égal à zéro')
        except:
            print('Sairsir un prix superieur ou égal à zéro')

        # Saisi de la nouvelle quantité
    while True:
        try:
            new_qty = int(input('Quantité: '))                                       
            if 0 <= new_qty:
                break
            else:
                print('Sairsir un entier superieur ou égal à zéro')
        except:
            print('Sairsir un entier superieur ou égal à zéro')

    new_book = {'title': new_title, 'price': new_price, 'quantity': new_qty}
        # Ajout du nouveau livre
    new_library.append(new_book)  
        # tri des titres par odre alphabétique                                               
    library = sorted(new_library, key=lambda i: i['title'])
        # Affichage du nouveau livre
    print('Noveau livre ajouté')
    print('Titre:',new_book["title"],' Prix:',"%.2f" % new_book["price"],'€  Qté:',new_book["quantity"],'\n')


def remove_book():
    '''Suppression d'un livre'''
    search_book(input('Saisir le titre du livre à supprimer: '))
    print('Voulez-vous supprimer le livre',library[book_position]["title"],'de la librairie ? OUI:y / NON:n')
    valid = input()
    if valid == 'y':
        del library[book_position]
        print('Suppression terminée!\n')
    else:
        print('Suppression annulée!\n')
    

def show_books():
    '''Affichage de tous les titres de la librairie'''
    for book in library:
        print('Titre:',book["title"],' Prix:',"%.2f" % book["price"],'€  Qté:',book["quantity"])
    print('\n')

def show_nb_books():
    '''Affichage du nombre de titre de la librairie et du nombre total de livre'''
    print('Nombre de titre de la librairie: ',len(library))
    sum=0
    for book in library:
        sum += int(book["quantity"])
    print('Nombre total de livres:',sum,'\n')


def update(field):
    '''Modification du prix ou de la quantité d'un livre'''
    search_book(input('Saisir le titre du livre à modifier: '))
        # Modification du prix du livre
    if field == "price":
        print('Le prix actuel du livre est de',"%.2f" % library[book_position]["price"],'€')
        while True:
            try:
                library[book_position]["price"] = round(float(input('Saisir le nouveau prix: ')),2)
                if 0 <= library[book_position]["price"]:
                    break
                else:
                    print('Sairsir un prix superieur ou égal à zéro')
            except:
                print('Sairsir un prix superieur ou égal à zéro')

        # Modification de la quantité de livre           
    else:
        print('La quantité actuelle du livre est de',library[book_position]["quantity"])
        while True:
            try:
                library[book_position]["quantity"] = int(input('Saisir la nouvelle quantité: '))
                if 0 <= library[book_position]["quantity"]:
                    break
                else:
                    print('Sairsir un entier superieur ou égal à zéro')
            except:
                print('Sairsir un entier superieur ou égal à zéro')
    print('Modification terimnée')
    print('Titre:',library[book_position]["title"],' Prix:',"%.2f" % library[book_position]["price"],'€  Qté:',library[book_position]["quantity"],'\n')


def search_book(select_title):
    '''Recherche d'un titre dans la librairie'''
    global book_position
    book_indexer = dict((p['title'], i) for i, p in enumerate(library))
    book_position = book_indexer.get(select_title, -1)
    if book_position == -1:
        print('Titre non trouvé!\n')
        start()


def run_option(option):
    try:    
       print(f"{MENU_OPTIONS[option]}")
       match option:
         case 1:
             add_book()
         case 2:
             remove_book()
         case 3:
             show_books()
         case 4:
             show_nb_books()
         case 5:
             update(field="price")
         case 6:
             update(field="quantity")
         case 7:
             exit()
    except KeyError:
        print('Merci de saisir un nombre entre 1 et 7')
        start()

# Le tableau il faudra ajouter vos livres, ça sera un tableau de dictionnaire
library = []
book = {"title": "Les misérables", "price": 10.00, "quantity": 10}
library.append(book)  # Ajout d'un premier livre


def start():
    while(True):
        show_options()
        try:
            run_option(int(input('Merci de saisir une option: ')))
        except ValueError:
            print('Merci de saisir un nombre entre 1 et 7')
            start()   
        


def show_options():
    print('Bienvenue dans l\'application de gestion de librairie')
    # Compléter la fonction en faisant une boucle for sur MENU_OPTIONS
    for key in range(1, 8):
        print(f'[{key}] - ',MENU_OPTIONS[key])  # A remplacer


start()