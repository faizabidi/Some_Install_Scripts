#!/usr/bin/python

import subprocess

retcode = subprocess.call("virt-install "
						  "--connect qemu:///system "
						  "-n cloudera-vm "
						  "-r  8192 "
						  "--vcpus=4 "
						  "--disk path= "
						  "/home/faiz89/Images/cloudera-quickstart-vm-5.3.0"
						  "-0-kvm.qcow2, device=disk, bus=virtio,format=qcow2 "
						  "--ram 8192 "
						  "--vnc "
						  "--noautoconsole "
						  "--import", shell=True)

if retcode == 0:
	print("Successfully created a VM :)")
else:
	print("VM creation failed.") 			



