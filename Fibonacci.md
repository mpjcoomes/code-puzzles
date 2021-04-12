# Fibonacci Sequence
Fibonacci numbers form an *F<sub>n</sub>* sequence where each number is the sum of the two preceding it, indexed from 0.

> *F*<sub>0</sub> = 0
>
> *F*<sub>1</sub> = 1
> 
> Where *n*>1, *F<sub>n</sub>* = *F<sub>n</sub>*-1 + *F<sub>n</sub>*-2
> 
> Where *n*<0, *F<sub>n</sub>* = *F<sub>n</sub>*+2, - *F<sub>n</sub>*+1, or  *F<sub>-n</sub>* = (-1)<sup>*n*+1</sup>*F<sub>n</sub>*

Thus the positive sequence terms are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, ...

Write a program to generate the *n*<sup>th</sup> Fibonacci number. Optionally, support the bidirectional negative sequence (i.e. negafibonacci).

### python
```python
# iterative, tested n < 400000
def fib(n):
    fibl = [0, 1]
    for i in range(0, n):
        fibl.append(fibl[-1] + fibl[-2])
    return fibl[n]

# rescursive, tested n < 35
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
```

### bash
```bash
# negafibonacci, tested -10000 < n < 10000
fib() {
  export BC_LINE_LENGTH=0
  fib=(0 1)
  j=$(( $1 > 0 ? $1 : $1 * -1 ))
  for i in $(seq -s' ' 0 "$j"); do
    n=${#fib[@]}
    fib+=( "$(bc<<<"${fib[$((n-1))]} + ${fib[$((n-2))]}")" )
  done
  bc<<<"if ( $1 > 0 ) ${fib["$j"]} else -${fib["$j"]}"
}

# simple iterative, tested n < 93
fib() {
  fib=(0 1)
  for i in $(seq -s' ' 0 "$1"); do
    n=${#fib[@]}
    fib+=( "$(( ${fib[$((n-1))]} + ${fib[$((n-2))]} ))" )
  done
  echo "${fib["$1"]}"
}

# recursive, inefficient, tested n < 25
fib() {
  if [ "$1" -lt 2 ]; then
    echo "$1"
  else
    i=$(fib $(( $1 - 1 )) )
    j=$(fib $(( $1 - 2 )) )
    echo $(( i + j ))
  fi
}
```

### PostgreSQL
```sql
-- nested tabular, tested n < 10000
CREATE TABLE fib AS VALUES (0.), (1);
do $$
declare
	n integer:= 10;
begin
for i in 1..n loop
	INSERT INTO fib
	SELECT SUM(column1)
	FROM (
		SELECT *
		FROM fib
		ORDER BY column1 DESC
		LIMIT 2
		) AS t;
end loop;
raise notice '%',
	* FROM fib
	ORDER BY column1 DESC
	LIMIT 1
	OFFSET 1;
end; $$;

-- in-memory, performant, tested n < 500000
do $$
declare
	n integer := 10;
	i integer := 0;
	k numeric := 0; 
	j numeric := 1;
begin
	if n = 0 then
		k := 0;
	end if;
	loop
		exit when i = n;
		i := i + 1;
		select j, k + j into k, j;
	end loop;
	raise notice '%', k;
end; $$;
```
