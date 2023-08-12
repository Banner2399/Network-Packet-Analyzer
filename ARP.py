import scapy.all as scapy
import optparse


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress", dest="ip_address", help="Enter IP Address")
    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Enter IP Address")
    
    return user_input



def network_my_scanner(ip):

    arp_packet_request = scapy.ARP(pdst="192.168.0.119/24")
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packets = broadcast_packet/arp_packet_request
    (answred_list, unanwserd_list) = scapy.srp(combined_packets, timeout=1)
    answred_list.summary()

user_ip_address = get_user_input()
network_my_scanner(user_ip_address.ip_address)
