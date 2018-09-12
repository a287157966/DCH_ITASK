import random
import string

def login_user():
    username = "auto_test"
    return  username
def login_pwd():
    password = "111111"
    return password

def get_coustom_name():
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    #print(ran_str)
    return ran_str
def get_coustom_mobile():
    mobile = str(random.randint(10000000000,99999999999))
    #print(mobile)
    return mobile
def get_id_card():
    id_card = str(random.randint(100000000000000000,999999999999999999))
    #print(id_card)
    return id_card
def storage_information(custom_name=None,custom_mobile=None):
    custom_name = custom_name
    custom_mobile = custom_mobile
    return custom_name,custom_mobile


# if __name__ == '__main__':
#     cus = get_coustom_name()
#     #get_coustom_mobile()
#     #get_id_card()
#     si = storage_information(custom_name=cus,custom_mobile='454534')
#     print(si)
