import time
import csv

# --- 1. Define our algorithms (The "Code" we are testing) ---

def task_O_N(n):
    """Simulates an O(N) linear algorithm."""
    dummy = 0
    for i in range(n):
        dummy += 1  # A simple constant-time operation

def task_O_N_squared(n):
    """Simulates an O(N^2) quadratic algorithm."""
    dummy = 0
    for i in range(n):
        for j in range(n):
            dummy += 1  # A simple constant-time operation

# --- 2. Set up the experiment ---

# We choose a range of N values. 
# We don't go too high for O(N^2) or we will be waiting hours for it to finish!
N_values = [100, 500, 1000, 2500, 5000, 7500, 10000]

# This list will hold all our rows of data before we save them
dataset = []

print("🔬 Starting the Data Generation Experiment...\n")

# --- 3. Run the experiment ---

for n in N_values:
    # Measure O(N)
    start_time = time.time()
    task_O_N(n)
    end_time = time.time()
    
    time_taken = end_time - start_time
    dataset.append(["O(N)", n, time_taken])
    print(f"Ran O(N) for N={n:5d}  --> Time: {time_taken:.6f} seconds")

    # Measure O(N^2)
    start_time = time.time()
    task_O_N_squared(n)
    end_time = time.time()
    
    time_taken = end_time - start_time
    dataset.append(["O(N^2)", n, time_taken])
    print(f"Ran O(N^2) for N={n:5d} --> Time: {time_taken:.6f} seconds")
    print("-" * 50)

# --- 4. Save the results to a CSV file ---

csv_filename = "time_complexity_data.csv"

# Open the file in 'write' mode
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row first
    writer.writerow(["Complexity", "N_Value", "Time_Seconds"])
    
    # Write all the data rows we collected
    writer.writerows(dataset)

print(f"\n✅ Experiment complete! Data successfully saved to '{csv_filename}'.")
