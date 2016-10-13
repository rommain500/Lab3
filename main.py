from base import BaseClient
from methods import FriendsGet
from methods import UserGet

r = UserGet('178981827')
b = r.execute()
print(b)

f = FriendsGet(b);
a = f.execute()
print(a)
list_date = sorted(list(a.keys()), reverse=True)
for i in list_date:
    print(2016 - int(i), end=": ")
    print("#" * int(a[i]), end="")
    print()

