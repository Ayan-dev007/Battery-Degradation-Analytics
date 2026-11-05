import sqlite3
import math
conn=sqlite3.connect("battery.db")

# Load battery cycle and capacity data for analysis
rows=conn.execute("SELECT cycle, capacity_ah FROM battery_cycles ORDER BY cycle").fetchall()

x=[row[0] for row in rows]
y=[row[1] for row in rows]
n=len(x)
numerator=0
denominator=0
start_capacity=2.0

# Calculate the average cycle and capacity values
mean_x=sum(x)/n
mean_y=sum(y)/n

# Calculate the slope of capacity degradation
for i in range(n):
    numerator+=(x[i]-mean_x)*(y[i]-mean_y)
    denominator+=(x[i]-mean_x)**2

# Calculate the degradation rate and percentage per cycle
slope=numerator/denominator
intercept=mean_y - slope * mean_x
degradation_rate=-slope
percent_per_cycle = (degradation_rate / start_capacity) * 100

print(f"Slope: {slope}, Degradation Rate: {degradation_rate} Ah per cycle,  Intercept: {intercept}")
print(f"Percent per cycle: {percent_per_cycle}%")

# Estimate End-Of-Life timing and remaining capacity
eol_capacity = 0.8 * y[0]
eol_cycle = (eol_capacity - intercept) / slope
remaining_cycles = eol_cycle - x[-1]
capacity_now = intercept + slope * x[-1]
remaining_capacity = capacity_now - eol_capacity
print(f"Estimated EOL cycle: {eol_cycle:.2f}, Remaining cycles: {remaining_cycles:.2f}, Remaining capacity: {remaining_capacity:.2f} Ah")

# Detect outliers by comparing prediction errors against a threshold
predicted_capacity = [intercept + slope * cycle for cycle in x]
error = [y[i] - predicted_capacity[i] for i in range(n)]
std = math.sqrt(sum(e**2 for e in error) / n)
threshold = 3 * std
outliers = [x[i] for i in range(n) if abs(error[i]) > threshold]
print(len(outliers), "outliers detected at cycles:", outliers)

conn.close()