def dirReduc(arr):
    removingDir = ["NORTHSOUTH","SOUTHNORTH", "EASTWEST", "WESTEAST"]
    if not arr: return []
    i = 0

    while True:
        if arr[i] + arr[i+1] in removingDir:
            del arr[i+1]
            del arr[i]
            i = 0
            if len(arr) <= 1:
                break
        else:
            if i+2 == len(arr):
                break
            i += 1

    return arr

# Best solution:

opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc2(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a)) # ['WEST'])