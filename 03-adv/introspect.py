my_string = 'my string'

object_methods = [method_name for method_name in dir(my_string) if callable(getattr(my_string, method_name))]
print(object_methods)
