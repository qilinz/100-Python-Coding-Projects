# Add a greeting message
print("Welcome to the tip calculator")

# Ask the total bill
total_bill = float(input("What was the total bill? "))

# Ask the tip percentage
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask the number of people
total_people = int(input("How many people to split the bill? "))

# Calculate the split bill
bill_plus_tip = total_bill * (1 + tip_percentage / 100)
split_bill = bill_plus_tip / total_people

# Convert the split bill to 2 decimal places
final_split_bill = "{:.2f}".format(split_bill)

# print the final split bill
print(f"Each person should pay: ${final_split_bill}")