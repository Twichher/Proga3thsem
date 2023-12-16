import sys

class Equation:

    def __init__(self, a = 1, b = 1, c = 1, arr = []):
        self.a = a
        self.b = b
        self.c = c
        self.arr = arr

    def get_coef(self):
        ans = 0

        try:
            arr = [float(i) for i in sys.argv[1:]]
            if (len(arr) == 3 and arr[0] != 0):
                print("Взяты параметры из cmd")
                #return arr
                self.a = arr[0]
                self.b = arr[1]
                self.c = arr[2]
                ans = 1
            else:
                print("Ошибка при взятии аргументов из cmd")
        except:
            print("Ошибка при взятии аргументов из cmd")

        while ans == 0:
            try:
                print ("Введите 3 действительных числа через пробел (A, B, C)")
                arr = list(map(float, input().split())) #[float(i) for i in input().split()]
                if (len(arr) == 3 and arr[0] != 0):
                    self.a = arr[0]
                    self.b = arr[1]
                    self.c = arr[2]
                    ans = 1
                else:
                    print("Error")
                    ans = 0
            except:
                print("Error")
                ans = 0
        

    def solve(self):
        solutions = []
        d = float(self.b**2 - 4 * self.a * self.c)
        if (d == 0):
            x = -self.b / (2 * self.a)
            solutions.append(x)
        elif (d > 0):
            x1 = (-self.b + d**0.5) / (2 * self.a)
            x2 = (-self.b - d**0.5) / (2 * self.a)
            solutions.append(x1)
            solutions.append(x2)

        self.arr = solutions

    def see_eq(self):
        print(f"{self.a}x^2", end="")

        if (self.b > 0): print(f"+{self.b}x", end="")
        elif (self.b < 0): print(f"{self.b}x", end="")

        if (self.c > 0): print(f"+{self.c}")
        elif (self.c < 0): print(f"{self.c}")

        print()

        if(len(self.arr) == 0): print("Нет корней")
        elif(len(self.arr) == 1): print(f"x = {self.arr[0]}")
        else: print(f"X1 = {self.arr[0]}, X2 = {self.arr[1]}")
            



if __name__ == "__main__":
    obj = Equation()
    obj.get_coef()
    obj.solve()
    obj.see_eq()