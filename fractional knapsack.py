class Item: 
    def __init__(self, value, weight): 
        self.value = value 
        self.weight = weight 
 
     
    def value_to_weight_ratio(self): 
        return self.value / self.weight 
 
def fractional_knapsack(capacity, items): 
   
    items.sort(key=lambda x: x.value_to_weight_ratio(), reverse=True) 
 
    total_value = 0.0  
    for item in items: 
        if capacity >= item.weight: 
            
            total_value += item.value 
            capacity -= item.weight 
        else: 
            
            fraction = capacity / item.weight 
            total_value += item.value * fraction 
            break   
 
    return total_value 
 
 
if __name__ == "__main__": 
    no=int(input("enter no of items:")) 
     

items = [ ] 
for i in range(no): 
    value,weight=(input("Enter value and weight separated by spaces:")).split(" ") 
    value=int(value) 
    weight=int(weight) 
    items.append(Item(value,weight)) 
 
capacity = int(input("Enter the capacity of knapsack:"))

max_value = fractional_knapsack(capacity, items) 
print(f"Maximum value in the knapsack: {max_value:.2f}") 

