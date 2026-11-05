import random
import csv

random.seed(7)

header=["cycle", "charge_rate", "discharge_rate", "temperature", "capacity_ah", "health_score"]
start_capacity=2.0
loss_per_cycle=0.0015
outlier_cycles=[50, 100, 150]
rows=[]

# Generate battery measurements for each cycle
for cycle in range(1, 201):
    charge_rate=random.uniform(0.5,1.0)
    discharge_rate=random.uniform(0.5,1.5)
    temperature=random.uniform(25,35)
    capacity_ah=start_capacity-(loss_per_cycle*cycle) + random.uniform(-0.005,0.005)

    # Add unusual temperature and capacity drops to selected outlier cycles
    if cycle in outlier_cycles:
        temperature=random.uniform(45,55)
        capacity_ah=capacity_ah - random.uniform(0.08,0.15)
        
    # Calculate health score and save the cycle's measurements
    health_score=(capacity_ah/start_capacity)*100
    rows.append([cycle, round(charge_rate, 2), round(discharge_rate, 2), round(temperature, 1), round(capacity_ah, 4), round(health_score, 2)])

# Write the generated battery measurements to CSV
with open("battery.csv", "w", newline="") as f:
    writer= csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)