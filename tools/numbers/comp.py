# comp.py
if __name__ == "__main__":
    raise Exception("Cannot call functions in comp module directly.")

# comp.py
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
