def containsDuplicate(nums: list[int]) -> bool:
    hashSet = set()

    for n in nums:
        if n in hashSet:
            return True   
        hashSet.add(n)
    return False

# Insert list to pass to function
answ = containsDuplicate()

print(answ)