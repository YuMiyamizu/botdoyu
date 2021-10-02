# coding=utf-8
#!/usr/bin/env python3

""" 
Before changing the program and publishing it somewhere, please
Please note that this program is under GPLv3 license.
More information:
https://tr.wikipedia.org/wiki/gnu_genel_kamu_lisans%c4%b1
https://www.gnu.org/licenses/quick-guide-gplv3.html
"""

__author__ = "nenem : @yuh.nenem"
__license__ = "GPLv3"
__version__ = "0.1"
__status__ = "sendo feito"



from time import time, sleep
from random import choice
from multiprocessing import Process

from libs.utils import CheckPublicIP, IsProxyWorking
from libs.utils import PrintStatus, PrintSuccess, PrintError
from libs.utils import PrintBanner, GetInput, PrintFatalError
from libs.utils import LoadUsers, LoadProxies, PrintChoices

from libs.instaclient import InstaClient

USERS = []
PROXIES = []

def MultiThread(username, userid, loginuser, loginpass, proxy, reasonid):
    client = None
    if (proxy != None):
        PrintStatus("[" + loginuser + "]", "Login na sua conta!")
        client = InstaClient(
            loginuser,
            loginpass,
            proxy["ip"],
            proxy["port"]
        )
    else:
        PrintStatus("[" + loginuser + "]", "Login na sua conta!")
        client = InstaClient(
            loginuser,
            loginpass,
            None,
            None
        )
        
    client.Connect()
    client.Login()
    client.Spam(userid, username, reasonid)
    print("")

def NoMultiThread():
    for user in USERS:
        client = None
        if (useproxy):
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Login na sua conta!")
            client = InstaClient(
                user["user"],
                user["password"],
                proxy["ip"],
                proxy["port"]
            )
        else:
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Login na sua conta!")
            client = InstaClient(
                user["user"],
                user["password"],
                None,
                None
            )
        
        client.Connect()
        client.Login()
        client.Spam(userid, username, reasonid)
        print("")


if __name__ == "__main__":
    PrintBanner()
    PrintStatus("Loading users!")
    USERS = LoadUsers("./users.txt")
    PrintStatus("Loading Proxes!")
    PROXIES = LoadProxies("./proxy.txt")
    print("")

    username = GetInput("O nome de usuário da conta da qual você deseja reportar:")
    userid = GetInput("O número da conta da qual você deseja reportar:")
    useproxy = GetInput("Você quer usar proxy?? [Yes/No]:")
    if (useproxy == "Yes"):
        useproxy = True
    elif (useproxy == "No"):
        useproxy = False
    else:
        PrintFatalError("Por favor escolha entre 'Yes' or 'No'!")
        exit(0)
    usemultithread = GetInput("Você quer usar multithreading?? [Yes / No] (Não utilize se seu celular estiver muito lento ou sobrecarregado!):")
    
    if (usemultithread == "Yes"):
        usemultithread = True
    elif (usemultithread == "No"):
        usemultithread = False
    else:
        PrintFatalError("Por favor escolha entre 'Yes' or 'No'!")
        exit(0)
    
    PrintChoices()
    reasonid = GetInput("Selecione um dos motivos para a reportagem acima (ex: 1 para spam):")

    
    
    
    print("")
    PrintStatus("Iniciando!")
    print("")

    if (usemultithread == False):
        NoMultiThread()
    else:
        for user in USERS:
            p = Process(target=MultiThread,
                args=(username,
                    userid,
                    user["user"],
                    user["password"],
                    None if useproxy == False else choice(PROXIES),
                    reasonid
                )
            )
            p.start() 
    

    
