def recu_fibonacci(fn):
  f1 = 1
  if fn<=f1:
    return fn
  else:
    fn = recu_fibonacci(fn-1) + recu_fibonacci(fn-2)
    return fn

def f(terms=3):
  if terms <=0:
    print('introduzca un termino valido')
  else:
    for i in range(terms):
      fibo = recu_fibonacci(i)
      # print(fibo)
    return fibo
f = f(terms=1000)
print(f'fibonacci = {f}')