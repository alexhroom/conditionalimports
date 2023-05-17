import importlib
import inspect

temp_lib = importlib.import_module("lib", package="conditionalimports")

classes = inspect.getmembers(temp_lib, inspect.isclass)

for name, obj in classes:
    if obj.letter == 'B':
        globals().update({name: obj})

del temp_lib