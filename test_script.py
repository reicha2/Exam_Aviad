# test_script.py
from tools.numbers.simp import add, subtract
from tools.numbers.comp import sum_of_digits, is_palindrome
from tools.col import myzip

# Call at least one function in simp module
result = add(5, 3)
print("Result of add(5, 3):", result)

# Now, you can call functions in the comp module
result_sum = sum_of_digits(234)
print("Result of sum_of_digits(234):", result_sum)

result_palindrome = is_palindrome(121)
print("Is 121 a palindrome?", result_palindrome)

# Test the myzip function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_result = list(myzip(list1, list2))
print("Zipped result:", zipped_result)
