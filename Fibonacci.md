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

Write a program to generate the *n*<sup>th</sup> Fibonacci number.

### python
```python

```

### bash
```bash
# iterative, 0 <= n < 93
fib() {
  fib=(0 1)
  for i in $(seq -s' ' 0 "$1"); do
    n=${#fib[@]}
    fib+=( "$(( ${fib[$((n-2))]} + ${fib[$((n-1))]} ))" )
  done
  echo "${fib["$1"]}"
}

# negafibonacci, tested -10000 < n < 10000
fib() {
  export BC_LINE_LENGTH=0
  fib=(0 1)
  j=$(( $1 > 0 ? $1 : $1 * -1 ))
  for i in $(seq -s' ' 0 "$j"); do
    n=${#fib[@]}
    fib+=( "$(bc<<<"${fib[$((n-2))]} + ${fib[$((n-1))]}")" )
  done
  bc<<<"if ( $1 > 0 ) ${fib["$j"]} else -${fib["$j"]}"
}

# recursive
fib() {
  if [ "$1" -eq 0 ]; then
    echo 0
  elif [ "$1" -eq 1 ]; then
    echo 1
  else
    i=$(fib $(( $1 - 1 )) )
    j=$(fib $(( $1 - 2 )) )
    echo $(( i + j ))
  fi
}
```

### PostgreSQL
```sql
-- tesed to n < 10000
CREATE TABLE fib AS VALUES (0.), (1);
do $$
declare
	n integer:= 1000;
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
```
