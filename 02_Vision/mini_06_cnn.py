import numpy as np

def correlate_2d(image, kernel):
    img_h, img_w = image.shape
    ker_h, ker_w = kernel.shape

    out_h = img_h - ker_h + 1
    out_w = img_w - ker_w + 1

    output = np.zeros((out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            region = image[i:i+ker_h, j:j+ker_w]
            output[i,j] = np.sum(region * kernel)
    return output

# 원본 이미지
A = np.array([
    [10, 35, 15],
    [15, 30, 10],
    [10, 20, 5]
])

# 필터 커널
F = np.array([
    [1, -2],
    [0, 2]
])

result = correlate_2d(A, F)
print(result.tolist())
