import pickle
from .Category import *
from .Dish import *


class Items:
	def __init__(self):
		self._items = []

	def add_dish(self):
		dish = Dish()
		self._items.append(dish)

	def add_cat(self):
		mcat = Category()
		self._items.append(mcat)

	def print_items(self):
		print('-Список блюд-')
		for item in self._items:
			item.output()
			print(" ")
		
	def edit(self):
		print('Выберите категорию для редактирования')
		i = 0
		for item in self._items:
			print("{0}. {1}".format(i, item.tittle))
			i+=1
		try:
			i = int(input('Ввод: '))
			self._items[i].inp_dish()
		except:
			print('Неверный ввод\n')
			self.edit()

	def save(self):
		pickle.dump(self._items, open('st11/output.txt', 'wb'))
		print('Список сохранен в файл output.txt')

	def load(self):
		try:
			self._items = pickle.load(open('st11/output.txt', 'rb'))
			print('Список загружен из файла\n')
		except:
			print('Файл не найден\n')

	def delete(self):
		print('Выберите запись')
		i = 0
		for item in self._items:
			print("{0}. {1}".format(i, item.tittle))
			i+=1
		try:
			i = int(input('Ввод: '))
			self._items.pop(i)
			print('Запись удалена\n')
		except:
			print('Неверный ввод\n')
			self.delete()

	def clear(self):
		self._items.clear()
		print('Список очищен\n')
