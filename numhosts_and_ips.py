import ipaddress
import random

#Funció per a generar ip's
def generar_ip_amb_mascara():
	prefix=random.randint(15,28)
	ip_random=".".join(str(random.randint(0,255)) for _ in range(4))
	xarxa=ipaddress.IPv4Network(f"{ip_random}/{prefix}", strict=False)
	print("Generarem un lab amb la xarxa : " , xarxa)
	hosts=list(xarxa.hosts())
	return hosts, prefix


#Inici del programa
from Kathara.manager.Kathara import Kathara
from Kathara.model.Lab import Lab


print("/**")
print("*     _   __      _   _                                           _                   _       _        _____         _     __  ")
print("*    | | / /     | | | |                                         | |                 | |     | |   _  |_   _|       | |   /  | ")
print("*    | |/ /  __ _| |_| |__   __ _ _ __ __ _   _ __ __ _ _ __   __| | ___  _ __ ___   | | __ _| |__(_)   | | ___  ___| |_  `| | ")
print("*    |    \ / _` | __| '_ \ / _` | '__/ _` | | '__/ _` | '_ \ / _` |/ _ \| '_ ` _ \  | |/ _` | '_ \     | |/ _ \/ __| __|  | | ")
print("*    | |\  \ (_| | |_| | | | (_| | | | (_| | | | | (_| | | | | (_| | (_) | | | | | | | | (_| | |_) |    | |  __/\__ \ |_  _| |_")
print("*    \_| \_/\__,_|\__|_| |_|\__,_|_|  \__,_| |_|  \__,_|_| |_|\__,_|\___/|_| |_| |_| |_|\__,_|_.__(_)   \_/\___||___/\__| \___/")
print("*                                                                                                                              ")
print("*                                                                                                                              ")
print(" */")
u=input("Write your username:")
ip,mask=generar_ip_amb_mascara()
lab = Lab("Lab"+u)
nhosts=random.randint(2,8)
for i in range(1,nhosts):
	nom=u+str(i)
	print("Generant " , nom)
	n=lab.new_machine(nom, **{"image":"kathara/quagga"})
	lab.connect_machine_to_link(nom,"A")
	f1="/sbin/ifconfig eth0 "+str(random.choice(ip))+" up"
	f2=nom+".startup"
	print(f1, " " , f2)
	lab.create_file_from_list([f1],f2 )
Kathara.get_instance().deploy_lab(lab)


