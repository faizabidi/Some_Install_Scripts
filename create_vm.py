#!/usr/bin/python

import subprocess

retcode = subprocess.call("virt-install \
				-n ubuntu1404 \
				-r 8192 \
				--disk path=/var/lib/libvirt/images/ubuntu1404.img,bus=virtio,size=8 \
				-c /home/faiz89/Downloads/ubuntu-14.04.5-server-amd64.iso \
				--network network=default,model=virtio \
				--graphics vnc,listen=0.0.0.0 \
				--noautoconsole -v", shell=True)

if retcode == 0:
	print("Successfully created a VM :)")
    print("Type 'vncviewer localhost:0' to connect to the VM, and finish installtion.")
else:
	print("VM creation failed.") 			



