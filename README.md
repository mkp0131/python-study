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

### 파일쓰기

41. open 함수 사용.

```
src_file = open('ttt.txt', "w", encoding="utf-8")
print('안녕하세요.', file=src_file)
src_file.close()
```

42. "w" => 덮어쓰기(새로운파일생성), "a" => 이어쓰기(append)

43. "r" => 읽어오기

```
src_file = open('ttt.txt', "r", encoding="utf-8")
print(src_file.read())
src_file.close()
```

44. src_file.read() => 모두 읽기, readline() => 한줄 읽기, readline() => [한줄내용, 한줄내용] 으로 return

45. 자료형을 파일에 저장할때 pickle 사용

```
import pickle

obj = {'name': 'kan', 'age': 31}
src_file = open('ttt.pickle', "wb")
pickle.dump(obj, src_file)
src_file.close()
```

46. wb => 바이너리 데이터 쓰기, rb => 바이너리 데이터 읽기

47. 파일에서 데이터 읽기

```
import pickle

src_file = open('ttt.pickle', "rb")
profile = pickle.load(src_file)
print(profile)
src_file.close()
```

48. with 를 사용하여 file 닫기 없이 가독성 좋게 사용하기

```
with open('ttt.txt', "r", encoding="utf-8") as hello:
    print(hello.read())
```

50. 연습문제

```
# 주간보고서를 50주차(50개) 만드시오.
# 파일이름규칙 "1주차", "2주차" ...
# 보고서 형태
# - X 주차 보고서 -
# 부서:
# 이름:

for index in range(1, 51):
    memo = '- {0}주차 보고서 -\n부서: 개발팀\n이름: 박민규'.format(index)
    with open('./주간보고서/{0}주차.txt'.format(index), "w",
              encoding="utf-8") as weeklyReport:
        print(memo, file=weeklyReport)

```

### class 클래스

# 기본클래스 정의

class Unit:
def **init**(self, name, hp):
self.name = name
self.hp = hp

# 메소드 정의

def damaged(self, damage):
self.hp -= damage
if self.hp <= 0:
print('{0}: 파괴되었습니다.'.format(self.name))
else:
print('{0}: {1} 데미지를 입었습니다. [hp {2}]'.format(self.name, damage, self.hp))

# 클래스 상속

class AttackUnit(Unit):
def **init**(self, name, hp, damage):
Unit.**init**(self, name, hp)
self.damage = damage

def attack(self, location):
print('{1}: {0} 방향으로 공격합니다.[공격력 {2}]'.format(location, self.name, self.damage))

class Flyable:
def **init**(self, flying_speed):
self.flying_speed = flying_speed

def fly(self, name, location):
print('{0}: {1} 로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))

# 다중상속

class FlyableAttackUnit(AttackUnit, Flyable):
def **init**(self, name, hp, damage, flying_speed):
AttackUnit.**init**(self, name, hp, damage)
Flyable.**init**(self, flying_speed)

# marine = Flyable(100)

# marine.fly('마린', 10)

prince = FlyableAttackUnit('스카웃', 100, 60, 999)
prince.fly(prince.name, 10)

# 내가 원하는 error 메세지를 출력할 수 있게 만듦.

class NumberError(Exception):
def **init**(self, msg):
self.msg = msg

def **str**(self):
return self.msg

try:
raise NumberError('안녕') # 의도적으로 에러발생
except NumberError as err: # ValueError 에러일때 에러메세지 발생
print("에러입니다")
print(err)
finally: # 무조건 실행
print('Thank you')

class SoldOutErr(Exception):
def **init**(self, msg):
self.msg = msg
def **str**(self):
return self.msg

chichen = 10

while True:

try:
order = int(input('몇마리 주문?'))

      if(not order):
         raise ValueError
         continue
      else:
         if (chichen < order):
            print('재료가 부족합니다. {0} 마리 주문가능합니다.'.format(chichen))
            continue

         chichen -= order
         print('{0} 마리 나왔습니다.'.format(order))
         if(chichen == 0):
            raise SoldOutErr('#### 주문이 모두 소진되었습니다. ####')

except ValueError:
print('#### 주문을 다시해주세요. ####')
except SoldOutErr as err:
print(err)
print("#### 영업을 종료합니다.👏 ####")
break

### module

#### 1. 단순한 사용(안에 있는 함수 모두 가져오기)

import apple
apple.hello()

#### 2. 이름을 지정(안에 있는 함수 모두 가져오기)

import apple as fruit
fruit.hello()

#### 3. 전역 사용

from apple import \*

#### 4. 전역사용으로 원하는 함수만 가져오기

from apple import hello as hi

#### \* 폴더는 . 으로 표시

### pakage

0. 파이썬 파일들을 폴더로 묶어 놓음.
1. form apple import \* # apple 이라는 폴더에 있는 모든 .py 파일을 사용하기 원할경우, 공개설정을 해야함.
2. **init**.py # 패키지폴더에서의 공개설정
3. **all** = ["vietnam"] # vietnam.py 를 공개한다.
4. py 파일내에서 직접실행시 무언가를 추가하고싶을경우 => **name** 정보를 활용
   => 파일내에서 직접 사용시 if **name == "**main\_\_"
5. inspect 모듈 => 패키지의 위치를 알고싶을때

```py
import inspect
import random
print(inspect.getfile(random)) # random 모듈의 위치
```
