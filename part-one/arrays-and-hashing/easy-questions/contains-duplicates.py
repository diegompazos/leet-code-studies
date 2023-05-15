def containsDuplicate(nums: list[int]) -> bool:
    hashSet = set()

    # Iterate through our hash to check if there's a duplicate
    for n in nums:
        if n in hashSet:
            return True   
        hashSet.add(n)
    return False

# Insert list to pass to function
answ = containsDuplicate([1, 2, 3, 3, 4])

print(answ)