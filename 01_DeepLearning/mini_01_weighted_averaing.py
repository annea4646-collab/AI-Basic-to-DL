
scores = [90, 60, 80, 80]
y_true= 0

weights = [0.1, 0.2, 0.3, 0.1]
bias= -20
learning_rate = 0.005

def predict(x, w, b):
    total_sum = sum(x[i] * w[i] for i in range(len(x))) + b
    return 1 if total_sum > 0 else 0

y_pred = predict(scores, weights, bias)

error = y_true - y_pred

print(f"초기 예측 결과: {'합격' if y_pred == 1 else '불합격'} ({y_pred})")
print(f"실제 결과: {'합격' if y_true == 1 else '불합격'} ({y_true})")
print(f"발생한 오차: {error}")

print("\n--- 가중치 및 편향 업데이트 ---")


subject_names = ["국어","수학","영어","과학"]
for i in range(len(weights)):
    weights[i] = weights[i] + (learning_rate * error * scores[i])
    print(f"업데이트 된 {subject_names[i]} 가중치: {weights[i]:.2f}")

bias = bias + (learning_rate * error * 1)
print(f"업데이트된 편향: {bias:.3f}")
