# Chapter 6: Dictionaries — Summary Notes
Author: Paulson Idoko
Date: July 25, 2026

## Core Rules & Syntax

### 1. Accessing Values
Specify the dictionary name followed by the key in square brackets:
```python
person = {'first_name': 'juliet', 'age': 32}
print(person['first_name'])
```

### 2. Adding Key-Value Pairs
Assign a value to a new key:
```python
person['city'] = 'abuja'
```

### 3. Deleting Key-Value Pairs
Use the `del` statement with the exact key spelling:
```python
del person['age']
```

### 4. Modifying Values
Specify the dictionary name with the key in square brackets, then assign the new value:
```python
person['city'] = 'enugu'
```
