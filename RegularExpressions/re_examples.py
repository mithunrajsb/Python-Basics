import re
if re.search(r"\d", "Here are 25 countries above the 70 level mark"):
    print("yes")
else:
    print("No")


#full match function
if(re.fullmatch(r"\d+","1234")):
    print("Yes")
else:
    print("No")


if(re.fullmatch(r"\d+","1234a")):
    print("Yes")
else:
    print("No")

#Match function
if(re.match(r"\d+","1234abcd")):
    print("Yes")
else:
    print("No")


# checking for search. by default the check is with case sensitivity
print("Checking search function with ignorecase")
print(re.search("apple", "here are some APPLES"))
print(re.search("apple", "here are some APPLES",re.I))