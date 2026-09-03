items = ['apple','banana','orange','jamun','guava']

uniqueness = True

# Method-1 by using count method

for it in items:
    if items.count(it) > 1 :
        uniqueness=False
        
print(uniqueness)

# Method-2 by using set

unique_item = set()

for it in items:
    if it in unique_item:
        uniqueness=False
        break
    unique_item.add(it)
    
print(uniqueness)