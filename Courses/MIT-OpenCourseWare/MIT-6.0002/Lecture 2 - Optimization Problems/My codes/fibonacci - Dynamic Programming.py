""" Calculation of fibonacci sequence using dynamic programming. Mearning, using
more space to store previous values but reducing execution time """
def new_fib(number, history = {}):
    if number == 0 or number == 1:
        return 1
    try:
        return history[number]
    except KeyError:
        result = new_fib(number - 1, history) + new_fib(number - 2, history)
        history[number] = result
        return result

""" Old recursive algorithm """
# def old_fib(number):
#     if number == 0 or number == 1:
#         return 1
#     else:
#         return old_fib(number - 1) + old_fib(number - 2)

""" main """
for i in range(200):
    print('fib ', i, ' : ', new_fib(i))
#     print('fib ', i, ' : ', old_fib(i))
