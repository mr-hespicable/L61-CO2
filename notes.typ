= Data Types: General
All data is held as a binary number `:=` *datum*. But consider `0100 1000 0110 1001`.
The datatype tells us what this number actually is.

Data types come in two flavors: *primitive* and *composite*. \
A primitive data type is a datatype which is stored as a single object in memory.
  - integer
  - float
  - boolean
  - char
Languages usually operate very quickly on these primitive data types.

Composite data types are composed of two or more primitive data types.
- date
- array (dynamic or static length)


= Primitive Data Types
== Integers
*Integers* are whole numbers, included negative integers and 0.
Many languages distinguish between signed and unsigned integers, or have different 
integer types with different maximum values.
 
For example, in Java:
- byte (1 byte): -128 to 127
- short (2 bytes): -32768 to 32767
- int (4 bytes): -2147483648 to 2147483647
- long (8 bytes): -9223372036854775808 to 9223372036854775807

== Real
*Real* or *floating point* data types cover numbers with a fractional part, 
like 6.7 or 3.14.

Many languages allow real data types with different maximum values for real 
numbers, and also with different precisions.

In python:
- `float`, with 53-bit precision, or about 15 decimal digits.

In Java:
- `float` (4 bytes), about 6/7 decimal digits.
- `double` (8 bytes), about 15 decimal digits.

== Boolean
- Non-numeric
- Python uses a whole byte instead of a bit

== String
Holds a sequence of encoded characters.

In some languages, strings are composite types (`[char]`) but in python, the string
data type _is_ primitive. Encoded using UTF-8. 

#pagebreak()

== Pointer
A *pointer* data type holds the address of a value in memory. So the value of the 
pointer is just the memory location, not the actual value.

Pointers are used in most C-like languages (e.g. `C++`, `rust`) to make it easier to 
navigate complex data structures.

However, *pointers do not exist in python*.

= Strong and Weak Typing
In Python, variables can be declared as a datatype (e.g. `i: int = 2`), but you can
change the datatype of the variable to a string without errors.

This is known as *weak typing*.

In other languages (like rust, C++), *strong typing* is used.

== Nothing?
Some data types allow empty representations e.g. `[]` or `""`. Though these objects
are 'empty', they still have the type `list` and `str` respectively.

The only datatype that is truly 'nothing' is `None` in python (of type `NoneType`). 

= Composite Data Types

== Array
An *array* is an ordered group of elements of the same data type. \
Like a `Vec` in Rust.

== Record
A record is an ordered group of elements. These elements can be of different data
types.

In Python, lists, dicts, and tuples are all records.

== User-defined data types
A user-defined data type is a data type created by a user based on existing primitive and
composite data types.

In `python`:
```python
pet_dict = {'id': None, 'name': None, 'species': None, 'owner': None}
```
```python
my_pet = pet_dict.copy()
my_pet['id'] = 23301
my_pet['name'] = 'Aggie'
my_pet['species'] = 'cat'
my_pet['owner'] = 'Mr Clark'
```

== Subroutines
A *procedure* is a subroutine that does not return a value.
A *function* is a subroutine that returns a one or more values.

= Object-Oriented Programming

== Inheritance
A subclass *inherits* the attributes and methods of its superclass by default.
e.g. `class Foo extends Bar` or in python, for `class Foo(Bar)`, Foo inherits Bar.

== Attributes and Methods
Unless it says otherwise, attributes and methods of a class are private by default.
