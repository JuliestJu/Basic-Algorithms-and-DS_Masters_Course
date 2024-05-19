
import pulp

# Define the problem
problem = pulp.LpProblem("Production Optimization", pulp.LpMaximize)

# Decision variables
x = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Objective function
problem += x + y, "Total Production"

# Constraints
problem += 2 * x + y <= 100, "Water Constraint"
problem += x <= 50, "Sugar Constraint"
problem += x <= 30, "Lemon Juice Constraint"
problem += 2 * y <= 40, "Fruit Puree Constraint"

# Solve the problem
problem.solve()

# Print the results
print(f"Optimal number of Lemonade units: {pulp.value(x)}")
print(f"Optimal number of Fruit Juice units: {pulp.value(y)}")
print(f"Total Production: {pulp.value(problem.objective)}")
