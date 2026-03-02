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
d = [99.63333333333334, 99.5, 99.65555555555555, 98.84444444444445, 96.62222222222222]
print(analyze_differences(d))


print("MNIST")
d = [7.65209654098543, 25.79245912579246, 34.97942386831276, 15.170726281837393, 1.312423534645757]
print(analyze_differences(d))
