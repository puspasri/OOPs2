class Employee:

    def __init__(self):
        print("created")

    def __del__(self):
        print("deleated")
def create():
    object=Employee()
    print(object)

create()
    