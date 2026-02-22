#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
def menu():
	try:
		while True:
			os.system("figlet PORT SCANNER")
			print(""" 
PORT SCAN
		
1)Fast Scan
2)Service Scan
3)Operating System Info
4)All Of Them

			""")
	
			islemno= input("Enter Number:")
			if islemno.lower() == 'q':
				print("Exiting...")
				break
			if islemno in ["1", "2", "3", "4"]:	
				if(islemno == "1"):
					hedef_ip = input("Enter target IP: ") 
					print("Scanning...")
					os.system("nmap " + hedef_ip)
				elif(islemno == "2"):
					hedef2 = input("Enter target IP: ")
					print("Scanning...")
					os.system("nmap -sS -sV " + hedef2)
				elif(islemno == "3"):
					hedef3 = input("Enter target IP: ")
					print("Scanning...")
					os.system("nmap -O " + hedef3)
				elif(islemno == "4"):
					hedef4 = input("Enter target IP: ")
					print("Scanning...")
					os.system("nmap -O -sS -sV " + hedef4)
				print("Scan Completed")
				input("Press Enter to see Main Menu")
			else:
				print("FALSE INPUT")	
				input("Press enter if you want to continue")
	except KeyboardInterrupt:
		print(" Exiting....")
if __name__ == "__main__":
	menu()
