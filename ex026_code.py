import ex026
import ex026  # that seems to do nothing
from pprint import pprint

print("name", ex026.name)
print("height", ex026.height)
print("age", ex026.age)

pprint(ex026.__dict__)
print("height is", ex026.height)
print("height is", ex026.__dict__["height"])
