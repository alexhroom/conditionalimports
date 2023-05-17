## conditional imports

This is a minimal working example of conditionally importing classes
into submodules, based on features of the classes themselves. This allows
the reuse of 'generic' classes in specific modules, e.g. a class which is the
same apart from one different attribute in submodule `a` vs submodule `b`.

# Usage:
the `lib` file contains 4 classes:
```
class Example1:
    """Example class 1."""

    letter = "A"

class Example2:
    """Example class 2."""

    letter = "A"

class Example3:
    """Example class 3."""

    letter = "B"

class Example4:
    """Example class 4."""

    letter = "D"
```

Open a Python REPL while in this folder. Now try `import a` or `import b`, and
try to run e.g. `a.Example1`, or `a.Example3` or `b.Example2`. You will find that
the namespace `a` only contains the classes with `letter = 'A'`, and the namespace
`b` only contains the classes with `letter = 'B'`!


# How this works
The `__init__.py` files for `a` and `b` import the shared `lib` file like so:
```
temp_lib = importlib.import_module("lib", package="conditionalimports")
```
under the name `temp_lib`. We then use `inspect.getmembers` to get the classes
from this object. Note that the function can take any predicate (here we've
simply chosen `inspect.isclass`), for greater fine-tuning if desired.

We then iterate through all of these classes; if they satisfy a condition
(in our case, whether the letter is "A" or "B"); if they do, then we add them
to the global variables for the submodule's scope (which is equivalent to what
happens when we do something like `from module import class`).

Finally, we use `del temp_lib` to 'un-import' the full library package.
