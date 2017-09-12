oldpass = input("old pass?")
newpass = input("new pass?")
def new_password(old, new):
    if old != new and len(new) >= 6 and str("abcdefghijklmnopqrstuvwqyx") in new:
        return True
    else:
        return False

print(new_password(oldpass, newpass))
b