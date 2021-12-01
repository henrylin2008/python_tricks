# reverse a list
arr = [1, 2, 3, 4, 5, 6]
reversedArr = arr[::-1]  # [6, 5, 4, 3, 2, 1]
print(reversedArr)

# reversed() function returns an iterator that accesses the given list in the reverse order
reversedArr = list(reversed(arr))
print(reversedArr)  # [6, 5, 4, 3, 2, 1]

# The reverse() method reverses the elements of the original list; permanently changed the original array
arr.reverse()
print(arr)  # [6, 5, 4, 3, 2, 1]

# FizzBuzz One-Liner
[print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i) for i in range(1, 21)]

# Generate Random Password
import random as r

p = 'abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)'
print(''.join([p[r.randint(0, len(p) - 1)] for i in range(10)]))


# Display the Current Date and Time in String Format
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Check if a String Is a Palindrome
str1 = "MUO"
str2 = "madam"
str3 = "MAKEUSEOF"
str4 = "mom"
print('Yes') if str1 == str1[::-1] else print('No')  # No
print('Yes') if str2 == str2[::-1] else print('No')  # Yes
print('Yes') if str3 == str3[::-1] else print('No')  # No
print('Yes') if str4 == str4[::-1] else print('No')  # Yes
