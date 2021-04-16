# Factorial

The *n*! factorial is the product of positive integers less than or equal to n, where 0! = 1. For example, 7! = 7 · 6 · 5 · 4 · 3 · 2 · 1 · 1 = 5040.

> *n*! = *n* · (*n* - 1) · (*n* - 2) · (*n* - 3) · 3 · 2 · 1 · 1


Thus the sequence terms are: 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, ...

Write a program to generate the *n*<sup>th</sup> factorial.

### python
```python
# recursive, n < 998
def fact(n):
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)

# iterative, n < 100000
def fact(n):
    for i in range(1, n):
        n = n * i
    return n

# math function, n < 200000
from math import prod
def fact(n):
    return prod(range(1, n + 1))
```

### bash
```bash
# recursive, n < 21
fact() {
  if [ "$1" -lt 1 ]; then
    echo 1
  else
    i=$(fact $(("$1" - 1)))
    echo $(("$1" * i))
  fi
}

# iterative, n < 30000
fact() {
  export BC_LINE_LENGTH=0
  bc <<<"$(seq -s'*' 1 "$1")"
```

### PostgreSQL
```sql

```
