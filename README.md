# eng110-python

## This is a repository created for learning Python.

### Some basics:

- Variables are declared using `var_name = var_value`;
- Standard mathematical operators: `+` (add), `-`(subtract), `*`(multiply), `/`(divide), `^`(to the power of), `%` (modulo);
- Can update variables with `x = x + 1` (for example), or `x += 1`.

#### Variable types:
##### Integers and floats

- `int` and `float` variables are numbers;
- Numerically, `1` and `1.0` are equal, but behave slightly differently in Python when being used.

##### Strings

- Stings are characters enclosed in `''` or `""`. 

#### Booleans

- Booleans are `True` and `False` (spelt as given). See below for their use with conditionals.

#### Collection types

##### Lists
- Lists are represented with square brackets: e.g., `['eggs', 3, True]`;
- They are ordered since their contents are stored in the order they are entered, and mutable since Python allows us to 
edit their contents.
- To get item at nth index, use `list[n]`; e.g, `['eggs', 3, True][0]` returns `'eggs'`.

##### Sets
- Sets are represented with curly brackets: e.g., `{'eggs', 3, True}`;
- They are unordered (calling the set multiple times will give different orders) and mutable.

##### Tuples
- Tuple are represented with standard brackets: e.g., `('eggs', 3, True)`;
- They are ordered and immutable - once created, Python does not allow their order or contents to be edited.

##### Dictionaries

- Dictionaries are sets where __ALL__ items are key-value pairs, written in the form `"key": value`; e.g., 
`{"name": 'eggs', "number_in_basket": 3, "unbroken": True}`;
- Lists of the keys/values can be found using `.keys()` and `.values()` methods (see below).