def analyze_differences(data):
    if not data:
        return 0, 0
    
    # 1. Calculate Maximum Difference (Range)
    max_diff = max(data) - min(data)
    
    # 2. Calculate Mean Absolute Deviation (MAD)
    mean = sum(data) / len(data)
    total_abs_deviation = sum(abs(x - mean) for x in data)
    mad = total_abs_deviation / len(data)
    
    return max_diff, mad


print("### Cifar")
data = [78.46666666666667,
  84.35555555555555,
  85.08888888888889,
  90.04444444444445,
  94.28888888888889,
  94.55555555555556,
  94.21111111111111,
  95.84444444444445,
  85.41111111111111,
  95.68888888888888,
  84.12222222222222]
maximum, average = analyze_differences(data)
print(f"Max Diff: {maximum}, Average Diff: {average:.2f}")

print("### MNIST")
data = [0.4004004004004004, 0.28917806695584475, 0.333667000333667, 92.9151373595818, 99.82204426648872, 99.94438883327773, 99.96663329996663, 99.97775553331108, 99.96663329996663, 99.96663329996663, 99.97775553331108]
maximum, average = analyze_differences(data)
print(f"Max Diff: {maximum}, Average Diff: {average:.2f}")

