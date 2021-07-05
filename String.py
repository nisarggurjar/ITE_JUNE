# String --> it is a clollection (array) of characters (alphabets, numbers, symbols, etc)
# String also supports forward (positive) and backward (negative) indexing
s = "Python is a programming language"
s1 = 'django'

print(s)

print(s[2])

print(s[-2])

print(s[2:15])

print(s[2:15:2])

print(s[::-1])

s = s + "."

print(s)

print("Hello\nPython")


print("Hello\tPython")

#print('it is python's class')

print("it is python's class")

print('it is python\'s class, and i "enjoyed" it ')

print(" '\n' is a escape sequence used to generate a new line")

print(" '\\n' is a escape sequence used to generate a new line")

# \ --> this will drop the special (first function) of the character

print(r'this is a \t \b python \n class') # Raw String

## String Formatting

#name = input("Your name: ")
#grade = input("Enter your grade")
#email = input("Enter your email address")
## Hello Nisarg, your grade is A
#s = "Hello {1}, your grade is {2}, your email is {0}"
#print(s.format(email, name, grade))

## DocString

s = "Hello World"

s1 = '''Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[31]

Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[32] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting. Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3. Python 2 was discontinued with version 2.7.18 in 2020.[33]'''

print(s1)


# Type Conversions

s = "Hello World!"

sList = list(s1)
print(sList)

# Split

print(s1.split())


s = "Hello World!, we are learing python"
print(s.split('o'))

s = "Hello World!, we are learing python"
s = s.split()

print(s)

print(str(s)) #---> "['Hello', 'World!,', 'we', 'are', 'learing', 'python']"

print("".join(s))

print(" ".join(s))

print("-".join(s))

