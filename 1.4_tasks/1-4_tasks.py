### 1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat = list(nat.split())
nat[7] = "GigabitEthernet 0/1"
" ".join(nat)

### 2
MAC = "AAAA:BBBB:CCCC"
MAC2 = "AA:AA:BB:BB:CC:CC"

def mac_converter(str(MAC)):
    if len(MAC) == 14:
        MAC = list(MAC)
        MAC[4] = "."
        MAC[9] = "."
        return "".join(MAC)
    elif len(MAC) == 17:
        MAC = list()
        MAC[2] = ""
        MAC[5] = "."
        MAC[8] = "."
        MAC[11] = "."
        MAC[14] = "."
        return "".join(MAC)
    else: 
        print("Unexpected format")
        return 1

