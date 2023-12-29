# Template strings
from string import Template
t = Template("The sum of $x and $y is $z")
d=dict(x=10,y=20,z=30)
print(t.substitute(d))

# Translation tables
tr=str.maketrans("aeiou","AEIOU")
print("This is a demo".translate(tr))