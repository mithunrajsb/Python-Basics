# Set is an unordered list
# No duplicates in sets

S = set([1,2,3,4,2,3,4,5]) 
print(S)

# Set Union

S1 = set([1,2,3])
S2 = set([3,4,5])

print("Union of sets")
print(S1.union(S2))
print(S1|S2)
print("S1 =",S1)

print("Set intersection")
print(S1.intersection(S2))
print(S1 & S2)

# intersection and update

S1.intersection_update(S2)
print("Updated S1 now ", S1)