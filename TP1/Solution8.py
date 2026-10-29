# a.
def describe(*number, decimals =2 ,label ="Data"):
    if len(number) == 0:
        print(f"{label}: no values")
        return None
    minimum = min(number)
    maximum = max(number)
    mean = round(sum(number)/len(number), decimals)
    
    print(f"{label}: n={len(number)} min={minimum} max={maximum} mean={mean} ")
    return (len(number), minimum, maximum, mean)
# b.
def make_tag(text, **style):
    argument = ""
    for key, value in style.items():
        argument += f'{key} = "{value}"'
        
    return f"<span{argument}>{text}</span>"
# c. write two lambda func
square = lambda x: x**2
is_adult = lambda age: age >=18

describe(12,7,30,4)

describe(3.14159, 2.71828,decimals=3,label="Constants")
describe() 
print(make_tag("Hello", color="red", size=14)) 
print(square(9), is_adult(17), is_adult(21))
