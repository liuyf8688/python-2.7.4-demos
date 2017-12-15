import timeit

def fibonacci(x):
    if x < 1:
        return 0;
    
    if x == 1 or x == 2:
        return 1
    
    return fibonacci(x - 1) + fibonacci(x - 2)

# print fibonacci(0)
# print fibonacci(1)
# print fibonacci(2)
# print fibonacci(3)
# print fibonacci(4)
# print fibonacci(5)
num = 1
while num <= 2000:
    
    start_time = timeit.default_timer()
    print num, fibonacci(num), '%.10f seconds' % (timeit.default_timer() - start_time)
    num += 1