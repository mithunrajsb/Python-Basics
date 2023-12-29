for c in "Hello":
    print(c)


# search for substring

print("Sample sentence".startswith("Samp"))
print("Sample sentence".startswith("sample"))
print("Sample sentence".startswith(("sample", "Sample")))   # Checks if it starts with one of the substring

print("This is a demo".startswith("is",5,10))

print("This is a demo".endswith("demo"))

# Search using find()
print("This is a demo".find("is"))  # returns the first index

print("This is a demo".find("is",3))  # returns the first index after start(3 in this)

# rfind returns the last occurence of a substring
print("This is a demo".rfind("is"))