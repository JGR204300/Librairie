import service.modif as modif


def search_book(select_title):
    '''Recherche d'un titre dans la librairie'''
    book_indexer = dict((p['title'], i) for i, p in enumerate(library))
    book_position = book_indexer.get(select_title, -1)
    if book_position == -1:
        print('Titre non trouvé!\n')
    return book_position


def add_book():
    '''Ajout d'un nouveau titre'''
    global library
    new_library = library
    print('Saisir les paramètres du nouveau livre')
    # Saisi du nouveau titre
    is_title_duplicated = True
    while is_title_duplicated:
        new_title = input('Titre: ')
        is_title_duplicated = bool([book for book in new_library if new_title.lower() == book["title"].lower()])
        if is_title_duplicated:
            print("Titre déja présent")

    # Saisi du nouveau prix
    new_price = modif.price()

    # Saisi de la nouvelle quantité
    new_qty = modif.qty()

    # Ajout du nouveau livre
    new_book = {'title': new_title, 'price': new_price, 'quantity': new_qty}
    new_library.append(new_book)

    # tri des titres par odre alphabétique
    library = sorted(new_library, key=lambda i: i['title'])

    # Affichage du nouveau livre
    print('Noveau livre ajouté')
    book_title = new_book["title"]
    book_price = "%.2f" % new_book["price"] + '€'
    book_qty = new_book["quantity"]
    print('Titre:', book_title, ' Prix:', book_price, '  Qté:', book_qty, '\n')


def remove_book():
    '''Suppression d'un livre'''
    book_position = search_book(input('Saisir le titre du livre à supprimer: '))
    if book_position != -1:
        print('Voulez-vous supprimer le livre')
        print(library[book_position]["title"], 'de la librairie ?')
        print('OUI:y / NON:n')
        valid = input()
        if valid == 'y':
            del library[book_position]
            print('Suppression terminée!\n')
        else:
            print('Suppression annulée!\n')


def show_books():
    '''Affichage de tous les titres de la librairie'''
    for book in library:
        book_title = book["title"]
        book_price = "%.2f" % book["price"] + '€'
        book_qty = book["quantity"]
        print('Titre:', book_title, ' Prix:', book_price, 'Qté:', book_qty)
    print('\n')


def show_nb_books():
    '''Affichage du nombre de titre de la librairie
    et du nombre total de livre'''
    print('Nombre de titre de la librairie: ', len(library))
    sum = 0
    for book in library:
        sum += int(book["quantity"])
    print('Nombre total de livres:', sum, '\n')


def update(field):
    '''Modification du prix ou de la quantité d'un livre'''
    book_position = search_book(input('Saisir le titre du livre à modifier: '))
    if book_position != -1:
        # Modification du prix du livre
        if field == "price":
            # Affichage du prix avant modification
            book_price = "%.2f" % library[book_position]["price"] + '€'
            print('Le prix actuel du livre est de', book_price)
            # Saisi du nouveau prix
            library[book_position]["price"] = modif.price()

        # Modification de la quantité de livre
        else:
            # Affichage de la quantité avant modification
            book_qty = library[book_position]["quantity"]
            print('La quantité actuelle du livre est de', book_qty)
            # Saisi de la nouvelle quantité
            library[book_position]["quantity"] = modif.qty()

        print('Modification terimnée')
        book_title = library[book_position]["title"]
        book_price = "%.2f" % library[book_position]["price"] + '€'
        book_qty = library[book_position]["quantity"]
        print('Titre:', book_title, ' Prix:', book_price, '  Qté:', book_qty, '\n')
