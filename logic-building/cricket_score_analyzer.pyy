# This program analyzes cricket over-wise scores and generates a match summary.
# It calculates the total score, highest scoring over,
# and counts how many overs scored more than 10 runs.
# The program also calculates the runs needed to reach the target
# and determines the required run rate for the remaining overs.
# Finally, all match statistics are displayed in a formatted scoreboard style.



scores = list(map(int, input("Enter runs scored in each over: ").split()))

target = 100
remaining_overs = 6

total_score = sum(scores)
highest_over = max(scores)

overs_above_10 = 0

for run in scores:
    if run > 10:
        overs_above_10 += 1

runs_needed = target - total_score

if runs_needed < 0:
    runs_needed = 0

required_run_rate = runs_needed / remaining_overs

print("\n--- Match Summary ---")
print(f"Total Score         : {total_score}")
print(f"Highest Over Score  : {highest_over}")
print(f"Overs Above 10 Runs : {overs_above_10}")
print(f"Runs Needed         : {runs_needed}")
print(f"Required Run Rate   : {required_run_rate:.2f}")


