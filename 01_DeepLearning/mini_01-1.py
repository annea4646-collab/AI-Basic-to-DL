scores = [90, 60, 80, 80]
y_true = 0

weights = [0.1, 0.2, 0.3, 0.1]
bias = -20
learning_rate = 0.0005

def predict(x, w, b):
    total_sum = sum(x[i] * w[i] for i in range(len(x))) + b
    return 1 if total_sum > 0 else 0

epochs = 100
for epoch in range(epochs):
    y_pred = predict(scores, weights, bias)
    error = y_true - y_pred
    
    if error == 0:
        print(f"{epoch}번째 에포크에서 학습 완료!")
        break

    for i in range(len(weights)):
        weights[i] = weights[i] + (learning_rate * error * scores[i])
    
    bias = bias + (learning_rate * error * 1)
    
    print(f"에포크 {epoch+1}: 오차 {error}, 편향 {bias:.3f}")

print("\n--- 최종 학습 결과 ---")
subject_names = ["국어", "수학", "영어", "과학"]
for i in range(len(weights)):
    print(f"최종 {subject_names[i]} 가중치: {weights[i]:.2f}")
print(f"최종 편향: {bias:.3f}")


final_pred = predict(scores, weights, bias)
print(f"최종 예측: {'합격' if final_pred == 1 else '불합격'} ({final_pred})")