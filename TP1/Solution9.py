# a. write electricity_bill func
def electricity_bill(kwh):
    if kwh < 0:
        return None
    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)
    
    cost = (tier1 * 480 +tier2 * 610 +tier3 * 730)
    subtotal = cost + 2000
    total = subtotal * 1.10
    
    return round(total)
# b. print a table for the list of energy_usage
Energy_usage = [0, 35, 50, 120, 200, 350]

for kwh in Energy_usage:
    bill = electricity_bill(kwh)
    usd = bill / 4100

    print(f"{kwh:6} kWh -> {bill:8,}riel (≈ {usd:7.2f} USD)")

# c. 56Ask the user for their monthly consumption and print their bill.
kwh = float(input("Enter monthly consumption (kWh): "))

bill = electricity_bill(kwh)

if bill is None:
    print("Invalid consumption")
else:
    print(f"Your bill is {bill:,} riel")