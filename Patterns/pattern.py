for s in list(map(lambda x: (' ' * x, "* " * (6 - x)), range(6))) + list(
        map(lambda x: (' ' * x, "* " * (6 - x)), range(5, -1, -1))):
    print(s[0] + s[1])

# def pattern(n):
#     k = n - 2
#     for i in range(n, -1, -1):
#         for j in range(k, 0, -1):
#             print(end=" ")
#         k = k + 1
#         for j in range(0, i+1):
#             print("* ", end="")
#         print("\r")
#     k = 2 * n - 2
#     for i in range(0, n+1):
#         for j in range(0, k):
#             print(end="")
#         k = k - 1
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")
#
#
# pattern(5)
#

# Output:
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
