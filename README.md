# Phthon

## 다른언어와 틀린점

1. 문자열을 계산 할 수 있다.

```phthon
print(5 * 'z'); // zzzzz
```

2. True / False 는 앞글자를 대문자로한다.

3. not 연산자는 'not ' 을 앞에 붙여준다.

```phthon
print(not False) // True
```

4. 문자열과 변수를 '+'로 연결

```phthon
'안녕 ' + name
```

5. 숫자를 문자열과 연결할려면 str() 을 사용하여 string으로 변환

```phthon
age = 9
'나이는 ' + str(age)
```

6. boolean 값도 str()을 사용하여 string 으로 변환하여 사용

```phthon
is_adult = age > 19
'나이는 ' + str(is_adult) // 나이는 True
```

7. 주석 '# ' 을 붙여준다.
