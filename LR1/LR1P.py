import sys

def get_param():

    try:
        arr = [float(i) for i in sys.argv[1:]]
        if (len(arr) == 3 and arr[0] != 0):
            print("Взяты параметры из cmd")
            return arr
        else:
            print("Ошибка при взятии аргументов из cmd")
    except:
        print("Ошибка при взятии аргументов из cmd")

    ans = 0
    while ans == 0:
        try:
            print ("Введите 3 действительных числа через пробел (A, B, C)")
            arr = list(map(float, input().split())) #[float(i) for i in input().split()]
            if (len(arr) == 3 and arr[0] != 0):
                return arr
            else:
                print("Error")
                ans = 0
        except:
            print("Error")
            ans = 0




#arr[0, 1, 2] - a, b, c

def solve(arr):
    solutions = []
    d = float(arr[1]**2 - 4 * arr[0] * arr[2])
    if (d == 0):
        x = -arr[1] / (2 * arr[0])
        solutions.append(x)
    elif (d > 0):
        x1 = (-arr[1] + d**0.5) / (2 * arr[0])
        x2 = (-arr[1] - d**0.5) / (2 * arr[0])
        solutions.append(x1)
        solutions.append(x2)

    return solutions




def main():
    arr = get_param()
    solutions = solve(arr)
    if (len(solutions) == 2):
        print(f"X1 = {solutions[0]}; X2 = {solutions[1]}")
    elif (len(solutions) == 1):
        print(f"X = {solutions[0]}")
    else:
        print("Корней нет")




if '__main__' == __name__:
    main()

