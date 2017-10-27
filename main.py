from itertools import groupby
from catch_id import CatchID
from catch_friends import CatchFriends


def PrintSimpleGraph(listOfDates):
    newListOfDates = [elem for elem, _ in groupby(listOfDates)]
    for x in newListOfDates:
        num = listOfDates.count(x)
        a = ''.join("#" for x in range(0, num))
        print(str(x) + a)




username = input()
user = CatchID(str(username))
#print(user.ID)

listOfFriends = CatchFriends(user.ID)
#print(listOfFriends.friends)

print('\n')
PrintSimpleGraph(listOfFriends.friends)
print('\n')

