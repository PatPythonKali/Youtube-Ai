import sys
x = "Hello"
# sys.modules[__name__] is the instance of the current module
var = getattr(sys.modules, 'var_name')

