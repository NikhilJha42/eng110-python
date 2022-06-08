# eng110-python

## This is a repository created for learning Python 3.

I recommend reading the [Python documentation](https://docs.python.org/3/) for further uses and details not fully covered here.

I have another repository if you're interested in learning [OOP with Python](https://github.com/NikhilJha42/eng110-python-oop).

#### Some basics:

- Variables are declared using `var_name = var_value`;
- Standard mathematical operators: `+` (add), `-`(subtract), `*`(multiply), `/`(divide), `^`(to the power of), `%` (modulo);
- Can update variables with `x = x + 1` (for example), or `x += 1`.

### [Variables](variables)
#### Integers and floats

- `int` and `float` variables are numbers;
- Numerically, `1` and `1.0` are equal, but behave slightly differently in Python when being used.

#### Strings

- Stings are characters enclosed in `''` or `""`. 

#### Booleans

- Booleans are `True` and `False` (spelt as given). See below for their use with conditionals.

### [Collections](collections) 

#### Lists
- Lists are represented with square brackets: e.g., `['eggs', 3, True]`;
- They are ordered since their contents are stored in the order they are entered, and mutable since Python allows us to 
edit their contents.
- To get item at nth index, use `list[n]`; e.g, `['eggs', 3, True][0]` returns `'eggs'`.

#### Sets
- Sets are represented with curly brackets: e.g., `{'eggs', 3, True}`;
- They are unordered (calling the set multiple times will give different orders) and mutable.

#### Tuples
- Tuple are represented with standard brackets: e.g., `('eggs', 3, True)`;
- They are ordered and immutable - once created, Python does not allow their order or contents to be edited.

#### Dictionaries

- Dictionaries are sets where __ALL__ items are key-value pairs, written in the form `"key": value`; e.g., 
`{"name": 'eggs', "number_in_basket": 3, "unbroken": True}`;
- Lists of the keys/values can be found using `.keys()` and `.values()` methods (see below).

### [Functions](functions)

Created using the following syntax:
```python
def func_name(param_1, param_2):
    pass
```
where `pass` is replaced with some code utilising the parameters; `pass` here informs Python to do nothing if the function
is called. You can also specify data types for the parameters, such as `int` and `str`:
```python
def func_name(param_1:int, param_2:str):
    pass
```

Note that if we want a function to return a value when it is called, the final piece of code within the function 
must be `return some_value`:
```python
def add(int_1, int_2):
    return int_1 + int_2
```

We can call built-in functions, known as methods, on data types. For example:
```python
basket = ["eggs", 3, True]
basket.append("hello") # adds item "hello" to the end of the list.
print(basket) # prints ["eggs", 3, True, "hello"]
basket.pop() # removes last item from the list (in this case "hello") and returns this item.
print(basket) # prints ["eggs", 3, True]

greeting = "hello"
greeting.capitalize() # returns "Hello"
greeting.upper() # returns "HELLO"
print(greeting) #returns "hello"

personal_info = {"name": "Jha, Nikhil", "role": "DevOps Consultant"}
personal_info.keys() # returns ["name", "role"]
personal_info.values() # returns ["Jha, Nikhil", "DevOps Consultant"]
```
Note that in the above, the first block of code directly modifies the list `basket`, whereas the method calls in the 
second block return the modified versions, but leave the original unchanged.

### [Conditionals](conditionals)
- `if` statements have a similar syntax to functions:
```python
if statement_1 == statement_2:
    pass
```
where `==` can be replaced by any other conditional:
- `==` : equal to
- `!=` : not equal to
- `<` : less thab
- `>` : greater than
- `<=` : less than or equal to
- `>=` : greater than or equal to

### [Loops](conditionals)

- `for` loops are written as follows:
```python
for index in list:
    pass
```
where `list` represents a list; typically, this is either a range of indexes (obtained using `range(n)` for some integer 
`n`) or a list where we want to apply the same code to each item. For e.g.:
```python
for name in list_of_names:
    print(name.capitalize)
```

### [File handling](file_handling)
See the above link for the notation on opening and reading/writing content from/into files.

### Importing python files and packages
See the end of this section for links to different directories.

If you create two Python files, you can write code in one and then import it into the other:
- `file_1`:
  ```python
  def add(int_1, int_2):
    return int_1 + int_2
  ```
- `file_2`:
  ```python
  from file_1 import add
  add(1, 2) # returns 3
  ```
- To import everything from file_1:
  ```python
  from file_1 import *
  ```
- You might also use:
  ```python
  import file_1
  file_1.add(1, 2) # also returns 3
  ```
  
You can also import packages as required for functionality - but remember this will increase the size of the python file:
```python
import math

math.ceil(3.2) # returns 4
math.floor(3.2) # returns 3
```

You can find further examples of file handling and importing packages with the following python projects:

[CSV](csvfiles)

[JSON](json_intro)

[Requests APIs](APIs)

### [Testing](Testing)
The above link will take you to the directory covering unit testing - this uses classes, so you may wish to cover OOP in Python 
before doing this. 