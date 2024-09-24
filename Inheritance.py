class parent():
    def series(self,a,b):
        for i in range(a,b):
            print(i)
            
class child1(parent):
    def series1(self,a,b):
        for i in range(a,b):
            print(i)
             
class child2(child1):
    def series2(self,a,b):
        for i in range(a,b):
            print(i)

obj = child2()
obj.series(1,9)
obj.series1(1,12)
obj.series2(1,15)
