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

print("Cls1")
d = [57.733333, 2.3444444, 46.3777777, 2.3111111]
print(analyze_differences(d))
print("Red")
d = [99.7444444, 98.711111, 99.65555555, 97.8444445]
print(analyze_differences(d))

print("White")
d = [99.988877, 24.146368590813037, 98.95451006562118, 35.55778000222445]
print(analyze_differences(d))

print("Gray")
d = [99.83316649983317, 10.4882660438216, 95.62896229562897, 20.59837615393171]
print(analyze_differences(d))

