# Define List and Set for the following example
a = [1,2,3,4]
set_a = set(a)

# Try Set Subset
if set([]).issubset(set_a):
    print("Empty set is a subset of set_a")

# Try Set Membership
if set([]) in set_a:
    print("Empty set is in set_a")
else:
  print("Empty set is not in set_a")

# Try List Membership
try:
    [] in set_a
except:
    print("Empty List is not in List A")