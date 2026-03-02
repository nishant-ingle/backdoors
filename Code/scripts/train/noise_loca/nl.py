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

print("CIFAR-10")
d = [81.05555555555556, 64.68888888888888, 75.66666666666667, 32.86666666666667]
print(analyze_differences(d))


print("MNIST")
d = [93.68257146034924, 0.4337671004337671, 92.70381492603715, 0.5449894338783228]
print(analyze_differences(d))
