name = "Sok dara"
age = 20
major = "Data science"
gpa = 3.67
is_scholar = True

print("===============================")
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Major   : {major}")
print(f"GPA     : {gpa:.2f}")
print(f"Scholar : {is_scholar}")
print("===============================")
print(name, "->", type(name).__name__)
print(age, "->",type(age).__name__)
print(major, "->",type(major).__name__)
print(gpa, "->",type(gpa).__name__)
print(is_scholar,"->", type(is_scholar).__name__)
print("===============================")

age = "20"
print("New age ->",type(age).__name__)
# type is a string  , because it was put in ""
