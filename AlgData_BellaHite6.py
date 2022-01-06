# Part A
hashTable = {}
for i in range(0, 35):
    hashTable[i] = None
ids = []
a = 123456
for i in range(0, 32):
    ids.append(a + i)
print(ids)

probingCount1 = 0
pct = []
for i in range(0, 32):
    index = ids[i] % 31
    if hashTable[index] is None:
        hashTable[index] = ids[i]
    elif hashTable[index] is not None:  # collision handling
        for j in range(0, len(hashTable)):
            probingCount1 += 1
            if hashTable[j] is None:
                hashTable[j] = ids[i]
                break
    pct.append(probingCount1)
avgprobe = 0
for i in pct:
    avgprobe +=i
avgprobe = avgprobe/len(hashTable)
print("average probing count =", avgprobe)
print(hashTable)

k = 0
probeCount = 0
# key = 6
# key = 50
key = 35
# key = 8
while k != key:
    if key >= len(hashTable):
        print("key Does Not Exist")
        break
    if hashTable[key] == None:
        print("key Does Not Exist")
        break
    else:
        k = hashTable[key] % 31
        k = key
        probeCount += 1
    #print(probeCount)
if probeCount > 0:
    print("key found")



# # Part B
# hashTable = {}
# for i in range(0, 50):
#     hashTable[i] = None
# ids = []
# a = 123456
# for i in range(0, 32):
#     ids.append(a + i)
# print(ids)
#
# probingCount1 = 0
# pct = []
# for i in range(0, 32):
#     index = ids[i] % 47
#     if hashTable[index] is None:
#         hashTable[index] = ids[i]
#     elif hashTable[index] is not None:  # collision handling
#         for j in range(0, len(hashTable)):
#             probingCount1 += 1
#             if hashTable[j] is None:
#                 hashTable[j] = ids[i]
#                 break
#     pct.append(probingCount1)
# avgProbe = 0
# for i in pct:
#     avgProbe +=i
# avgProbe = avgProbe / len(hashTable)
# print("average probing count =", avgProbe)
# print(hashTable)
#
# k = 0
# probeCount = 0
# # key = 6
# # key = 49
# # key = 34
# # key = 8
# while k != key:
#     if key >= len(hashTable):
#         print("key Does Not Exist")
#         break
#     if hashTable[key] == None:
#         print("key Does Not Exist")
#         break
#     else:
#         k = hashTable[key] % 47 #len(hashTable)
#         k = key
#         probeCount += 1
#     print(probeCount)
# if probeCount > 0:
#     print("key found")