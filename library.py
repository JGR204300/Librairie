import service.menu
from service.book import save_book


# Le tableau il faudra ajouter vos livres, ça sera un tableau de dictionnaire
service.book.library = []
# book = {"title": "Les misérables", "price": 10.00, "quantity": 10}
# service.book.library.append(book)  # Ajout d'un premier livre


def start():
    service.menu.load_book()
    while (True):
        service.menu.show_options()
        try:
            service.menu.run_option(int(input('Merci de saisir une option: ')))
        except ValueError:
            print('Merci de saisir un nombre entre 1 et 7\n')


try:
    start()
except KeyboardInterrupt:
    save_book()
    exit()
