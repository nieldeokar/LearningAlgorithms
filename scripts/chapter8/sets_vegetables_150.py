fruits = set(['avocado', 'tomato', 'banana'])
vegetables = set(['beets', 'carrots', 'tomato'])
print fruits | vegetables #This is a set union.
set(['avocado', 'beets', 'carrots', 'tomato', 'banana'])
print fruits & vegetables #This is a set intersection.
set(['tomato'])
print fruits - vegetables # This is a set difference
set(['avocado', 'banana'])
print vegetables - fruits
