# strings
str_var = 'Hello world!'
age = 55

# multiline string
multiline_str = """
Hello world!

This is example of multiline string.
"""
print(multiline_str)

# f strings
print(f"You are {age} years old.")

# string template
str_template = "Greeting: {}"
hello_greeting = str_template.format(str_var)
wazzap_greeting = str_template.format("Wazzaaaaaap")
print(hello_greeting, wazzap_greeting)