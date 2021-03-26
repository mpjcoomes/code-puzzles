# FizzBuzz
Print the integers from 1 to 100 inclusive. For multiples of three, print Fizz instead of the number. For multiples of five, print Buzz instead of the number. For multiples of both three and five, print FizzBuzz instead of the number.

### python
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
```

### bash
```bash
for i in {1..100}; do
	((( i % 15 == 0 )) && echo 'FizzBuzz') ||
	((( i % 5 == 0 )) && echo 'Buzz') ||
	((( i % 3 == 0 )) && echo 'Fizz') ||
	echo $n;
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
