import os
import sys


def bind():
	os.system("python /home/dpdk/dpdk-2.0.0/tools/dpdk_nic_bind.py -b igb_uio 0000:00:07.0 0000:00:06.0");
	return;

def unbind():
	os.system("python /home/dpdk/dpdk-2.0.0/tools/dpdk_nic_bind.py -u 00:06.0 00:07.0");
	os.system("python /home/dpdk/dpdk-2.0.0/tools/dpdk_nic_bind.py -b i40evf 00:06.0 00:07.0")
	return;

if (sys.argv[1] == "u"):
        unbind();
elif (sys.argv[1] =="b"):
        bind();

