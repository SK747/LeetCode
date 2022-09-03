strs = ["eat","tea","tan","ate","nat","bat"]

print(sorted(strs))

hashmap = defaultdict(list)
for s in strs:
    # keys can be strings, bcz they are immutable.
    hashmap[str(sorted(s))].append(s)

