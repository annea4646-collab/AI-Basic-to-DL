from math import e

def sigmoid(z):
    return 1 / (1 + e**-z)

def sigmoid_derivative(z):
    s = sigmoid(z)
    return s * (1-s)

def relu(z):
    return max(0, z)

def relu_derivative(z):
    return 1 if z > 0 else 0

def calculate_accumulated_gradient(gradients):
    accumulated = 1
    for g in gradients:
        accumulated *= g
    return accumulated


print("--- 1. 시그모이드 도함수의 최댓값 확인 ---")
print(f"z=0 일 때 시그모이드의 미분값: {sigmoid_derivative(0)}\n")

sig_gradients = [0.25, 0.2, 0.1, 0.15, 0.3]
sig_accumulated = calculate_accumulated_gradient(sig_gradients)

print("--- 2. 기울기 소실(Gradient Vanishing) 시뮬레이션 ---")
print(f"각 층의 미분값: {sig_gradients}")
print(f"-> 시그모이드 누적 기울기 연쇄 곱셈 결과: {sig_accumulated:.6f}")
print(f" (결과값이 0에 매우 가까워져 앞쪽 층의 가중치가 업데이트되지 않음)\n")

relu_gradients = [1.0, 1.0, 1.0, 1.0, 1.0]
relu_accumulated = calculate_accumulated_gradient(relu_gradients)

print("--- 3. ReLU 함수를 적용한 경우 ---")
print(f"각 층의 미분값 (양수 영역): {relu_gradients}")
print(f"-> ReLU 누적 기울기 연쇄 곱셈 결과: {relu_accumulated:.6f}")
