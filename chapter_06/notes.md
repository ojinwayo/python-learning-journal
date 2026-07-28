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

### 5. Sorting Dictionaries & Handling Unique Values

#### Sorting Keys with `sorted()`
Dictionaries preserve insertion order in modern Python, but if you need to process or display keys in alphabetical/numerical order, wrap `.keys()` inside the `sorted()` function.

```python
# Iterating through dictionary keys in alphabetical order
user_scores = {
    'charlie': 85,
    'alice': 92,
    'bob': 78,
}

for name in sorted(user_scores.keys()):
    print(f"{name.title()}: {user_scores[name]}")
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
    
    
#### 5 Removing Duplicate Values with `set()`
If multiple keys have the same value, calling `.values()` will return duplicate items. Wrapping `.values()` in `set()` removes all duplicates so each value is only listed once.

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Without set() -> Prints 'python' twice
# With set()    -> Prints 'python' once

for language in set(favorite_languages.values()):
    print(language.title())
