# Product Inventory Project
# Mithil Patel
# Last worked on 10/13/2020


# initilization of product class 
class Products:
    def __init__(self,ID,price,quantity):
        self.ID = ID
        self.price = price
        self.quantity = quantity
        
class Inventory():
# initial inventory list
    def __init__(self):
        self.productlist = []
        self.pricelist = []
        self.quantitylist = []
        
# Add inventories
    def add_product(self):
        self.ID = input('Enter product ID: ')
        self.price = input('Enter price of the produce: ')
        self.quantity = input('Enter quantity of the produce: ')
        self.productlist.append(self.ID)
        self.pricelist.append(self.price)
        self.quantitylist.append(self.quantity)
    
    def Dict(self):
        dict_ID_price = dict(zip(self.productlist, self.pricelist))
        # convert keys to int using for loop
        for keys in dict_ID_price:
            dict_ID_price[keys] = int(dict_ID_price[keys])
        return dict_ID_price
        
    def Dict2(self):
        dict_ID_quantity = dict(zip(self.productlist, self.quantitylist))
        for keys in dict_ID_quantity:
            dict_ID_quantity[keys] = int(dict_ID_quantity[keys])
        return dict_ID_quantity

inv = Inventory()
def add_quan(search, add_q):
    val = inv.Dict2()[search]
    val += add_q
    return val

def remove_quan(search, rem_q):
    val2 = inv.Dict2()[search]
    val2 -= rem_q
    return val2
   
# takes user's input to look up product details in the inventory 
def Match(name):
    search = ''
    for i in name.Dict().keys():
        while i not in search:
            search = input('What would you like to look up? Please enter product ID:')
            if i == search:
                print("Product ID: {}\nPrice: {} \tQuantity: {}".format(i, name.Dict()[i],name.Dict2()[i]))
            else:
                print('Cannot find a match')
                continue
                
# function to add or remove quantity from product inventory
def Updated_quantity(name):
    for i in name.Dict2().keys():
        pro_id = ''
        while pro_id != i:
            pro_id = input('To update quantity please enter product ID: ')
            if pro_id == i:
                break  
            else:
                print('ID not found. Please try again.')
                continue  
                
        add_or_remove = ' '
        while add_or_remove.lower() != 'add' or add_or_remove.lower() != 'rem':
            add_or_remove = input("Would you like to add or remove quantity? please enter 'add' or 'rem'")
            if add_or_remove.lower() == 'add':
                add_q = int(input('How many quantities would you like to add?'))
                inv.Dict2().update(pro_id = add_quan(pro_id, add_q))
                print('Product ID:{} Quantity:{}'.format(pro_id, add_quan(pro_id, add_q)))
                break

            elif add_or_remove.lower() == 'rem':
                rem_q = int(input('How many quantities would you like to remove?'))
                inv.Dict2().update(pro_id = remove_quan(pro_id, rem_q))
                print('Product ID: {} Quantity: {}'.format(pro_id, remove_quan(pro_id, rem_q)))
                break
        total = 0
        total2 = 0 
        total += name.Dict2()[i]
        total2 += (name.Dict()[i])*name.Dict2()[i]

# Function to update/change price 
def Updated_price():
    for i in inv.Dict().keys():
        pro_id = ''
        while pro_id != i:
            pro_id = input('To update price please enter product ID: ')
            if pro_id == i:
                break
            
            else:
                print('ID not found. Please try again.')
                continue 
        up_pri = int(input('Please enter new price: '))
        inv.Dict().update(pro_id = up_pri)
        print('Updated price: {}'.format(inv.Dict()[i]))
        
# Welcome message for product inventory        
print("Welcome to Product Inventory menu!!")
boo = True
while boo:
    ask = 'random'
    while ask.lower() != 'add' or ask.lower() != 'rem':
        ask = input("would you like to add product, update quantity, update price, or look up product? Enter 'add', 'uq', 'up' or 'look' ")
        if ask.lower() == 'add':
            inv.add_product()
            inv.Dict()
            inv.Dict2()
            print("The product '{}' has been added to your inventory.".format(inv.ID))
            boo = False
            break
        elif ask.lower() == 'uq':
            Updated_quantity(inv)
            break
        elif ask.lower() == 'up':
            Updated_price()
            break
        elif ask.lower() == 'look':
            Match(inv)
            break
            
# Asking the user whether to continue with the menu   
    again = ''
    while again not in ['Y','y','N','n']:
        again = input('Would you like to continue? Enter y or n') 
        if again[0].lower() == 'y':
            boo = True
            continue
        elif again[0].lower() == 'n':
            print('Thank you. Have a wonderful day!')
            boo = False
            break
        else:
            print('Invalid input. Please enter y or n')
            continue
            