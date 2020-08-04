income = int(input())
if income < 15528:
    calculated_tax = 0
elif 15527 < income < 42708:
    calculated_tax = 15 * income / 100
    # calculated_tax = 15 * (income - 15527)
elif 42707 < income < 132407:
    calculated_tax = 25 * income / 100
    # calculated_tax = 25 * (income - 42707) + 15 * (42708 - 15527)
else:
    calculated_tax = 28 * income / 100
    # calculated_tax = 28 * (income - 132407) + 25 * (income - 42707) + 15 * (42708 - 15527)
calculated_tax = round(calculated_tax)
percent = round(calculated_tax * 100 / income)
print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
