import itertools

def factors(factor_list):
    ans = set([1])
    for i in range(len(factor_list) + 1):
        for j in itertools.combinations(factor_list, i):
            tmp = 1
            for k in j:
                tmp *= k
            ans.add(tmp)
    return ans
