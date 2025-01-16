class Product:

    def __init__(self,  name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        current_products = self.get_products().split('\n')
        current_product_names = {line.split(', ')[0] for line in current_products if line}
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if product.name not in current_product_names:
                    file.write(str(product) + '\n')
                    current_product_names.add(product.name)
                else:
                    print(f'Продукт {product} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
