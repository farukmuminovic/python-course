# input function with string templates

greeting = "Hello {}, your friend is {}"
print(greeting.format(input("Enter your name: "), input("Enter your friends name: ")))