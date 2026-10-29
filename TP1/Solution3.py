def celsius_to_fahrenheit( c, round_to = 1):
    temp = c * ( 9 / 5 ) + 32
    return round(temp, round_to)

def fahrenheit_to_celsius( f, round_to = 1):
    temp = (f - 32 ) * ( 5 / 9 )
    return round(temp, round_to)

# a. Use a for loop with range(0, 101, 20) to print the conversion table
print(f"a.\n  °C   |   °F")
print("-------+---------")
for a in range (0,101,20):
    calculated_temp = celsius_to_fahrenheit(a)
    print(f" {a:5} | {calculated_temp:6}")

# b.Convert 98.6 °F (normal body temperature) to Celsius.
print(f"b.\n 98.6 °F = {fahrenheit_to_celsius(98.6):.1f} °C")

# c.Convert 37 °C to Fahrenheit and back again. Do you get 37.0?
print(f"c.\n 37 °C = {celsius_to_fahrenheit(37):.1f} °F")
print(f"Convert backward : {fahrenheit_to_celsius(celsius_to_fahrenheit(37))} °C")
#Ans: Yes, we still got 37.0 after converting celcius to Fahrenheit

# d.Call one function with round_to=3. 

print(f"d.\nUsing round_to = 3 :{celsius_to_fahrenheit(172.6212, 3)} °F")

# Why is a default argument useful here?
# Ans: It is useful because the function can be called without having to input the round_to 
#      each time the fuinction is called. Also, if necessary, it can be modified.
#      with round_to = 3, it will show the answer up to 3 decimal places
#      but if it's 0, the trailing zero will not be shown. 
#      Ex.167.200 will be shown as 167.2