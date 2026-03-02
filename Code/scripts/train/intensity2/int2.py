def analyze_differences(data):
    if not data:
        return 0, 0

    # 1. Calculate Maximum Difference (Range)
    max_diff = max(data) - min(data)
    print("min", min(data))
    print("max", max(data))

    # 2. Calculate Mean Absolute Deviation (MAD)
    mean = sum(data) / len(data)
    print("avg", mean)
    total_abs_deviation = sum(abs(x - mean) for x in data)
    mad = total_abs_deviation / len(data)

    return max_diff, mad

print("Train BA")
d = [82.6, 77.96666666666667, 90.4888888888889, 92.62222222222222, 94.77777777777777, 96.42222222222222, 97.07777777777778, 98.3, 97.17777777777778, 95.78888888888889, 88.63333333333334]
print(analyze_differences(d))
print()

print("Average Image Intensity")
d = [99.56140350877193,
    98.59649122807018,
    96.7515923566879,
    96.08832807570978,
    95.20348837209302,
    95.57522123893806,
    96.99248120300751,
    100.0,
    100.0,
    100.0] 
print(analyze_differences(d))
print()


print("Average Image Intensity Clipped")
d  = [100.0,
    97.82608695652173,
    97.61904761904762,
    97.5609756097561,
    100.0,
    91.30434782608695,
    97.82608695652173,
    100.0,
    100.0,
    100.0]
print(analyze_differences(d))
print()

print("Average Border Intensity")
d  = [99.83870967741936,
    99.31592039800995,
    97.65182186234817,
    95.65217391304348,
    94.64788732394366,
    91.02112676056338,
    90.52369077306733,
    91.07692307692308,
    96.05734767025089,
    99.36708860759494]
print(analyze_differences(d))
print()


print("Average Border Intensity Clipped")
d =[100.0,
    97.77777777777777,
    95.65217391304348,
    93.33333333333333,
    95.45454545454545,
    90.9090909090909,
    95.34883720930233,
    89.1891891891892,
    97.14285714285714,
    100.0] 
print(analyze_differences(d))
print()

