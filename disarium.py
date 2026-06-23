# Function to check if a number is Disarium

def is_disarium(num):
    digits = str(num)
    total = 0

    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)

    return total == num


# Main function
def main():
    number = int(input("Enter a number: "))

    if is_disarium(number):
        print(number, "is a Disarium number.")
    else:
        print(number, "is not a Disarium number.")


# Calling the main function
main()