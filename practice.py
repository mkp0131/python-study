class House:
    def __init__(self, location, house_type, deal_type, price, year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.year = year

    def show_detail(self):
        print('{0} {1} {2} {3} {4}'\
          .format(self.location, self.house_type, self.deal_type, self.price, self.year))


houses = []
house1 = House('강남', '아파트', '매매', '2억', '1989')
houses.append(house1)
house2 = House('강남', '아파트', '매매', '1억', '1989')
houses.append(house2)
house3 = House('강남', '아파트', '매매', '3억', '1989')
houses.append(house3)

print('총 {0} 개의 매물이 있습니다.'.format(len(houses)))
for house in houses:
    house.show_detail()
