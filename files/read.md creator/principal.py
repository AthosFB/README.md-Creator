from time import sleep
infos = list()
langu = list()
account = str(input("Put the Name of you account: "))
insta = str(input("Put The Link Of your Instagram Account (N/A to don't put): "))
print("Put 3 Information of YOU!")
sleep(3)
for i in range(1, 4):
    infos.append(str(input(f"Put The {i}st Information: ")))
print(account, insta, infos)
lannum = int(input("how Many programming languages you know? "))
for l in range(1, lannum + 1):
    langu.append(str(input(f"Put The Name Of the {l}st language: ")))
