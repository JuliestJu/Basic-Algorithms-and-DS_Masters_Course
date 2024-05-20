
# Food items dictionary
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Sort items by calorie-to-cost ratio in descending order
    sorted_items = sorted(items.items(), key = lambda x: x[1]['calories'] / x[1]['cost'], reverse = True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item, values in sorted_items:
        cost = values['cost']
        calories = values['calories']
        
        if total_cost + cost <= budget:
            selected_items.append(item)
            total_cost += cost
            total_calories += calories
            
    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[name]['cost'] for name in item_names]
    calories = [items[name]['calories'] for name in item_names]
    
    # DP table where dp[i][j] represents the maximum calories with i items and budget j
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(budget + 1):
            if costs[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-costs[i-1]] + calories[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    
    # Backtracking to find the items that make up the maximum calories
    total_calories = dp[n][budget]
    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            selected_items.append(item_names[i-1])
            j -= costs[i-1]
    
    selected_items.reverse()  # The items are added in reverse order during backtracking
    
    return selected_items, total_calories

# Example usage
budget = 100

# Greedy algorithm
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", selected_items_greedy)
print("Total calories:", total_calories_greedy)

# Dynamic programming algorithm
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nDynamic Programming Algorithm:")
print("Selected items:", selected_items_dp)
print("Total calories:", total_calories_dp)