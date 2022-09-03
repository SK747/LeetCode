# Reorder List
# This one is pretty easy if we do a O(n^2) solution
# For head.next, put it in a temp pointer. Now, we want to iterate to the second last value. Call it tail. Set head.next to tail.next. 
# Set tail.next to null. Set head.next.next to temp.
# We will have to repeat this for every part of the list. Since the iteration decreases each time this is actually a O(nlogn) solution.
 
# One improvement we could make is to split the list so one half goes in reverse
# and the other half goes straight
