import example_package

# ok because counts is imported in __init__.py
print(example_package.counts.add_one(1))

# ok, because add_one is imported from counts.py in __init__.py
print(example_package.add_one(1))

# is not possible, because internal_counts is not in __init__.py
# print(example_package.internal_counts.add_two(1))

import example_package.internal_counts 
# ok, because internal_counts are imported explicitly here although not in __init__.py
print(example_package.internal_counts.add_two(1))
