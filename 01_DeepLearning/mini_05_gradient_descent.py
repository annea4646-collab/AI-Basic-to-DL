a = 5
r = 0.06
max_iter = 10000
epsilon = 1e-6

print(f"{'반복(n)':<8} {'a_n':<12} {'L(a_n)':<15} {'a_{n+1}':<12}")
print("-" * 50)

for n in range(max_iter):
    derivative = 12.5 * a - 15
    next_a = a - r * derivative

    print(f"{n:<10} {a:<12.6f} {derivative:<15.6f} {next_a:<12.6f}")

    if abs(derivative) < epsilon or abs(next_a - a) < epsilon:
        print("-" * 50)
        print(f"[종료] 접선의 기울기가 0에 수렴했습니다. (반복 횟수: {n})")
        print(f"최종 최적화된 a 값: {a:.6f} (이론적 최솟값 1.2에 근접)")
        break
    a = next_a
