# Is Prime

Write a function that returns *True* if a number is prime.


### Python
```python
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

is_prime(7919)
```