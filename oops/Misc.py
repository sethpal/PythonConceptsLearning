def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

def myFun1(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


def myFun2(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun2(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun2(**kwargs)

# Driver code
myFun1(first='Geeks', mid='for', last='Geeks')


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')