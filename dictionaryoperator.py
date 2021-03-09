# empty dictionary
d={}
print(f"my dictionary is {d}")
students = {1: "John", 2: "Valentina", 3: "Beatriz"}
students_list = {"John", "Valentina", "Beatriz"}

# add a new student
students[7] = "Carlos"
print(f"my students are: {students}")

# In a dictionary the order is not important, because you have keys to access the order.
print(f"Carlos is: {students[7]}")
students["nine"] = "Ignacio"
print(f"my students are: {students}")
del students[2]
print(f"my students are: {students}")

# we can iterate over a dictionary
for key in students:
    print(f"{key} -> {students[key]}" )




