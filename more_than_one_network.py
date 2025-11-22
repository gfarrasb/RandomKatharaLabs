import ipaddress
from Kathara.manager.Kathara import Kathara
from Kathara.model.Lab import Lab
import random

#Funció per a generar ip's
def generar_ip_amb_mascara():
	prefix=random.randint(15,28)
	ip_random=".".join(str(random.randint(0,255)) for _ in range(4))
	xarxa=ipaddress.IPv4Network(f"{ip_random}/{prefix}", strict=False)
	return xarxa


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
#u=input("Write your username:")
u="gfarrasb"
lab = Lab("Lab"+u)
networkzones=["A","B","C","D", "E", "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z"]
nnetworks=random.randint(2,len(networkzones))
xarxes=[]
ips=[]
for n in range(0,nnetworks):
	xarxes.append(generar_ip_amb_mascara())

for xarxa in range(0,len(xarxes)):
	print(str(xarxes[xarxa]) + " --> " + networkzones[xarxa] )
	
nhosts=random.randint(2,100)
print("Total hosts " + str(nhosts))
for i in range(1,nhosts+1):
	x=random.choice(xarxes)
	ip=random.choice(list(x.hosts()))	
	iface=ipaddress.IPv4Interface(f"{ip}/{x.prefixlen}")
	ips.append(iface)

print(ips)
i=1
while i<=nhosts and len(ips)>0:
	nom=u+str(i)
	#print("Generating " , nom, " host....")
	f2=nom+".startup"
	n=lab.new_machine(nom, **{"image":"kathara/quagga"})
	ipaleatoria=random.choice(ips)		
	f1="/sbin/ifconfig eth0 "+str(ipaleatoria)+" up;"
	#print("ip address " , ipaleatoria)
	#print(nom, " " , ipaleatoria)
	ips.remove(ipaleatoria)				
	for zz in range(0,len(xarxes)):
		if ipaleatoria.ip in xarxes[zz]:
			lab.connect_machine_to_link(nom,networkzones[zz])
	if len(ips)>0:
		ipaleatoria2=random.choice(ips)		
		if random.randint(0,1)==1 and ipaleatoria2.network!=ipaleatoria.network:
			f1=f1 + "/sbin/ifconfig eth1 "+str(ipaleatoria2)+" up;"
			#print("ip address " , ipaleatoria2)
			for zz in range(0,len(xarxes)):
				if ipaleatoria2.ip in xarxes[zz]:
					lab.connect_machine_to_link(nom,networkzones[zz])			
			ips.remove(ipaleatoria2)				
		#print("ips disponibles " , ips)
	#print(f1)
	lab.create_file_from_list([f1],f2)
	i=i+1
			
Kathara.get_instance().deploy_lab(lab)



