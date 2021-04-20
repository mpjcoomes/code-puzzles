# Calculate *π*

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
```

### PostgreSQL
```sql

```
