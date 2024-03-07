# Establecemos el directorio de trabajo
import os
os.chdir(r"C:/VASS/Python/python-env")

import pandas as pd
# import xlrd as xls

print("Current directory:" , os.getcwd())

class Iterator:

    def __init__(self, objects_to_iteract):
        self.object_to_iteract = objects_to_iteract
        self.last_object = (len(self.object_to_iteract) - 1)
    def __iter__(self):
        self.n = 0
        return self

    def get_object_num(self, n):
        return self.object_to_iteract[n]
    
    def __next__(self):
        if self.n < self.last_object:
            output = self.get_object_num(self.n)
            self.n += 1
            return output
        elif self.n == self.last_object:
            output = self.get_object_num(self.n)
            self.n = 0
            return output
        

   
class Generator:
    
    def __init__(self, objects_to_iteract):
        self.object_to_iteract = objects_to_iteract


    def generate(self):
        last_object = len(self.object_to_iteract)

        # lineup_max = len(self.players)
        idx = 0

        while True:
            if idx < last_object:
                yield self.object_to_iteract[idx]
            else:
                idx = 0
                yield self.object_to_iteract[idx]

            idx += 1

    def __repr__(self):
        return f'generate({self.object_to_iteract})'

    def __str__(self):
        return f"Generator with the object: {', '.join(self.object_to_iteract)}"


class User:

    def __init__(self, user_name, user_login):
        self.user_name = user_name
        self.user_login = user_login
        if self.user_name == '' and self.user_login == '':
            return True
        else:
            return False

class FilesDataSelector:

    def __init__(self, file_path, file_id, returned_id = None , file_conditions = None):
        self.file_path = file_path
        self.file_id = file_id
        self.file_conditions = file_conditions
        if returned_id == None:
            self.returned_id = file_id
        else:
            self.returned_id = returned_id

        

    def show_data(self):
        raise NotImplementedError("Subclass must implement show_data method")

class Shops(FilesDataSelector):

    def show_data(self):
        datafr_main = pd.read_csv(self.file_path)
        datafr = datafr_main
        if self.file_conditions != None:
            datafr = datafr_main[datafr_main[self.file_id] == self.file_conditions]
        datafr_main = None
        print(datafr)
        datafr_number = int(input('Selecciona una Tienda: '))
        datafr_reference = datafr[self.returned_id][datafr_number]
        self.selected_item = datafr[int(datafr_number):int(datafr_number)+1]
        return datafr_reference

class Articles(FilesDataSelector):

    def show_data(self):
        datafr_main = pd.read_csv(self.file_path)
        datafr = datafr_main
        if self.file_conditions != None:
            datafr = datafr_main[datafr_main[self.file_id] == self.file_conditions]
        datafr_main = None
        print(datafr)
        datafr_number = int(input('Selecciona un artículo: '))
        datafr_reference = datafr[self.returned_id][datafr_number]
        self.selected_item = datafr[int(datafr_number):int(datafr_number)+1]
        return datafr_reference
    
class ArticlesCompare(FilesDataSelector):

    def show_data(self):
        datafr_main = pd.read_csv(self.file_path)
        datafr = datafr_main
        if self.file_conditions != None:
            datafr = datafr_main[datafr_main[self.file_id] == self.file_conditions]
        datafr_main = None
        print(datafr)
        # datafr_number = input('Selecciona un valor: ')
        # datafr_reference = datafr[self.returned_id][datafr_number]
        self.selected_item = datafr
        return True
       
class BookShops:

    def __init__(self):
        # 1. Cargar los datos 
        path_root = 'C:/VASS/Python/python-env'
        df_book_shops = pd.read_csv(f'{path_root}/books_shops.csv')
        self.df_book_shops = df_book_shops
        print(df_book_shops)
        # Para crear una nueva variable
        shop_number = int(input('Introduce la librería en la que deseas consultar: '))
        # print(df_book_shops[int(shop_number):int(shop_number)+1])
        shop_reference = df_book_shops['shop_id'][shop_number]
        self.__selected_shop__ = df_book_shops[int(shop_number):int(shop_number)+1]
        
        shop_to_open = f'{path_root}/books_in_shops.csv'
        # shop_to_open = f'{path_root}/{str(shop_reference)}.csv'
        # print(shop_reference)
        # print(shop_to_open)
        df_books_in_shops = pd.read_csv(shop_to_open, sep=',', encoding="utf-8")
        df_books_in_shop = df_books_in_shops[df_books_in_shops['shop_id'] == shop_reference]
        # df_books = df_books_in_shop.sort_index()
        print(df_books_in_shop)
        # Hay qye hacer un reorder desde uno de las claves,,..
        book_number = int(input('Introduce el libro que quires comprar: '))
        
        book_reference = df_books_in_shops['book_id'][book_number]
        
        # self.__selected_book__ = book_reference
        self.__selected_book__ = df_books_in_shops[int(book_number):int(book_number)+1]
        print(self.__selected_book__)

        books_refence_all = df_books_in_shops[df_books_in_shops['book_id'] == book_reference]
        print(books_refence_all)
    
    def get_select_book_shop(self):
        return self.__selected_shop__

    def get_select_book(self):
        return self.__selected_book__

# class Invoice:
#     def __init__(self, *args, **kwargs):



# class Datawarehouse:
#     def __init__(self):



#  ------------------------------------
# desde aquí ejecución del programa
#  ------------------------------------
# Con herencia
    
path_root = 'C:/VASS/Python/python-env'
full_path = f'{path_root}/books_shops.csv'
books_shops = Shops(file_path = full_path , file_id = 'shop_id')
str_reference = books_shops.show_data()
print(str_reference)

full_path = f'{path_root}/books_in_shops.csv'
books_in_shop = Articles(file_path = full_path , file_id = 'shop_id', returned_id='book_id', file_conditions = str_reference)
str_book_reference = books_in_shop.show_data()
print(str_book_reference)

comparing_books = ArticlesCompare(file_path = full_path , file_id = 'book_id', file_conditions = str_book_reference)
str_book_reference_all = comparing_books.show_data()

# Una clase solo BookShops

first_books_shop = BookShops()

print('ver los datos de las vars iteratuando')
it = Iterator([first_books_shop.get_select_book_shop(), first_books_shop.get_select_book()])
process = iter(it)

print(next(process))
print(next(process))

print('ver los datos de las vars iteratuando')
activator = Generator([first_books_shop.get_select_book_shop(), first_books_shop.get_select_book()])
process = activator.generate()

print(next(process))
print(next(process))


