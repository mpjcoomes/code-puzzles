# Estimate *π*

The value of *π* can be approximated via Leibniz's alternating series.

4 - <sup>4</sup>/<sub>3</sub> + <sup>4</sup>/<sub>5</sub> - <sup>4</sup>/<sub>7</sub> + <sup>4</sup>/<sub>9</sub> ··· = *π*   

A greater number of terms increases the accuracy of the estimation. Convert this into a function that accepts the number of iterations.

### Python
```python
def pi(n):
    k = 0
    sign = 1
    deno = 1
    for _ in range(n):
        k += sign * 4 / deno
        sign *= -1
        deno += 2
    return k

print(pi(1000000))
```

### Bash
```bash
pi() {
  k=0
  sign=1
  deno=1
  for i in $(seq -s' ' 1 "$1"); do
    k=$(bc <<<"scale=1000; $k + $sign * 4 / $deno")
    sign=$((sign * -1))
    ((deno+=2))
  done
  echo "$k"
}

pi 10000
```

### PostgreSQL
```sql
CREATE OR REPLACE FUNCTION pg_pi(NUMERIC) RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
DECLARE
	k numeric := 0;
	s numeric := 1;
	d numeric := 1;
BEGIN
	for _ in 1..$1 loop
		select k + s * 4 / d into k;
		s := s * -1;
        d := d + 2;
	end loop;
	raise notice '%', k;
END; $$;

select pg_pi(300000);
```
