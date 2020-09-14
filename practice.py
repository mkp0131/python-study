# 기본클래스 정의
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    # 메소드 정의
    def damaged(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print('{0}: 파괴되었습니다.'.format(self.name))
        else:
            print('{0}: {1} 데미지를 입었습니다. [hp {2}]'.format(
                self.name, damage, self.hp))

    def move(self, location):
        print('[지상유닛 이동]')
        print('{0}: {1} 로 이동합니다. [이동속도 {2}]'\
          .format(self.name, location, self.speed))


# 클래스 상속
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print('{1}: {0} 방향으로 공격합니다.[공격력 {2}]'\
          .format(location, self.name, self.damage))


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0}: {1} 로 날아갑니다. [속도 {2}]'\
          .format(name, location, self.flying_speed))


# 다중상속
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, speed, flying_speed):
        Flyable.__init__(self, flying_speed)
        AttackUnit.__init__(self, name, hp, damage, speed)

    def move(self, location):
        print('[공중유닛]')
        print('{0}: {1} 로 이동합니다. [이동속도 {2}]'\
            .format(self.name, location, self.flying_speed))


# marine = AttackUnit('마린', 100, 20, 10)
# marine.move(10)

prince = FlyableAttackUnit('스카웃', 100, 60, 0, 9999)
prince.move(10)
