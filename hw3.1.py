
class Bank:
    def __init__(self, __name, balanse):
        self.__name = __name
        self.balanse = balanse
    def __str__(self):
        return f' name is: {self.__name}\n' \
               f'balanse is: {self.balanse}'



    def set_name(self,name):
        self.__name = name

    def get_name(self):
        print(self.__name)




    def set_balanse(self, balanse):

        self.balanse = balanse

    def get_balanse(self):
        print(self.balanse)




aku = Bank("Aku",100)
sake = Bank("Sake",100)
take = Bank("Take",100)


sake.get_balanse()
sake.set_balanse(122)
sake.get_balanse()
print(sake)


class Bank:
    def __init__(self, __name, balanse):
        self.__name = __name
        self.balanse = balanse
    def __str__(self):
        return f' name is: {self.__name}\n' \
               f'balanse is: {self.balanse}'



    def set_name_balanse(self,name,balanse):
        self.__name = name
        self.balanse = balanse

    def get_name_balanse(self):
        print(self.__name)
        print(self.balanse)


aku = Bank("Aku",100)

aku.get_name_balanse()
aku.set_name_balanse("beku",333)
aku.get_name_balanse()
print(aku)



