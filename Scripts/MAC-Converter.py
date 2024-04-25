from netaddr import *

hexChars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"] 

def checkMac(*args:str) -> bool:
    '''
    Check if a supplied MAC address has a valid format. Helper function.
    '''
    for arg in args:
        arg=arg.translate(str.maketrans('', '',  '-:_.'))  #cleans format to only hex chars
        if len(arg) < 12:
            badMac=True
        for i in mac2.lower():
            if i not in hexChars :
                badMac=True
        return badMac

def convertMac(*args:str, target:str = 'bare') -> None:
    for arg in args:
        if CheckMac(arg) == True:
            print(arg + " is NOT a valid MAC")
            return None
        if target == 'mac_cisco':
            print ("Cisco format: " +str(EUI(arg, dialect = mac_cisco))
        if target == 'mac_unix_expanded':
            return str(EUI(arg, dialect = mac_unix_expanded))
        if target == 'psql':
            return str(EUI(arg, dialect = mac_pgsql))
        if target == 'unix':
            return str(EUI(arg, dialect = mac_unix))
        if target == 'eui':
            return str


        else:
            print ("original: " + str(arg))
            print ("mac_cisco: " + str(EUI(mac1, dialect = mac_cisco)))
            print ("mac_unix_expanded: " + str(EUI(mac1, dialect = mac_unix_expanded)))
            print ("mac_bare: " + str(EUI(mac1, dialect = mac_bare)))
            print ("mac_pgsql: " + str(EUI(mac1, dialect = mac_pgsql)))
            print ("mac_unix: " + str(EUI(mac1, dialect = mac_unix)))
            print ("mac_eui: " + str(EUI(mac1)))
            print ("mac_comware: " + str(EUI(mac1, dialect = mac_comware)))
            print ("mac_procurve: " + str(EUI(mac1, dialect = mac_procurve)))
            try:   #needed because easy to get an exception when a MAC isn't registered in OUI db
                print (EUI(mac1).oui.registration().org)
            except Exception:
                pass
                print ("can't find MAC in database")


printMacs(input("mac?"))
