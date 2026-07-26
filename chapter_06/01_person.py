#Project: Dictionary - (PCC Exercis 6: - 1-3)
#Author: Paulson Idoko
#Date: 25th July, 2026

#--- Phase - 1 Person ---
"""
Task 6-1:Person.
Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You 
should have keys such as first_name, last_name, age, and city. Print each 
piece of information stored in your dictionary.
"""

person = {
	'first_name': 'juliet',
	'last_name': 'idoko',
	'age': 32,
	'city': 'abuja',
}
print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())
