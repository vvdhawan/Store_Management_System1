import os
import time

import storeroom.storedb as stdb
class Store:
    bill = 0

    def item_selected(self,menu , nos, itembill):
        self.menu = menu
        self.nos = nos
        self.itembill = itembill
        f = open('bill.txt','a+')
        f.writelines("{} * {} = {} \n".format(self.menu, self.nos, self.itembill))
        f.close()
        pass


    def billCountre(self, itembill):
        Store.bill += self.itembill


def item_selector():
    pid = input('Enter Your Product Serial No You want to Buy:')
    m, p = stdb.get_Price(pid)
    quantity = int(input('Enter The Quantity:'))
    
    return m, p, quantity

print("Hello Dear Customer Welcome To Alibaba Shopping Center")


while True:
    stdb.display_storelist()
    print('1. Buy \n 2. Get Bill \n 3. Cancel and Exit')
    choice = int(input('Enter Your Option:'))
    if choice == 1:
        menu, price, nos = item_selector()
        itembill = price * nos
        itms = Store()
        itms.item_selected(menu , nos, itembill)
        itms.billCountre(itembill)
        time.sleep(5)
    elif choice == 2:
        print('*********************************')
        print("\n Your Bill is Here:")
        print('*********************************')
        f = open('bill.txt')
        obj = f.read()
        print(obj)
        print("Total Bill Amount is", Store.bill )
        print('******************************************')
        print('THANK YOU FOR SHOPPING WITH US VISIT AGAIN')
        print('******************************************')
        time.sleep(5)
        f.close()
        os.remove('bill.txt')
        break


    elif choice == 3:
        print('Thank You for your Visit, Visit Again !!!')
        time.sleep(5)
        exit()
    else:
        print('please Enter Correct Option')
        time.sleep(3)
        exit()
