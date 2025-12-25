def compute_tax(status, income):
    # Tax brackets for each filing status using (income_limit, tax_rate)
    brackets = {
        0: [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)],
        1: [(16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)],
        2: [(8350, 0.10), (33950, 0.15), (68525, 0.25), (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)],
        3: [(11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)]
    }

    tax = 0
    previous_threshold = 0

    # For loop to check each tax bracket for the selected filing status
    for current_threshold, rate in brackets[status]:
        
        if income > current_threshold:
            tax += (current_threshold - previous_threshold) * rate
            previous_threshold = current_threshold # Stores the lower bound of the current tax bracket
        else:
            tax += (income - previous_threshold) * rate
            break

    return tax

print("Filing Status:")
print("0 - Single")
print("1 - Married Filing Jointly or Qualifying Widow(er)")
print("2 - Married Filing Separately")
print("3 - Head of Household")

status = int(input("Enter the filing status (0–3): "))

if status < 0 or status > 3:
    print("Invalid filing status. Please enter a number between 0 and 3.")
    exit()

    

income = float(input("Enter the taxable income: $"))

if income < 0:
    print("Invalid income. Taxable income cannot be negative.")
    exit()

total_tax = compute_tax(status, income)

print(f"Your personal income tax is: ${total_tax:,.2f}")