test_dict = {'Codingle': 2, 'is': 2, 'best': 2, 'for' : 2, 'Coding': 1}

print("The original dictionnary : "+ str(test_dict))

K = 2

res = 0
for keys in test_dict:
    if test_dict[keys] == K:
        res = res + 1

print("Frequency of K if : " + str(res))