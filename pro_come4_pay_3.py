def promotion(come,pay,pax,per_head):
    money = (pax // come)*(per_head*pay) + (pax % come)*(per_head)
    return money
print(promotion(4,3,5,200))