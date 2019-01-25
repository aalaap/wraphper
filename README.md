![PyPi Status](https://img.shields.io/pypi/status/wraphper.svg) ![PyPi Python Version](https://img.shields.io/pypi/pyversions/wraphper.svg) ![PyPi Downloads](https://img.shields.io/pypi/dm/wraphper.svg) ![GitHub Issues](https://img.shields.io/github/issues-raw/aalaap/wraphper.svg) ![GitHub Commit Activity](https://img.shields.io/github/commit-activity/y/aalaap/wraphper.svg) ![PyPi License](https://img.shields.io/pypi/l/wraphper.svg) ![PyPi Version](https://img.shields.io/pypi/v/wraphper.svg)

# wraphper

Python wrappers for PHP functions, when you just can't shake it.

## Why?

If you're coming from PHP, you'll take a bit of time getting used to the new names or methods in Python. You could look up something like `"python str_replace"` everytime you want to do so, or you could just save time and use `php.str_replace('Hello', 'Goodbye', 'Hello, world!')`.

Why not?

## Installation

Pip it.

```
$ pip install wraphper
```

## Usage

Import the module and then fulfil your PHP fantasies in Python:

```python
from wraphper import wraphper as php

a = [1, 2, 3]
php.count(a)
# outputs: 3
```

## Supported functions

This module is a work in progress. Not all functions are supported yet. The current list includes:

- [count](http://php.net/manual/en/function.count.php)

PRs with more functions are welcome!

## Performance and Security

wraphper doesn't internally call PHP to run these functions, it simply provides you a PHP-like function name that runs the Python equivalent. As such, performance is unaffected because only Python is running.

Similarly, there are no implications of this on security.

## Contributing

Follow these rules with contributed functions:

- The function must be an [native PHP function](http://php.net/manual/en/funcref.php), not from a third-party library. 
- The name of the function must match the original exactly. Otherwise, the purpose of this module is defeated.
- The function should take the exact same number of arguments as the original.
- The argument types must match the PHP types as closely as possible, so `string` is `str`, `int` is `int`, `array` is `list` or `dict`, etc.
- The function must throw an appropriate exception with the exact same error message from the PHP function.
- The function should avoid any pre- or post-processing of the argument or return value. The goal is not to match PHP functions' inputs and outputs, but to provide a PHP-familiar syntax for Python developers.

## Testing

Tests can be run by the following command:

```
$ python tests.py
```

## Compatibility

wraphper has been checked with Python 2.7 and 3.6, but there's no reason why it shouldn't work with older 3.x versions.
