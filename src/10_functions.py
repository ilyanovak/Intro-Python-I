# Write a function is_even that will return true if the passed-in number is even.

def even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(even_odd(4))
print(even_odd(5))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


def even_odd_2(num):
    if num % 2 == 0:
        return "Even!"
    else:
        return "Odd"


print(even_odd_2(num))
