import os

def main():
    print("Welcome to getting the requirements")
    choice = input("""
    1. Install pip
    2. Install kali-linux-all
    3. Install git
    4. All important single modules
    5.Clear
    6.Update
    Enter your choice: """)
    if choice == "1":
       pip()
    elif choice == "2":
       kali()
    elif choice == "3":
       git()
    elif choice == "4":
       single()
    elif choice == "5":
       clear()
    elif choice == "6":
       update()
def pip():
    try:
       os.system("sudo apt install python3-pip")
       main()
    except:
       print("Failed")
       main()

def kali():
    try:
       os.system("apt-get install kali-linux-all && kali-linux-full && kali-linux")
       main()
    except:
         try:
            os.system("apt-get install kali-linux")
            main()
         except:
            print("Failed")
            quit()
def git():
    try:
       os.system("apt-get install git")
       main()
    except:
       print("This didnt work")
       main()

def single():
    print("Most important pen testing tools you need")
    choice = input("""
    1.Hydra
    2.Metasploit
    3.John the ripper
    4.NMAP
    5.Hashcat
    6.WireShark
    7.Aircrack-ng
    8.Nessus
    9.Snort
    10.Nikto
    11.Yersinia
    12.Clear
    0.Exit
    Enter a choice: """)
    if choice == "1":
       hydra()
    elif choice == "2":
       metasploit()
    elif choice == "3":
       John()
    elif choice == "4":
       nmap()
    elif choice == "5":
       hashcat()
    elif choice == "6":
       wireshark()
    elif choice == "7":
       aircrack()
    elif choice == "8":
       Nessus()
    elif choice == "9":
       Snort()
    elif choice == "10":
       Nikto()
    elif choice == "11":
       Yersinia()
    elif choice == "12":
       clear1()
    elif choice == "0":
       Exit()
    else:
        print("Enter a valid choice")


def hydra():
    try:
       os.system("apt-get install hydra")
       single() 
    except:
       print("Could not find")
       single()

def metasploit():
    try:
       os.system("apt-get install metasploit-framework && postgresql")
       single()
    except:
       print("Not found")
       single()

def John():
    try:
      os.system("apt-get install john")
      single()
    except:
      print("Not found")
      single()

def nmap():
    try:
      os.system("apt-get install nmap")
      single()
    except:
      print("Not found")
      single()

def hashcat():
    try:
      os.system("apt-get install hashcat")
      single()
    except:
      print("Not found")
      single()

def wireshark():
    try:
      os.system("apt-get install hashcat")
      single()
    except:
      print("Not found")
      single()

def aircrack():
    try:
       os.system("apt-get install aircrack-ng")
       single()
    except:
       print("Not found")
       single()

def Nessus():
    try:
      os.system("apt-get install nessus")
      single()
    except:
      print("Not found")
      single()

def Snort():
    try:
      os.system("apt-get install snort")
      single()
    except:
      print("Not found")
      single()


def Nikto():
    try:
       os.system("apt-get install nikto")
       single()
    except:
       print("File not found")
       single()


def Yersinia():
    try:
       os.system("apt-get install yersinia")
       single()
    except:
       print("Not found")
       single()

def Exit():
    main()


def clear():
    os.system("clear")
    main()


def clear1():
    os.system("clear")
    single()

    
def update():
    try:
       f = open("easy.py","w+")
       john =os.system("git clone https://github.com/WHYSOEASY/EasyScript.git")
       main()
    except:
       print("Updated already or failed to update")
       main()
main()
