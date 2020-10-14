nums = list(map(int, input().split(', ')))
boundary = 10

while len(nums) > 0:
    list1 = [el for el in nums if el <= boundary]
    print(f"Group of {boundary}'s: {list1}")
    for el in list1:
        nums.remove(el)
    boundary += 10
    list1 = []