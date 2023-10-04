from netaddr import *

hexChars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"] 

class generic_mac(mac):
    def __init__(self, formatType):
        self.format = formatType

#class mac_comware(mac_cisco): pass
#mac_comware.word_sep = '-'
#mac_comware.word_size = 16

#class mac_procurve(mac_pgsql): pass
#mac_procurve.word_sep = '-'
#mac_procurve.word_size = 24


def CheckMac(mac1):  #returns false if valid
    badMac=False
    mac2=mac1.translate(str.maketrans('', '',  '-:_.'))  #strips normal chars
    if len(mac2) < 12:
        badMac=True
    for i in mac2.lower():
        if i not in hexChars :
            badMac=True
    return badMac

def printMacs(mac1):
    if CheckMac(mac1) == True:
        print(mac1 + " is NOT a valid MAC")
    else:
        print ("original: " + str(mac1))
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
