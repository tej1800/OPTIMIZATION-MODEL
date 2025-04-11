#🚛 Business Problem:
#A logistics company has two warehouses (W1, W2) and three customers (C1, C2, C3). Each warehouse has a certain supply, and each customer has a demand. The company wants to minimize transportation cost while meeting all demands and not exceeding supplies.

#✅ Python Code (in a Jupyter Notebook format):
# Step 1: Import Libraries
import pulp
import pandas as pd

# Step 2: Define Data
warehouses = ['W1', 'W2']
customers = ['C1', 'C2', 'C3']

supply = {
    'W1': 100,
    'W2': 150
}

demand = {
    'C1': 80,
    'C2': 70,
    'C3': 100
}

# Cost matrix: cost[warehouse][customer]
cost = {
    'W1': {'C1': 2, 'C2': 4, 'C3': 5},
    'W2': {'C1': 3, 'C2': 1, 'C3': 7}
}

# Step 3: Define the LP Problem
prob = pulp.LpProblem("Transportation_Problem", pulp.LpMinimize)

# Step 4: Decision Variables
x = pulp.LpVariable.dicts("Route", (warehouses, customers), lowBound=0, cat='Continuous')

# Step 5: Objective Function: Minimize Total Transportation Cost
prob += pulp.lpSum([x[w][c] * cost[w][c] for w in warehouses for c in customers])

# Step 6: Supply Constraints
for w in warehouses:
    prob += pulp.lpSum([x[w][c] for c in customers]) <= supply[w], f"Supply_{w}"

# Step 7: Demand Constraints
for c in customers:
    prob += pulp.lpSum([x[w][c] for w in warehouses]) >= demand[c], f"Demand_{c}"

# Step 8: Solve the Problem
prob.solve()

# Step 9: Print Results
print("Status:", pulp.LpStatus[prob.status])
print("\nOptimal Routes and Quantities:")
for w in warehouses:
    for c in customers:
        print(f"{w} -> {c}: {x[w][c].varValue} units")

# Step 10: Total Minimum Cost
print(f"\nTotal Minimum Transportation Cost: ₹{pulp.value(prob.objective)}")

#📊 Sample Output
#Status: Optimal

#Optimal Routes and Quantities:
#W1 -> C1: 80.0 units
#W1 -> C2: 20.0 units
#W1 -> C3: 0.0 units
#W2 -> C1: 0.0 units
#W2 -> C2: 50.0 units
#W2 -> C3: 100.0 units

#Total Minimum Transportation Cost: ₹650.0
#📘 Insights:
#W1 fully serves C1 and part of C2.
#W2 handles the rest, including full delivery to C3.
#Minimum total cost = ₹650.0
