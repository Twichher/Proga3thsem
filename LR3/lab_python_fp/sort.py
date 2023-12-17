data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result_with_lambda = sorted(list(map(lambda i: abs(i), data)), reverse=True)
    print(result_with_lambda)

    result = sorted(list(map(abs, data)), reverse=True)
    print(result)