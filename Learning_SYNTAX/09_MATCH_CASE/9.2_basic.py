# Boolean patterns
def check_status(status):
    match status:
        case True:
            return "Active"
        case False:
            return "Inactive"
        case _:
            return "Unknown"

print(check_status(True))   # Output: Active


# None pattern
def process_data(data):
    match data:
        case None:
            return "No data provided"
        case "error":
            return "Error occurred"
        case _:
            return f"Processing: {data}"

print(process_data(None))   # Output: No data provided


# Mixed literals
def identify_value(value):
    match value:
        case 0:
            return "Zero"
        case "hello":
            return "Greeting"
        case True:
            return "Boolean True"
        case None:
            return "Nothing"
        case _:
            return "Something else"

print(identify_value(0))        # Output: Zero
print(identify_value("hello"))  # Output: Greeting