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

8. 문자열을 줄바꿈을 포함하여 사용하고 싶을때 """ 쌍따옴표(따옴표)를 3번 감싸서 사용

```python
str = '''
안녕1
안녕2
'''
```

9. 문자열에서 원하는 index ~ index 까지 가져오는 방법

```python
str[0:2] # 0 ~ 2
str[:2] # 0 ~ 2
str[2:] # 2 ~ END
str[-7:] # 뒤에서부터 7 까지
```

10. 문자열의 길이를 알아내기 len(python)

11. 문자열에서 해당문자의 index 찾기 => str.index("n", startindex)

1) 만약 찾는 문자가 없을때 error를 내보낸다.

12. find('n') 문자열 찾기

13. count('n') => 문자열에서 문자가 몇번 사용되는지 확인

### array (list)

#### array 의 기본형태 => subway = [1, 2, 3]

14. arr.append('dd') => array 에 맨 뒤에 값을 push

15. arr.insert(1, 'dd') => 해당되는 index 에 값을 push

16. arr.pop() => 맨뒤에 값을 제거

17. arr.clear() => 값 모두 삭제

18. arr1.extend(arr2) => arr1, arr2 를 하나의 array로 합침

### obj (사전) => obj = {'인사': '안녕', '나이': 11}

19. obj 의 key 값은 유니크하다. key 값이 중복되었을 경우 뒤에 값이 overwrite 된다.

20. obj 의 값을 가져올때는 get() 메소드를 사용한다. => get 메소드를 사용하지 않고 값을 가져올 경우 값이 없다면 error 를 출력함.

21. value in obj => obj 에 값이 있는지 없는지 boolean 값으로 return

22. del obj[key] => delete

23. obj.keys() => key 들만 arr 로 return

24. obj.values() => value 들만 arr 로 return

25. obj.items() => [key, value] 쌍으로 return

26. obj.clear() => 모두삭제

### 튜플 => name = ('mkp', 'kan')

27. 튜플 -> 값을 변경할수없다.

28. 구조분해 할당 가능
    (name, age, say) = ('mkp', 14, 'hello')

### set => {1, 2} => 키없이 value 만 적어준다. (중복이 제거됨)

29. 중복이 안되고 순서가 없다.

30. 합집합을 만들거나 교집합을 만들어서 return 할 수있다.

31. 합집합 => java | python

32. 교집합 => java & python

33. 차집합 => java - python

34. set.add(value) => 값을 추가

35. set.remove(value) => 값을 제거

### type 변경

36. type(value) 의 형태로 type 을 알아낼 수 있다.

37. list(value) => type 을 리스트로 만든다.

38. tuple(value), set(value) 사용가능

### function

39. 가변인자 사용법

```
def profile(name, age, *language):
	for lang in language
		print(lang)
```

40. 함수내에서 전역변수를 사용하기 위해 global 키워드를 사용한다

```
b = 10
def add(a):
	global b
	return a + b
```
