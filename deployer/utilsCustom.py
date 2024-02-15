import os
import subprocess
import constants


'''
Checks if an app is installed on the host system
'''
def isApp(name):
    from shutil import which
    return which(name) is not None



'''
Checks if Anvil is running
'''

def checkAnvil():
    print(constants.SEPARATOR)
    print("Checking that Foundry is installed...")
    #Check that Foundry is installed, and exit if not
    if not isApp("forge"):
        print("Foundry needs to be installed in order for this script to run correctly. Please install Foundry. Exiting...")
        exit()
    
    print("Foundry is installed...")
    print(constants.SEPARATOR)
    print ("Checking that Anvil is running...")

    #Check that anvil is running. Ignore grep. If anvil not running, then start
    anvil = os.popen('ps -aux | grep anvil | grep -v grep').read()

    if not anvil:
        print("Anvil development blockchain is not running. Starting Anvil...")
        subprocess.Popen('anvil', start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    else: 
        print("Anvil is running...")



'''
Gets the deployment address of the contract
'''
def getDeploymentAddress(output):
    needle = "Deployed to: "

    lines = output.splitlines()
    for line in lines:
        if line.startswith("Deployed to: "):
            deplymentAddress = line.replace(needle, "")
            return deplymentAddress
        

