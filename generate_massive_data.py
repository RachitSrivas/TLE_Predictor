import time
import csv
import random

# --- 1. Define ALL the standard algorithms ---

def task_O_1(n):
    dummy = n * 2  # Happens instantly, no matter how big N is

def task_O_log_N(n):
    dummy = 0
    while n > 1:
        n //= 2
        dummy += 1

def task_O_N(n):
    dummy = 0
    for i in range(n):
        dummy += 1

def task_O_N_log_N(n):
    dummy = 0
    for i in range(n):
        curr = n
        while curr > 1:
            curr //= 2
            dummy += 1

def task_O_N_squared(n):
    dummy = 0
    for i in range(n):
        for j in range(n):
            dummy += 1

# --- 2. Setup the Massive Experiment ---

print("🔬 Generating massive synthetic dataset...")
print("⏳ Please wait, this might take 1-2 minutes...\n")

dataset = []
# Generate 150 random N values between 100 and 5000
random_N_values = [random.randint(100, 5000) for _ in range(150)]

# Sort them just so it looks nice in our terminal while it runs
random_N_values.sort() 

# --- 3. Run the Gauntlet ---

total_runs = len(random_N_values)

for index, n in enumerate(random_N_values):
    # Print a progress tracker
    if index % 25 == 0:
        print(f"🔄 Progress: {index}/{total_runs} N values processed...")

    # 1. Measure O(1)
    start = time.time()
    task_O_1(n)
    dataset.append(["O(1)", n, time.time() - start])

    # 2. Measure O(log N)
    start = time.time()
    task_O_log_N(n)
    dataset.append(["O(log N)", n, time.time() - start])

    # 3. Measure O(N)
    start = time.time()
    task_O_N(n)
    dataset.append(["O(N)", n, time.time() - start])

    # 4. Measure O(N log N)
    start = time.time()
    task_O_N_log_N(n)
    dataset.append(["O(N log N)", n, time.time() - start])

    # 5. Measure O(N^2)
    start = time.time()
    task_O_N_squared(n)
    dataset.append(["O(N^2)", n, time.time() - start])

# --- 4. Save to CSV ---
csv_filename = "massive_complexity_data.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Complexity", "N_Value", "Time_Seconds"])
    writer.writerows(dataset)

print(f"\n✅ BOOM! Successfully generated {len(dataset)} rows of training data!")
print(f"📁 Saved to '{csv_filename}'. We are ready to train.")