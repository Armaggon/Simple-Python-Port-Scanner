#!/usr/bin/python3
import socket
import time
import os
import threading
import colorama
from colorama import Fore, Style

from queue import Queue
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()




square = f"{Fore.RED}[{Style.RESET_ALL}{Fore.BLUE}+{Style.RESET_ALL}{Fore.RED}]{Style.RESET_ALL}"




print (f"" + square + Fore.BLUE + " Welcome.")
colour1 = f"{Fore.RED}[{Style.RESET_ALL}"
colour2 = f"{Fore.RED}]{Style.RESET_ALL}"
print("[!] NOTE - If you do not get any results at the end that may mean the ports are filtered.")


scan_ = ""
scan_ = input(f"" + square + Fore.BLUE + " Do you wish to do a network scan for targets?[Y/N]: ")

if scan_ != "n" and scan_ != "N":
    os.system('arp-scan 192.168.1.0/24')

else:
    pass




target = input(f"{Fore.GREEN}[*] Enter the host to be scanned: {Style.RESET_ALL}")
t_IP = socket.gethostbyname(target)
time.sleep(1)
print("[+] Scanning...")
time.sleep(0.5)	
print (f"{Fore.GREEN}[!] Starting scan on host: {Style.RESET_ALL}", t_IP)
print("")

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print(f"{Fore.YELLOW}[+] Open port -{Style.RESET_ALL}", port)
      con.close()
   except:
      pass

def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = Queue()
startTime = time.time()
   
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for worker in range(1, 500):
   q.put(worker)
   
q.join()
print("")
print(f"{Fore.YELLOW}[-] Time taken:{Style.RESET_ALL}", time.time() - startTime)
