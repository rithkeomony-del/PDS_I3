# Part A:
#          Expression          |  Prediction  | Python's answer
# _______________________________________________________________
# int("7") + 3.5               |  10.5        |  10.5
# str(10) * 3                  |  101010      |  101010
# bool(""), bool(" ")          |  False True  |  False True
# int(3.99)                    |  3           |  3
# float("1e3")                 |  1000        |  1000.0
# int(True) + float("2.5")     |  3.5         |  3.5
# round(2.5), round(3.5)       |  3 4         |  2 4
# type(10 / 2)                 |  float       |  <class 'float'>

# Part B: function turning string into number
def safe_int(text):
    
    text = text.strip()
    if text.lstrip("-").isdigit():         
        return int(text)
    try:
        return int(float(text))            
    except ValueError:
        return None                       
    
for sample in ["42", " -8 ", "3.9", "abc", ""]: 
    print(repr(sample), "->", safe_int(sample))
    
# Part C:
num1 = safe_int(input("Enter an input 1: "))
num2 = safe_int(input("Enter an input 2: "))

if (num1 is None) or (num2 is None) :
    print("sorry, The input value is not a number")
else:
    print(f"Sum = {num1+num2}")

 