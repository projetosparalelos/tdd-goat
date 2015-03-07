from selenium import webdriver


browser = webdriver.Firefox()

# Popei uses an online to-do app.
# He opens the home page
browser.get('http://127.0.0.1:8000')

# He notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# He wants to enter a to-do item as usual

# He types "Buy TDD book" into a text box

# When he hits enter, the page updates and now the page lists
# "1: Buy TDD book" as an item in a to-do list

# He still needs to add other items to the to-do list
# He enters "Sleep tight"

# The page updates again, and now the list contains the two items

# He copies the url to access his to-do list anywhere he goes.

# He visits that url later 

# He goes back to watever he was doing

browser.quit()
