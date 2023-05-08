from Database import Database
from Notebook import Notebook
from UserFilter import UserFilter

notebook = Notebook(model="model0", ram=16, disk=256)
print(notebook)
print()

data = Database()
for i in range(0,10):
    data.addNew(data.createRandom())

filter = UserFilter(data.base)
filter.printbase()
while filter.userHere:
    filter.askFilter()

