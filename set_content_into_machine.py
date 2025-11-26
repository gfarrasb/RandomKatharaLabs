import ipaddress
import random
import os

from Kathara.manager.Kathara import Kathara
from Kathara.model.Lab import Lab

nom=input("Write your username:")
lab = Lab("Lab")
a1=lab.new_machine("a1", **{"image":"kathara/base"})
lab.connect_machine_to_link("a1","A")	

#Method 1
comandes=[]
comandes.append("/sbin/ifconfig eth0 10.10.10.10 up")
comandes.append("echo hello > /root/test.txt")
lab.create_file_from_list(comandes,"a1.startup")

#Method 2
a1.create_file_from_path(os.path.join("./","file-to-be-copied.txt"), "/files/transferred-file.txt")


Kathara.get_instance().deploy_lab(lab)


