def price():
    while True:
        try:
            new_price = round(float(input('Prix: ')), 2)
            if 0 <= new_price:
                return new_price
                break
            else:
                print('Sairsir un prix superieur ou égal à zéro')
        except ValueError:
            print('Sairsir un prix superieur ou égal à zéro')


def qty():
    while True:
        try:
            new_qty = int(input('Quantité: '))
            if 0 <= new_qty:
                return new_qty
                break
            else:
                print('Sairsir un entier superieur ou égal à zéro')
        except ValueError:
            print('Sairsir un entier superieur ou égal à zéro')
