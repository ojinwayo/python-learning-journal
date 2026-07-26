
#Project: Dictionary - (PCC Exercis 6.3)
#Author: Paulson Idoko
#Date: 26th July, 2026

#--- Phase - 1 Glossary - ---
"""
Task 6-3:Glossary.
A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous 
chapters. Use these words as the keys in your glossary, and store their 
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line. Use the 
newline character (\n) to insert a blank line between each word-meaning 
pair in your output.
"""

glossary = {
	'insert': 'to add an object to another given object such as lists',
	'delete': 'to get rid of an object completely',
	'slicing': 'to extract a subset of a given object',
	'pop': 'to temporarily remove an object from another',
	'curly_braces': 'a form of brackets that are curly in the middle'
}

print(f"Insert: {glossary['insert']}.")
print(f"\nDelete: {glossary['delete']}.")
print(f"\nSlicing: {glossary['slicing']}.")
print(f"\nPop: {glossary['pop']}.")
print(f"\nCurly braces: {glossary['curly_braces']}.")

print()

#printing the word on one line and then-
#printing its meaning indented on a second line.

print(f"Insert: \n\t{glossary['insert']}.")
print(f"\nDelete: \n\t{glossary['delete']}.")
print(f"\nSlicing: \n\t{glossary['slicing']}.")
print(f"\nPop: \n\t{glossary['pop']}.")
print(f"\nCurly braces: \n\t{glossary['curly_braces']}.")
