def display_storelist():
    f = open('C:\\Users\Shree\PycharmProjects\Store_Management_System\\storelist.txt',newline='\n')
    alldata = f.readlines()
    for i in alldata:
        x, y, z = (tuple(i.split("|")))
        print(x.center(6),"|", y.center(18),"|", z.center(6),end="")
    f.close()


def add_Menu_Store():
    af = open('C:\\Users\Shree\PycharmProjects\Store_Management_System\\storelist.txt', 'a+')
    add_item_name = input('Enter New Item Name You want To Add in Store:')
    add_item_price = input('Enter The Price of', add_item_name, ':')
    add_item_index = getIndex_sr()
    af.writelines("{}|{}|{}\n".format(add_item_index, add_item_name, add_item_price))
    af.close()


def getIndex_sr():
    fr = open('C:\\Users\Shree\PycharmProjects\Store_Management_System\\storelist.txt')
    inno = fr.readlines()
    rc = 0
    for i in inno:
        rc += 1
    fr.close()
    return rc



def get_Price(j):
    fileread = open('C:\\Users\Shree\PycharmProjects\Store_Management_System\\storelist.txt')
    inno = fileread.readlines()
    price = 0
    for i in inno:
        if str(j) == i.split('|')[0]:
            menuname = i.split('|')[1]
            price = int(i.split('|')[2])
    return menuname, price

