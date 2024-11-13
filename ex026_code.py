import ex026
import ex026  # that seems to do nothing
from pprint import pprint
from importlib import reload

print("name", ex026.name)
print("height", ex026.height)
print("age", ex026.age)

pprint(ex026.__dict__)
print("height is", ex026.height)
print("height is", ex026.__dict__["height"])

print(f"I am currently {ex026.height} inches tall.")

ex026.__dict__["height"] = 1000
print(f"I am now {ex026.height} inches tall.")

ex026.height = 12
print(f"Oopsm now I'm {ex026.__dict__['height']} inches tall.")

reload(ex026)
print(f"I am currently {ex026.height} inches tall.")

print(pprint.__doc__)
help(pprint)

n = 13
print(f"n.__repr__() is {n.__repr__()}")

print(f"print.__name__ is {print.__name__} and it is defined in {
      print.__module__} module")
