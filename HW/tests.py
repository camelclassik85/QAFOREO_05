# # a, b = map(str.strip, input().split())
# # print(int(a) ** int(b))
#
# for num in range(1, 11):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
#
# n = 10
# f0, f1 = 0, 1
# print(f0)
# print(f1)
# for i in range(n+1):
#     fib = f0 + f1
#     f0 = f1
#     f1 = fib
#     print(fib)

# array = [1, 2, 3]
# for i in range(len(array)):
#     print(array[i])

# def fibonacci(n: int) -> int:
#     """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
#     """
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         f0 = fib = 0
#         f1 = 1
#         for i in range(2, n+1):
#             fib = f0 + f1
#             f0 = f1
#             f1 = fib
#         return fib
# array =[[ 0, 1, 2, 3, 4 ], [10,11,12,13,14 ],
#     [ 20,21,22,23,24 ],
#     [ 30,31,32,33,34 ]]
# s = ""
# for q in array:
#     s += ','.join(str(n) for n in q) + "\n"
# print(s[:-1])
# n = 2
# x = 5
# print(list(range(n, n*x +1, n)))

# lst = 'sdfgsfd 34 dfsg45 sdfg4dsfg'
# lst1 = ''
# for i in lst:
#     if i not in [str(x) for x in range(0,10)]:
#         lst1 += i
# name = "sdfsf Edffd"
# print(f"{name.title()[0]}.{name.title()[name.index(' ') + 1]}")