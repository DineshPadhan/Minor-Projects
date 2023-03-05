from scapy.all import ARP,Ether,srp

# define the network range to scan
target_ip = "192.168.1.0/24"

# create ARP packet
arp_request = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target_ip)

# send ARP request and capture response
responses, _ = srp(arp_request, timeout=2, verbose=0)

# print results
print("IP\t\t\tHostname")
print("-" * 40)
for response in responses:
    ip_address = response[1].psrc
    hostname = response[1].hwsrc
    print(f"{ip_address}\t\t{hostname}")
