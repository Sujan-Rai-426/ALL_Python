# =======================================================================
# NOTE: AND Operator (Both conditions must be True)
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")  # Output: You can drive

# Multiple AND conditions
marks = 85
attendance = 80
is_paid = True

if marks >= 60 and attendance >= 75 and is_paid:
    print("Eligible for exam")  # Output: Eligible for exam
    


# =======================================================================
# NOTE: OR Operator (At least one condition must be True)
day = "Saturday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("Weekend!")  # Output: Weekend!

# Real world example
has_id = True
has_passport = False
if has_id or has_passport:
    print("Can board the flight")  # Output: Can board the flight



# =======================================================================
# NOTE: NOT Operator (Reverses the condition)
is_raining = False

if not is_raining:
    print("Let's go outside!")  # Output: Let's go outside!

# With other operators
is_logged_in = False
if not is_logged_in:
    print("Please login first")  # Output: Please login first



# =====================================================================
# NOTE: Combining Multiple Operators
# Complex condition
age = 22
income = 50000
credit_score = 750

# Loan eligibility
if (age >= 21 and age <= 60) and (income >= 30000 or credit_score >= 700):
    print("Eligible for loan")  # Output: Eligible for loan
else:
    print("Not eligible for loan")