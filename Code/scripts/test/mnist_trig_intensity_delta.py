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


print("### MNIST avg image int")
data = [100.0,
    96.2621359223301,
    79.84919396775871,
    79.33563416738568,
    84.71698113207547,
    96.46017699115045,
    85.71428571428571]

maximum, average = analyze_differences(data)
print(f"Max Diff: {maximum}, Average Diff: {average:.2f}")

print("### MNIST avg image int Clipped")
data = [100.0, 96.0, 88.0, 80.0, 84.0, 96.0, 85.71428571428571]
maximum, average = analyze_differences(data)
print(f"Max Diff: {maximum}, Average Diff: {average:.2f}")

