from requests import Session

def CheckPublicIP():
    try:
        with Session() as ses:
            res = ses.get("https://api.ipify.org/?format=json")
            if (res.status_code == 200):
                return res.json()["ip"]
            return None
    except:
        return None
    pass
    
def IsProxyWorking(proxy):
    try:
        with Session() as ses:
            ses.proxies.update(proxy)
            res = ses.get("https://api.ipify.org/?format=json")
            if (res.status_code == 200):
                if(res.json()["ip"] != CheckPublicIP() and CheckPublicIP != None):
                    return True
            return False
    except:
        return False
    pass

def PrintSuccess(message, username, *argv):
    print("[ OK ] ", end="")
    print("[", end="")
    print(username, end="")
    print("] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

# Spam 1
# Multilação/etc 2
# Drogas 3
# Nuds 4
# Grave 5
# Discurso Ilegal 6
# Assédio ou intimidação 7
# Imitação de identidade 8
# Criança 11

def PrintChoices():
    print("""    
    +----------------------------+--------+
    |        Motivo              | Numero |
    +----------------------------+--------+
    | Spam                       |      1 |
    | Multilação/etc             |      2 |
    | Drogas                     |      3 |
    | Nuds                       |      4 |
    | Grave                      |      5 |
    | Discurso Ilegal            |      6 |
    | Assédio ou intimidação     |      7 |
    | Imitação de identidade     |      8 |
    | Criança                    |     11 |
    +----------------------------+--------+
    """)

def GetInput(message, *argv):
    print("[ ? ] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    return input()

def PrintFatalError(message, *argv):
    print("[ X ] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

def PrintError(message, username, *argv):
    print("[ X ] ", end="")
    print("[", end="")
    print(username, end="")
    print("] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

def PrintStatus(message, *argv):
    print("[ * ] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

def PrintBanner():
    banner = """
  ──▄█████████████████████████▄──
  ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░█░█░█░░░░░░░░░░░░░░█████░░█
  █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
  ███████████▀▀░░░░░▀▀███████████
  █░░░░░░░██░░▄█████▄░░██░░░░░░░█
  █░░░░░░░██░██▀░░░▀██░██░░░░░░░█
  █░░░░░░░██░██░░░░░██░██░░░░░░░█
  █░░░░░░░██░██▄░░░▄██░██░░░░░░░█
  █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
  █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
  █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
  █░░░░BOT DE REPORT░░░░░░░░░░░░█
  █░░░░FEITO PELO SEU NENEM░░░░░█
  █░░░░EU TE AMO MTO MEU AMOR░░░█
  ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
  ──▀█████████████████████████▀──
 
    """
    print(banner)
    pass

def LoadUsers(path):
    ret = []
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.replace("\n", "").replace("\r","")
                user = line.split(" ")[0]
                password = line.split(" ")[1]
                ret.append({
                    "user": user,
                    "password": password
                })
                pass
            pass
        return ret
    except:
        PrintFatalError("'users.txt' Arquivo não encontrado!")
        exit(0)
    pass

def LoadProxies(path):
    ret = []
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.replace("\n", "").replace("\r","")
                ip = line.split(":")[0]
                port = line.split(":")[1]
                ret.append({
                    "ip": ip,
                    "port": port
                })
                pass
            pass
        return ret
    except:
        PrintFatalError("'proxy.txt' Arquivo não encontrado!")
        exit(0)
    pass
