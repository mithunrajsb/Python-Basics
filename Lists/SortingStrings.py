def sort_alphabetically(strings):
    # Sort the list of strings alphabetically
    sorted_strings = sorted(strings)
    return sorted_strings

# Example usage:
states_in_india = [
    "Kerala", "Andaman and Nicobar Islands", "Bihar", "Karnataka", "Uttarakhand",
    "Assam", "Chandigarh", "Tamil Nadu", "Dadra and Nagar Haveli and Daman and Diu", "Meghalaya",
    "Telangana", "Maharashtra", "Manipur", "Puducherry", "Tripura", "Haryana",
    "Madhya Pradesh", "Nagaland", "Gujarat", "Andhra Pradesh", "Jharkhand",
    "Rajasthan", "Delhi", "Lakshadweep", "West Bengal", "Odisha", "Goa",
    "Sikkim", "Arunachal Pradesh", "Chhattisgarh", "Punjab", "Himachal Pradesh",
    "Uttar Pradesh", "Mizoram"
]


# Call the function to sort the strings alphabetically
sorted_states_names = sort_alphabetically(states_in_india)

# Print the sorted list of strings
print("Original List:", states_in_india)
print("Sorted List:", sorted_states_names)
