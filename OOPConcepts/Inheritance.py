from Constructor import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        # call the parent constructor
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return ChildImpl.num2 + self.num + self.summation()


obj = ChildImpl()
print(obj.getCompleteData())
