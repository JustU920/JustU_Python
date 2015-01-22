__author__ = 'zhoumin'
class Function:
    def __init__(self):
        print("Function init...")

    def getListAllVaules(items):
        for item in items:
            if isinstance(item, list):
                Function.getListAllVaules(item)
            else:
                print(item)