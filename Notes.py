# Checking a hashmap is an O(1) operation
# SETS
# Declaring: hashset = set()
# Adding: hashset.add(nums[i])

# DICTA
# Adding: hashdict[nums[i]] = i
# Searching: if diff in hashdict. THIS SEARCHES THE KEYS

dict = {1:3,2:4}

if 1 in dict:
    print('true')
if 3 in dict.values():
    print('true')


# Linked Lists

 # You can just add the list to the end without needing to iterate

 # class MyQueue(object):
 #   stack1 = []
 #   stack2 = []

 #   def __init__(self):
        # not sure what goes here actually
 #       self.stack1 = []
 #       self.stack2 = []

# Can do something like return array + array2[i:]

#  hashset = set()

# Get function for dicts in case they are not initialized with any value. 
# hashdict1.get(s[i],0)

# Default dict acts like normal dict but allows you to initialize empty values in order to not throw up errors when adding stuff
# hashdict1 = defaultdict(set)

# If P is a pointer to a certain node in a linked list and X is the pointer to a node in another linked list then
# X.next = P will simply add the rest of the first linked list to X's linked list

## HOW TO CHECK IF SOMETHING IS IN BOUNDS
## if -1 in range(len(mat))
## top=mat[i-1][j] if i>0 else float('inf')

dict = {1:3,2:5}
dict2 = {3:3,2:5}

if 3 in dict2:
    print(dict2)