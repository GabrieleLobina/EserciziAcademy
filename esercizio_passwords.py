class PasswordLV2():
    def __init__(self):
        self.password = []
        
    def add_password(self, new_password=0):
        if new_password: 
            self.password.append(new_password)
            return
    
    def _password_changer(self, old_password, new_password):
        if old_password in self.password:
            self.password.remove(old_password)
            self.password.append(new_password)
        else:
            return print("ERROR: password non presente")


class PasswordLV1(PasswordLV2):
    def __init__(self):
        self.password = PasswordLV2().password

    def _remove_password(self, old_password):
        if old_password in self.password:
            self.password.remove(old_password)
        else:
            return print("ERRORE: password non presente")


class PasswordLV0(PasswordLV1):
    def __init__(self, password):
        self.password = [password]


if __name__ == "__main__":
    test1 = PasswordLV0("ksdhsd")
    print(test1.password)

    test2 = PasswordLV2()
    test2.add_password("uvnud")

    test3 = PasswordLV1()
    print(test2.password)

    # test = PasswordLV2()
# 
    # test.add_password("snif8s9fn23")
    # print(test.password)
# 
    # test.add_password("jk43v689df")
    # print(test.password)
# 
    # test._password_changer('snif8s9fn23', "123stella")
    # print(test.password)
# 
    # test2 = PasswordLV1()
    # print(test2.password)
    # print(test._password_changer('jk43v689df', "123stella"))
# 
    # print(test2.password)




    