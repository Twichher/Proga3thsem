import json
from random import randint
from unique import Unique
from print_result import print_result
from field import field
from gen_random import gen_random
from cm_timer import Cm_timer_1

path = "C:\\Users\\vladi\\OneDrive\\Рабочий стол\\LR3thSem\\LR3\\lab_python_fp\\data_light.json"

with open(path, encoding="utf-8") as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted([el for el in Unique(field(arg, 'job-name'), ignore_case = True)])

@print_result
def f2(arg):
    return list(filter(lambda x: x.split()[0] == "программист", arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    return  [f"{man}, зарплата {sal} руб." for man, sal in zip(arg, gen_random(len(arg), 100000, 200000))]


if __name__ == "__main__":
    with Cm_timer_1():
        f4(f3(f2(f1(data))))






