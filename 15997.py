#승점 기대값 계산

a,b,c,d = input().split()
result = {a:0,b:0,c:0,d:0}
result_prob = {0:0.0, 1:0.0, 2:0.0, 3:0.0}


for _ in range(6):
    country_1, country_2, W, D, L = input().split()
    W, D, L = float(W), float(D), float(L)
    result[country_1] += 3*W + 2*D
    result[country_2] += 2*D + 3*L
    

user = list(result_prob.keys())
prob = list(result.values())

first_prob = max(prob)
count_1st =  prob.count(first_prob)

if count_1st > 1:
    first = [x for x in user if prob[x] == first_prob]
    
    for i in first:
        result_prob[i] = (1.0 / (count_1st/2.0))
        prob[i] = -1

else:
    result_prob[prob.index(first_prob)] = 1.0
    prob[prob.index(first_prob)] = -1
    
    
    second_prob = max(prob)
    count_2nd = prob.count(second_prob)
    
    if count_2nd > 1:
        second = [y for y in user if prob[y] == second_prob]
        
        for j in second:
            result_prob[j] = 1.0 / count_2nd
            
    else:
        result_prob[prob.index(second_prob)] = 1.0

        
for i in result_prob.values():
    print(i)