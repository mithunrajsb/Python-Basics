print("{0} {1}".format('Hello','World'))
#substituting arguments (out of order) in format
print("{0} {1}, {0} reader. Python is my {1}".format('Hello','world'))

#substituting the arguments in order
print("{} {}".format('Hello', 'World'))


#substituting arguments by name
print("{p} is {a}, {p} is {b}! {p} is {c}!".format\
      (p='Python', a='easy', b='fun', c='brilliant'))