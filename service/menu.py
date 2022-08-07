from service.book import add_book, remove_book, show_books, show_nb_books, update


MENU_OPTIONS = {
    1: 'Ajouter un livre',
    2: 'Retirer un livre',
    3: 'Afficher les livres',
    4: 'Afficher le nombre de livre',
    5: 'Modifier le prix d\'un livre',
    6: 'Modifier la quantité d\'un livre',
    7: 'Quitter'
}


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
        print('Merci de saisir un nombre entre 1 et 7\n')


def show_options():
    print('Bienvenue dans l\'application de gestion de librairie')
    # Compléter la fonction en faisant une boucle for sur MENU_OPTIONS
    for key in range(1, 8):
        print(f'[{key}] - ', MENU_OPTIONS[key])
