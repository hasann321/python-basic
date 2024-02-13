myDict = {"you": "Yes its you", "my": "belongs to me", "dict": "beloved dictionary"}
# print(type(myDict))
# print(myDict)

# print(myDict["dict"])

# myKeys = myDict.keys()
# myValues = myDict.values()
# print(type(myKeys), "\n", myKeys)
# print(type(myValues), "\n", myValues)

# myItems = myDict.items()
# print(type(myItems))
# print(myItems)

# for value in myDict.values():
#     print(value)

for x, y in myDict.items():
    print(x, "=>", y)
