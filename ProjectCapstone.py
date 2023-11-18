warehouseStock = [
    {
        'stockId': 'WS01',
        'stockName': 'White Shirt',
        'size': 'S',
        'qty': 20,
        'price' : 20000
    },
    {
        'stockId': 'WS02',
        'stockName': 'Blue Jeans',
        'size': 'S',
        'qty': 20,
        'price': 50000
    },
    {
        'stockId': 'WS03',
        'stockName': 'Jacket',
        'size': 'S',
        'qty': 20,
        'price': 70000
    }
]

cart = []

def showingStockList() :
    print('Stock List\n')
    print('Index\t| Stock ID  \t| Stock Name\t| Size \t| Qty \t| Price')
    for i in range(len(warehouseStock)) :
        print('{}\t| {}  \t| {}  \t| {}  \t| {}  \t| {}'.format(i,warehouseStock[i]['stockId'],warehouseStock[i]['stockName'],warehouseStock[i]['size'],warehouseStock[i]['qty'],warehouseStock[i]['price']))

def addNewStock() :
    stockId = input('Please Input New Stock ID : ')
    stockName = input('Please Input New Stock Name : ')
    size = input('Please Input Size : ')
    qtyStock = int(input('Please Input Qty : '))
    price = int(input('Please Input Price : '))
    warehouseStock.append({
        'stockId' : stockId,
        'stockName': stockName,
        'size': size,
        'qty': qtyStock,
        'price': price
    })
    showingStockList()

def deleteStock() :
    showingStockList()
    indexStock = int(input('Please input index stock will delete : '))
    del warehouseStock[indexStock]
    showingStockList()

def recordSellStock() :
    showingStockList()
    while True :
        indexStock = int(input('Please input index stock will sell : '))
        if (indexStock < len(warehouseStock)):
            qtySell = int(input('Please input selling qty : '))
            if(qtySell > warehouseStock[indexStock]['qty']) :
                print('Qty is not enough, stock {} remains {}'.format(warehouseStock[indexStock]['stockName'],warehouseStock[indexStock]['qty']))
            else :
             cart.append({
                'stockId': warehouseStock[indexStock]['stockId'],
                'stockName' :warehouseStock[indexStock]['stockName'],
                'size': warehouseStock[indexStock]['size'],
                'qty': qtySell, 
                'price': warehouseStock[indexStock]['price'], 
                'index': indexStock
                })
        else:
            print('Wrong Input Index Stock !!! Please input again')
        print('Cart :')
        print('Stock Id\t| Stock Name\t| Size \t| Qty\t| Price')
        for item in cart :
            print('{} \t\t| {}  \t| {}  \t| {}  \t| {}'.format(item['stockId'], item['stockName'],item['size'], item['qty'], item['price']))
        checker = input('Make another selling? (yes/no) = ')
        if(checker == 'no') :
            break

    print('Selling List :')
    print('StockId\t| Stock Name\t| Size \t|  Qty\t| Price   \t| Total Price')
    totalPrice = 0
    for item in cart :
        print('{}  \t| {} \t| {} \t| {}  \t| {} \t| {}'.format(item['stockId'], item['stockName'], item['size'], item['qty'], item['price'], item['qty'] * item['price']))
        totalPrice += item['qty'] * item['price']    
    while True :
        print('Sales Total = {}'.format(totalPrice))
        money = int(input('Please input customer payment : '))
        if(money > totalPrice) :
            change = money - totalPrice
            print('Transaction Complete \n\nCustomer Change : {}'.format(change))
            for item in cart :
                warehouseStock[item['index']]['qty'] -= item['qty']
            cart.clear()
            break
        elif(money == totalPrice) :
            print('Transaction Complete')
            for item in cart :
                warehouseStock[item['index']]['qty'] -= item['qty']
            cart.clear()
            break
        else :
            short = totalPrice - money
            print('Customer payment is short {}'.format(short))

while True :
    optionMenu = input('''
        Welcome to Warehouse Stock Program

        List Menu :
        1. Showing Warehouse Stock
        2. Add New Stock
        3. Delete Stock
        4. Selling Stock
        5. Exit Program

        Please input your menu option : ''')

    if(optionMenu == '1') :
        showingStockList()
    elif(optionMenu == '2') :
        addNewStock()
    elif(optionMenu == '3') :
        deleteStock()
    elif(optionMenu == '4') :
        recordSellStock()
    elif(optionMenu == '5') :
        break