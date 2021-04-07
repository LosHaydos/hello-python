import book
import author

first_author = author.Author("John", "Doe", "Australian")
book = book.Book("All About Python", 1, author)

book.lend("testUser")