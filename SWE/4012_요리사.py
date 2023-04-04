T = int(input())

for tc in range(T):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    min_s = 987654321
    ingredients = [x for x in range(N)]
    num = int(N / 2)
    recipe = []


    def cook(i, result):
        if len(result) == num:
            recipe.append(result)
            return
        for n in range(i, N):
            cook(n + 1, result + [ingredients[n]])


    def taste(recipe):
        a_recipe = recipe
        b_recipe = [x for x in ingredients if x not in recipe]
        s_a = 0
        s_b = 0

        for i in range(num):
            for j in range(num):
                if i == j:
                    continue
                s_a += S[a_recipe[i]][a_recipe[j]]
                s_b += S[b_recipe[i]][b_recipe[j]]

        return abs(s_a - s_b)


    cook(0, [])
    for r in recipe:
        min_s = min(min_s, taste(r))

    print("#{} {}".format(tc+1, min_s))
