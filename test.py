n: int = int(input())
lis: list = []
for _ in range(n):
    ni = input()
    lis.append(ni)
n2 = int(input())
req_list = []
for _ in range(n2):
    req = input()
    req_list.append(req.upper())

for i in range(len(req_list)):
    r = lis[i]
    if req_list[0].upper() not in r.upper():
        del lis[i]

print(*lis, sep='\n')
