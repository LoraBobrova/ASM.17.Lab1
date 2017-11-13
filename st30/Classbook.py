from st30.Book import Book


class Classbook(Book):
	subject = ''
	edit_menu = {}

	def __init__(self):
		Book.__init__(self)
		self.edit_menu["5"] = ["subject", self.set_subject]

	def set_subject(self):
		self.subject = input('Enter the subject to be learned using the book\n')

	def book_registration(self):
		Book.book_registration(self)
		self.set_subject()

	def show_book(self):
		Book.show_book(self)
		print('Subject: ' + self.subject)
