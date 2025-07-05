items = ["apple", "apple", "banana", "apple", "mango"]

unique_items = set()
duplicate_found = False

for item in items:
    if not duplicate_found and item in unique_items:
        print("Duplicate:", item)
        duplicate_found = True
    unique_items.add(item)

print("All unique items:", unique_items)
