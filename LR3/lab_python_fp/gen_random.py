from random import randint

def gen_random(count_, min_, max_):
    arr = [randint(min_, max_) for i in range(count_)]
    return arr

if __name__ == "__main__":
    arr = gen_random(5, 1, 3)
    print(arr)