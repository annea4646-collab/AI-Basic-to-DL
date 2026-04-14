x = [4, 8, 12, 16, 20]
y_t = [6, 5, 16, 12, 20]

def calculate_errors(x_list, y_list, model_func):
    mae_sum=0
    mse_sum=0
    n = len(x_list)

    for i in range(n):
        y_p = model_func(x_list[i])
        error = y_list[i] - y_p
        mae_sum += abs(error)
        mse_sum += error ** 2

    return mae_sum/n, mse_sum/n

model_a = lambda x: (9/8) * x
model_b = lambda x: (7/8) * x

mae_a, mse_a = calculate_errors(x, y_t, model_a)
mae_b, mse_b = calculate_errors(x, y_t, model_b)

print(f"--- 모델 A (y = 9/8x) ---")
print(f"MAE: {mae_a:.2f}")
print(f"MSE: {mse_a:.2f}\n")

print(f"--- 모델 B (y = 7/8x) ---")
print(f"MAE: {mae_b:.2f}")
print(f"MSE: {mse_b:.2f}")
