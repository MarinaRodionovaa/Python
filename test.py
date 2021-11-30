import math, time
def decoratorFunc(func):
        def wrapper(*args):
                print("Вызвана функция: {}.".format(func.__name__))
                start = time.time()
                result = func(*args)
                print("На выполнение было потрачено: {} секунд".format(time.time()-start))
                return result
        return wrapper

@decoratorFunc
def calculateSqare(w, h):
    const = 0.000022957
    return (w**2) * const * (h**2) * const

@decoratorFunc
def getVelocity(h):
    startSpeed = 0
    speedUp = 9.8
    return math.sqrt(startSpeed**2)+2*speedUp*h
        
        
w = float(input("Ширина: "))
h = float(input("Высота: "))
print("Result:", calculateSqare(w, h))

h = int(input("Высота: "))
print("Result: ", getVelocity(h))