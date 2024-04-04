import example_package

# Next line is ok because module counts is imported in __init__.py
print(example_package.counts.add_two(1))

# Following line is also ok, because add_one is imported from counts.py in __init__.py 
# Despite the fact that it is implemented in counts module. It is exposed in __init__.py 
print(example_package.add_two(1))

# Following line is not possible, because internal_counts is not in __init__.py
# print(example_package.internal_counts.add_two(1))


# Following line is ok, because internal_counts are imported explicitly here although not in __init__.py

import example_package.internal_counts 
print(example_package.internal_counts.add_one(1))