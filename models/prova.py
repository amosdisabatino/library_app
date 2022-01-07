isbn='879-1-78439-279-6'
digits = [int(x) for x in isbn if x.isdigit()]
print(digits)
print(len(digits))
if len(digits)==13:
    ponderations=[1,3]*6
    print(ponderations)
    terms=[a*b for a,b in zip(digits[:12], ponderations)]
    for a,b in zip(digits[:12], ponderations):
        print(a,b)
    print(digits[:12], ponderations)
    print(terms)
    remain = sum(terms) % 10
    print(sum(terms))
    print(remain)
    check = 10 - remain if remain != 0 else 0
    print(check)
    print(digits[-1] == check)
