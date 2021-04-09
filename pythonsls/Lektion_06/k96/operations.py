
def max(response):
    # Return Structure
    # gramm: 100
    # uid: 1
    # date: 2020-12-30
    max = { 'gramm': 0,
            'uid': "0",
            'date': "1937-12-30"}
    
    for item in response.get('Items', []):
        current_weight = max['gramm']
        

        item_weight = item['gramm']['N']
        item_weight = int(item_weight)

        if  item_weight > current_weight:
            max['gramm'] = item_weight
            max['uid'] = item['userID']['S']
            max['date'] = item['date']['S']
        
    return max