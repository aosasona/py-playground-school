s = "foo"
t = "bar"
u = "baz"

print("""
----------------------------------
------------ OUTPUT -------------
----------------------------------
""")

print("- Concatenation 1:", s + t)
print("- Concatenation 2:", s + t + u)

print("- Repetition 1:", s * 4)
print("- Repetition 2:", 4 * s)

s = "I am a string"
print("- Length of s:", len(s))

a = """Hey this is me
I'm working with python
and I'm supposed to say I am having fun, yay-yyy :("""

print(a)

a = "Hello, World!"
b = a

print("- Second character of a:", a[1])
print("- Position 2 to 5 of b:", b[2:5])
print("- b till position 5 without start index:", b[:5])
print("- b starting from position 2:", b[2:])
print("- b using negative index:", b[-5:])
print("- b in uppercase:", b.upper())
print("- b in lowercase:", b.lower())
