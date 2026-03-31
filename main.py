from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

# הגדרת צבעים
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("security_log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            
            # בדיקת פורט 80 (HTTP לא מאובטח)
            if tcp_layer.dport == 80:
                alert_msg = f"ALERT: Unsecured HTTP from {src_ip} to {dst_ip}"
                print(f"{RED}[!] {alert_msg}{RESET}")
                
                # חשיפת תוכן החבילה (Deep Packet Inspection)
                if packet.haslayer(Raw):
                    payload = packet.getlayer(Raw).load
                    try:
                        # מנסים להפוך את המידע לטקסט קריא
                        decoded_data = payload.decode('utf-8', errors='ignore')
                        print(f"    {CYAN}Data Snippet:{RESET} {decoded_data[:100].strip()}...")
                    except:
                        print(f"    {CYAN}Data Snippet:{RESET} [Binary/Encrypted Data]")
                
                log_alert(alert_msg)
            
            elif tcp_layer.dport == 443:
                # מדפיס HTTPS רק כדי שתראה שהתנועה המאובטחת עדיין עוברת
                print(f"{GREEN}[TCP/HTTPS] {src_ip} --> {dst_ip}{RESET}")

        elif packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            if udp_layer.dport == 53:
                print(f"{YELLOW}[DNS Query] {src_ip} searching for a domain...{RESET}")

def main():
    print(f"{YELLOW}--- Deep Packet Inspector Started ---{RESET}")
    print("Monitoring all IP traffic. Alerts saved to 'security_log.txt'")
    print("Press Ctrl+C to stop.\n")
    
    try:
        sniff(filter="ip", prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print(f"\n{YELLOW}--- Monitoring Stopped ---{RESET}")

if __name__ == "__main__":
    main()