# artist = {
#     "first": "Neil",
#     "last": "Young",
# }

# full_name = artist["first"] + " " + artist["last"]

# print(full_name)

# Accessing data from a dict.

# instructor = {
#     "name": "ItsMe",
#     "owns_dog": "False",
#     "num_curs": "2",
#     "code": "python",
#     "humor": None,
#     "poept": "graag",
#     "items": [1, 2, 3, 4, 5, 6],
# }

# # For looping over the values:

# for v in instructor.values():
#     print(v)

# # For the keys:
# for key in instructor.keys():
#     print(key)

# # for both: remember it will return a tuple
# for item in instructor.items():
#     print(item)

# # different way to do so:

# for k, v in instructor.items():
#     print(k, v)

# donations = dict(
#     sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0
# )
# totaldon = sum(donations.values())
