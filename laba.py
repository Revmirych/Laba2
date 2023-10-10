Goods = []
Shops = ["Ашан" , "Магнит" , "Пятерочка"]
Posts = []
IsTrue = True
while IsTrue == True:
   Name = input(f"Введите название товара \n")
   if Name != '':
     Goods.append(Name)
   else:
    IsTrue = False


for Item in Goods:
  Goods_posts = []
  for Shop in Shops:
    Price = int(input(f"Введите цену на товар {Item} в магазине {Shop}\n"))
    Goods_posts.append(Price)
  Posts.append(Goods_posts)
Basket = []
for Count , Value in enumerate(Shops):
  Total = 0
  for Idx , Product in enumerate(Goods):
    Total+= Posts[Idx][Count]
  print(f"стоимость корзины в магазине {Value}: {Total}")
  Basket.append(Total)
Min_Dx = 0
Min_Value = None
for Idx , Value in enumerate(Basket):
  if Min_Value == None  or Value < Min_Value:
    Min_Dx = Idx
    Min_Value = Value
print(f"минимальная цена в магазине {Shops[Min_Dx]}")
