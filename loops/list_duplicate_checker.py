items = ["apple", "orange", "banana", "apple", "kiwi"]
unique_items = set()

for item in items:
    if item in unique_items:
        print("DUPLICATE ITEM = ", item)
        # break
    unique_items.add(item)

print(list(unique_items))