import random
alhp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
nums = '1234567890'
spec_sym = '!@#$%^&*()_'


def gen_random_pass(lenght, lett, num, spec):
    pasw = []
    if lett == 1:
        for i in range(lenght):
            pasw += [random.choice(list(alhp))]
    if num == 1:
        for i in range(lenght):
            pasw += [random.choice(list(nums))]
    if spec == 1:
        for i in range(lenght):
            pasw += [random.choice(list(spec_sym))]
    random.shuffle(pasw)
    while True:
        tempr = random.sample(pasw, lenght)
        z = 0
        if lett == 1:
            for i in tempr:
                if i in alhp:
                    z += 1
                    break
        if num == 1:
            for i in tempr:
                if i in nums:
                    z += 1
                    break
        if spec == 1:
            for i in tempr:
                if i in spec_sym:
                    z += 1
                    break
        if z == (lett + num + spec):
            break
    

    return ''.join(tempr)


def pah_def(lenght, lett, num, spec):
    if (lenght > 31) or (len(str(lett)) > 2) or (len(str(num)) < 0) or (len(str(spec)) < 0) or (lenght < 0) or (lenght == 0):
        return True
    elif lenght == 0 or (lett == 0 and spec == 0 and num == 0):
        return True