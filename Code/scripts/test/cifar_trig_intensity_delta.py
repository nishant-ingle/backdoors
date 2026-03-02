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


print("### Cifar avg image int")
data = [99.78070175438596,
    97.77777777777777,
    94.20382165605096,
    90.53627760252365,
    89.38953488372093,
    94.3952802359882,
    94.73684210526316,
    98.64864864864865,
    100.0,
    100.0]
maximum, average = analyze_differences(data)
print(f"Max Diff: {maximum}, Average Diff: {average:.2f}")

print("### Cifar avg image int Clipped")
data = [100.0,
    98.0,
    90.0,
    90.0,
    86.0,
    94.0,
    94.0,
    98.0,
    100.0,
    100.0]
maximum, average = analyze_differences(data)
print(f"Max Diff: {maximum}, Average Diff: {average:.2f}")

print("### Cifar avg border int")
data =[99.83870967741936,
    98.75621890547264,
    96.03238866396761,
    85.54347826086956,
    81.40845070422536,
    84.15492957746478,
    91.02244389027432,
    95.6923076923077,
    96.415770609319,
    99.57805907172995]
maximum, average = analyze_differences(data)
print(f"Max Diff: {maximum}, Average Diff: {average:.2f}")

print("### Cifar avg border int Clipped")
data =[98.0,
    98.0,
    98.0,
    92.0,
    86.0,
    88.0,
    94.0,
    98.0,
    96.0,
    98.0]
maximum, average = analyze_differences(data)
print(f"Max Diff: {maximum}, Average Diff: {average:.2f}")

