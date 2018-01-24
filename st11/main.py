from .Items import *

dish_menu = Items()

MENU = [
		["Добавить блюдо",dish_menu.add_dish],
		["Добавить категорию",dish_menu.add_cat],
		["Показать меню",dish_menu.print_items],
		["Сохранить меню",dish_menu.save],
		["Загрузить меню из файла",dish_menu.load],
		["Очистить список",dish_menu.clear],
		["Редактировать запись в меню",dish_menu.edit],
		["Удалить запись",dish_menu.delete]
	]

def main():
	try:
		i = 0
		print("------------------------------")
		for item in MENU:
			print("{0:2}. {1}".format(i, item[0]))
			i += 1
		print("Введите любое другое значение для выхода")
		option = int(input("ввод: "))
		if option != 8:
			MENU[option][1]()
			main()
	except:
		print('Выход')

if __name__ == "__main__":
	main()
