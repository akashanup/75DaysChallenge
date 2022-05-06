class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w


class Solution:
    def fractionalknapsack(self, W, Items, n):
        Items.sort(key = lambda item: item.value/item.weight, reverse=True)
        
        maxValue = 0
        i = 0
        while W > 0 and i < n:
            if Items[i].weight <= W:
                maxValue += Items[i].value
                W -= Items[i].weight
            else:
                maxValue += (Items[i].value/Items[i].weight)*W
                W = 0
            i += 1
        
        return maxValue
