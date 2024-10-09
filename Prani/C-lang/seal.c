#include <stdio.h>
#include <string.h>

// Define a maximum number of books in the library
#define MAX_BOOKS 100

// Structure to represent a book
struct Book {
    char title[50];
    int isBorrowed;
};

// Library structure to manage books
struct Library {
    struct Book books[MAX_BOOKS];
    int count; // Number of books in the library
};

// Function to initialize the library with some books
void initializeLibrary(struct Library *lib) {
    strcpy(lib->books[0].title, "C Programming");
    lib->books[0].isBorrowed = 0;

    strcpy(lib->books[1].title, "Data Structures");
    lib->books[1].isBorrowed = 0;

    strcpy(lib->books[2].title, "Algorithms");
    lib->books[2].isBorrowed = 0;

    strcpy(lib->books[3].title, "Operating Systems");
    lib->books[3].isBorrowed = 0;

    strcpy(lib->books[4].title, "Database Systems");
    lib->books[4].isBorrowed = 0;

    lib->count = 5; // Initially, 5 books are added
}

// Function to display available books
void displayAvailableBooks(struct Library *lib) {
    printf("\nBooks currently available in the library:\n");
    int availableBooks = 0;
    for (int i = 0; i < lib->count; i++) {
        if (!lib->books[i].isBorrowed) {
            printf(" - %s\n", lib->books[i].title);
            availableBooks++;
        }
    }
    if (availableBooks == 0) {
        printf("No books are currently available.\n");
    }
}

// Function to borrow a book
void borrowBook(struct Library *lib) {
    char bookName[50];
    printf("Enter the name of the book you want to borrow: ");
    getchar(); // To clear the newline left by previous input
    fgets(bookName, sizeof(bookName), stdin);
    bookName[strlen(bookName) - 1] = '\0'; // Remove the newline character

    for (int i = 0; i < lib->count; i++) {
        if (strcmp(lib->books[i].title, bookName) == 0) {
            if (!lib->books[i].isBorrowed) {
                lib->books[i].isBorrowed = 1;
                printf("\nYou have borrowed '%s'. Please return it after reading.\n", bookName);
                return;
            } else {
                printf("\nSorry, the book '%s' is already borrowed.\n", bookName);
                return;
            }
        }
    }
    printf("\nSorry, the book '%s' is not available in the library.\n", bookName);
}

// Function to return a book
void returnBook(struct Library *lib) {
    char bookName[50];
    printf("Enter the name of the book you want to return: ");
    getchar(); // To clear the newline left by previous input
    fgets(bookName, sizeof(bookName), stdin);
    bookName[strlen(bookName) - 1] = '\0'; // Remove the newline character

    for (int i = 0; i < lib->count; i++) {
        if (strcmp(lib->books[i].title, bookName) == 0) {
            if (lib->books[i].isBorrowed) {
                lib->books[i].isBorrowed = 0;
                printf("\nThank you for returning '%s'.\n", bookName);
                return;
            } else {
                printf("\nThe book '%s' was not borrowed.\n", bookName);
                return;
            }
        }
    }
    printf("\nThe book '%s' is not recognized in our system.\n", bookName);
}

// Main function with the user menu
int main() {
    struct Library library;
    initializeLibrary(&library);

    while (1) {
        int choice;
        printf("\n\n===== Welcome to the Library Management System =====\n");
        printf("1. Display all available books\n");
        printf("2. Borrow a book\n");
        printf("3. Return a book\n");
        printf("4. Exit\n");
        printf("Enter your choice (1-4): ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                // Display available books
                displayAvailableBooks(&library);
                break;
            case 2:
                // Borrow a book
                borrowBook(&library);
                break;
            case 3:
                // Return a book
                returnBook(&library);
                break;
            case 4:
                // Exit the program
                printf("\nThank you for using the Library Management System. Goodbye!\n");
                return 0;
            default:
                printf("\nInvalid choice! Please enter a number between 1 and 4.\n");
        }
    }

    return 0;
}
