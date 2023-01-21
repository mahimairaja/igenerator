# igenerator

**igenerator** is a python package that allows you to generate psudo random numbers and write them to a CSV file or SQLite database with just a few lines of code. The package utilizes the [JAX](https://jax.readthedocs.io/en/latest/#) function which is based on the C++ library [random123](http://www.thesalmons.org/john/random123/). These functions are designed to be fast and efficient, and are suitable for use in machine learning applications.

## Installation
You can install the package using pip:

``` bash
pip install igenerator
```

## Usage
To use the package, you first need to import it:

``` python
from igenerator import LiveGenerator
```

Then, you can create an instance of the `TrueGenerator` class:

```python
generator = LiveGenerator()
or
generator = LiveGenerator(0) # Pass a optional parameter (i.e any integer ) to set the seed val.

```

You can use the `randomInt()` method to generate a list of random integers within a certain range:
``` python
result = generator.randomInt(2, 15, 4)
``` 

The above code will generate a list of 4 random integers between 2 and 15 (inclusive).

You can then use the `writeCsv()` method to write the list of random numbers to a CSV file:

``` python
generator.writeCsv(result, 'your_csv_name.csv')
```

### Note
Before writing into a csv file remember to create one with desired headers.



And use the `writeSql()` method to write the list of random numbers to a SQLite database:

```python
table_name = "your_table_name"
generator.writeSql(result,'your_database_name.db',table_name)
```

### Note
Before writing into a sqlite database remember to create a table with desired headers.

## Example :

``` python
from igenerator.generate import LiveGenerator

generator = LiveGenerator()
result = generator.randomInt(2,15,4) # For float values use randomFloat

generator.writeCsv(result,'your_csv_name.csv')

table_name = "your_table_name"
generator.writeSql(result,'your_database_name.db',table_name)

```

## License
This package is released under the [MIT License](https://opensource.org/licenses/MIT).