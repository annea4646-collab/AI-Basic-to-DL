data = {
    "Bus": [0.8, 0.7, 0.6, 0.4],     # [길이, 높이, 각진모서리, 곡선]
    "Truck": [0.7, 0.6, 0.8, 0.2],
    "SUV": [0.5, 0.5, 0.6, 0.5]
}

new_car = [0.55, 0.45, 0.62, 0.48]

def calculate_distance(v1, v2):
    sum_squares = 0
    for i in range(len(v1)):
        sum_squares += (v1[i] - v2[i])** 2
    distance = sum_squares ** 0.5
    return distance

results = {}
for category, features in data.items():
    dist = calculate_distance(new_car, features)
    results[category]= dist
    print(f"{category}와의 거리: {dist:.4f}")

prediction = min(results, key=results.get)
print(f"이 차량은 {prediction}로 분류됩니다.")