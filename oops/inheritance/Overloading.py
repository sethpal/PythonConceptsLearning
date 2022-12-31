class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


def func(myObj):
    myObj.capital()
    myObj.language()
    myObj.type()

def function(string ):
    string.capital()

obj_ind = India()
obj_usa = USA()

function(obj_ind)
function(obj_usa)