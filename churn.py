filechurns = {}
with open("churns","r") as inputfile:
    for line in inputfile.readlines():
        if not line in filechurns:
            filechurns[line] = 0
        filechurns[line] += 1
for file in filechurns.keys():
    if filechurns[file] > 20:
        if not "csproj" in file and not "CHANGELOG" in file:
            print("%d commits: %s" % (filechurns[file],file))
        