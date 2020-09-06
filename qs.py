from sys import argv
from datetime import datetime
msg = """
qs diğer adıyla QuickScript kullan at scriptleri yazabileceğiniz bir araçtır. Python ile yazıldı.

[HOW TO USE]

qs [OPTIONS] [FILE TYPE]

qs c
qs py
qs cpp

[OPTIONS]
--help\tBu komutu gösterir. 
"""
if "--help" in argv[1:] or not argv[1:]:
	print(msg)
else:
	try:
		with open(f"{datetime.now()}-QuickScript.{argv[1]}".replace(":","."),"w") as f:
			f.write(" ")
			f.close()
	except Exception as e:
		x = input("Bir şeyler ters gitti hatayı görmek ister misin(Y/N): ")
		if x == "Y" or x == "y": print(e)
		elif x == "N" or x == "n": exit()
		else: exit()
			
			




