import ipaddress
import random

#Inici del programa
from Kathara.manager.Kathara import Kathara
from Kathara.model.Lab import Lab

u=input("Write your username:")
lab = Lab("Lab"+u)
available_os=["kathara/base", "kathara/quagga", "debian", "ubuntu", "ubuntu/apache", "gfarrasbal/reto3", "gfarrasbal/reto3b"]
nhosts=random.randint(6,12)
for i in range(1,nhosts):
	nom=u+str(i)
	print("Generant " , nom)
	n=lab.new_machine(nom, **{"image":random.choice(available_os)})
	lab.connect_machine_to_link(nom,"A")	
Kathara.get_instance().deploy_lab(lab)


