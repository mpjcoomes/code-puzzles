# FizzBuzz
Print the integers from 1 to 100 inclusive. Instead of the number, print Fizz for multiples of three, Buzz for multiples of five, and FizzBuzz for multiples of both three and five.

	1
	2
	Fizz
	4
	Buzz

	...

	13
	14
	FizzBuzz

	...

	97
	98
	Fizz
	Buzz

### Python
```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

for i in range(1, 101):
    fb = ''
    if i % 3 == 0:
        fb += 'Fizz'
    if i % 5 == 0:
        fb += 'Buzz'
    if not fb:
        fb = i
    print(fb)
```

### Bash
```bash
for i in {1..100}; do
	( (( i % 15 == 0 )) && echo 'FizzBuzz' ) ||
	( (( i % 5 == 0 )) && echo 'Buzz' ) ||
	( (( i % 3 == 0 )) && echo 'Fizz' ) ||
	echo $i;
done
```

### PostgreSQL
```sql
SELECT CASE
	WHEN i % 15 = 0 THEN 'FizzBuzz'
	WHEN i % 5 = 0 THEN 'Buzz'
	WHEN i % 3 = 0 THEN 'Fizz'
	ELSE CAST(i AS VARCHAR)
	END AS A
FROM GENERATE_SERIES(1,100) AS i;
```
