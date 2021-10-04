#GLOBAL FUNCTION IN FUNCTION of same variable (a)

a=5
def fun1():
    a=10
    def fun2():
        global a
        a=a+1
        print(a)
    print(a)
    fun2()
fun1()
print(a)
