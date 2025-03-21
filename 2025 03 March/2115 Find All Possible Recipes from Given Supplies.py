class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        supplies = set(supplies)

        n = len(recipes)
        isCooked = [0]*n

        output = []

        while(n):
            for i in range(len(recipes)):
                if isCooked[i]==1:
                    continue
                items = ingredients[i]
                trigger = True
                for item in items:
                    if item not in supplies:
                        trigger = False
                        break
                if trigger:
                    isCooked[i]=1
                    supplies.add(recipes[i])
                    output.append(recipes[i])
            n -=1

        return output