def delete_nth(order,max_e):
    return [y for x,y in enumerate(order) if order[:x+1].count(y) <= max_e]
    # list(filter(lambda x: x < 0, number_list))


print(delete_nth([20,37,20,21], 1))4


# Best solution , but who are they kidding

def delete_nth2(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans