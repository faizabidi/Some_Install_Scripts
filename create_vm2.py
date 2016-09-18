#!/usr/bin/python

import subprocess

<<<<<<< HEAD
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
=======
sudo virt-install --connect qemu:///system -n vm10 -r 512 --vcpus=2 -f ~/vm10.qcow2 -s 12 -c /dev/cdrom --vnc --noautoconsole --os-type linux --accelerate --network=bridge:br0 --hvm

retcode = subprocess.call("virt-install \
				
                -n ubuntu1404 \
				-r 2048 \
				--disk path=/var/lib/libvirt/images/ubuntu1404.img,bus=virtio,size=8 \
				-c /home/faiz89/Downloads/ubuntu-14.04.5-server-amd64.iso \
				--network network=default,model=virtio \
				--graphics vnc,listen=0.0.0.0 \
				--noautoconsole -v", shell=True)
>>>>>>> 4f5bf8ac6b805124a3cceb5fb75e95268076aa75

if retcode == 0:
	print("Successfully created a VM :)")
else:
	print("VM creation failed.") 			



