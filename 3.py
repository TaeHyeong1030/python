price = {
    "콩나물해장국": 4500,
    "갈비탕": 9000,
    "돈가스": 8000
}

price["팟타이"] = 7000

print("식당 메뉴와 가격:")
for menu, cost in price.items():
    print(f"{menu}: {cost}원")
