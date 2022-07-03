
#Q4
def ispangram(string):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in alpha :
        if i not in string.lower():
            return False
    return True
string=input()
print(ispangram(string))