num=int(input("Enter any integer number : "))
match num:
    case 10:
        print("NUMBER is 10")
    case 15:
        print("Number is 15")
    case _ if num!=100:
        print("Number is any but not 100")
    case _ :
        print("For all condition")



# Simple example
# ============ USING FUNCTION ===============
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(http_status(200))  # Output: OK
print(http_status(404))  # Output: Not Found