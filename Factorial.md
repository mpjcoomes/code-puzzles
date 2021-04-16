# Factorial

The *n*! factorial is the product of positive integers less than or equal to n, where 0! = 1. For example, 7! = 7 · 6 · 5 · 4 · 3 · 2 · 1 · 1 = 5040.

> Where 0! = 1,
> 
> *n*! = *n* · (*n* - 1) · (*n* - 2) · (*n* - 3) · ... · 3 · 2 · 1 · 1
>
> Π<sub>*i*=1</sub><sup>*n*</sup>*i* = 1 · 2 · 3 · ... · *n*

Thus the sequence terms are: 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, ...

Write a program to generate the *n*<sup>th</sup> factorial.

### Python
This is a programming exercise, in practice one would simply use Python's factorial() function.
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

# standard library, n < 200000
from math import prod
def fact(n):
    return prod(range(1, n + 1))
```

### Bash
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
As with Python, use PostgreSQL's factorial function in real-world applications.
```sql
-- mathematical, n < 400
do $$
declare
	n integer:= 400;
begin
	raise notice '%',
	ROUND(POWER(10, SUM(LOG(CAST(i AS NUMERIC(1000,990))))))
	FROM GENERATE_SERIES(1,n) AS i;
end; $$;

-- variable, n < 30000
do $$
declare
	n integer := 30000;
	i integer := 0;
	j numeric := 1;
begin
	loop
		exit when i = n;
		i := i + 1;
		select j * i into j;
	end loop;
	raise notice '%', j;
end; $$;

-- tabular iterative, n < 2000
CREATE TABLE fact AS VALUES (1.);
do $$
declare
	n integer:= 2000;
begin
for i in 1..n loop
	INSERT INTO fact
	SELECT column1 * i
	FROM fact
	ORDER BY column1 DESC
	LIMIT 1;
end loop;
raise notice '%',
	* FROM fact
	ORDER BY column1 DESC
	LIMIT 1;
end; $$;
```
