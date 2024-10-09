'''# Library Management System

class Library:
    def __init__(self, list_of_books):
        # List to store the available books in the library
        self.available_books = list_of_books

    def display_available_books(self):
        # Display all the available books in the library
        if len(self.available_books) > 0:
            print("\nBooks currently available in the library:")
            for book in self.available_books:
                print(f" - {book}")
        else:
            print("\nNo books available in the library currently.")

    def borrow_book(self, book_name):
        # Borrow a book from the library if available
        if book_name in self.available_books:
            print(f"\nYou have borrowed '{book_name}'. Please return it after reading.")
            self.available_books.remove(book_name)
        else:
            print(f"\nSorry, the book '{book_name}' is either not available or already borrowed.")

    def return_book(self, book_name):
        # Return a book to the library
        print(f"\nThank you for returning '{book_name}'.")
        self.available_books.append(book_name)


class User:
    def request_book(self):
        # User requests a book by entering its name
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def return_book(self):
        # User returns a book by entering its name
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


def main():
    # Initial list of books available in the library
    library = Library(["Python Programming", "Data Structures", "Algorithms", "Machine Learning", "Artificial Intelligence"])
    user = User()

    while True:
        print("\n\n===== Welcome to the Library Management System =====")
        print("1. Display all available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        choice = int(input("\nEnter your choice (1-4): "))

        if choice == 1:
            # Display available books
            library.display_available_books()

        elif choice == 2:
            # Borrow a book
            requested_book = user.request_book()
            library.borrow_book(requested_book)

        elif choice == 3:
            # Return a book
            returned_book = user.return_book()
            library.return_book(returned_book)

        elif choice == 4:
            # Exit the program
            print("\nThank you for using the Library Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()'''







"""# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
	global expression

	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)


# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)

		# initialize the expression variable
		# by empty string
		expression = ""

	# if error is generated then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background="light blue")

	# set the title of GUI window
	gui.title("Simple Calculator")

	# set the configuration of GUI window
	gui.geometry("270x150")

	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()

	# create the text entry box for
	# showing the expression .
	expression_field = Entry(gui, textvariable=equation)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	expression_field.grid(columnspan=4, ipadx=70)

	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	button1 = Button(gui, text=' 1 ', fg='black', bg='white',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='white',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='white',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='white',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='white',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='white',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='white',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='white',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='white',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='white',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='pink',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='pink',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='pink',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='pink',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='pink',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='pink',
				command=clear, height=1, width=7)
	clear.grid(row=5, column='1')
 
	                        
	# start the GUI
	gui.mainloop()"""


