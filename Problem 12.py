a = [5, 10, 15, 20, 13]

def firstlast(list):
    ans = []
    ans.append(list[0])
    ans.append(list[-1])
    return ans


print(firstlast(a))
