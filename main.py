from src.phonebook import *

phonebook = Phonebook()
phonebook.add("Bruno", "99999-9999")
phonebook.add("Rafael", "90000-0000")

print(phonebook.lookup("Bruno"))
print(phonebook.get_names())
print(phonebook.get_numbers())
print(phonebook.get_phonebook_reverse())
print(phonebook.get_phonebook_sorted())

print(phonebook.search("Bruno"))
