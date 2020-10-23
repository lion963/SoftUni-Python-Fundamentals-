class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        list_by_letter = [product for product in self.products if product.find(first_letter) == 0]
        return list_by_letter

    def __repr__(self):
        self.products.sort()
        return ''.join('Items in the {} catalogue: \n'.format(self.name)) + '\n'.join(product for product in self.products)


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
