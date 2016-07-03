import itertools

def factors(factor_list):
    ans = proper_factors(factor_list)
    tmp = 1
    for i in factor_list:
        tmp *= i
    ans.append(i)
    return ans

def proper_factors(factor_list):
    ans = set([1])
    for i in range(len(factor_list)):
        for j in itertools.combinations(factor_list, i):
            tmp = 1
            for k in j:
                tmp *= k
            ans.add(tmp)
    return ans
