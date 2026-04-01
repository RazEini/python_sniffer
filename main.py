import threading
import logging
from queue import Queue, Empty
from datetime import datetime, timedelta
from collections import defaultdict
from scapy.all import sniff, IP, TCP, UDP, Raw, DNSQR

class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.FileHandler("network_security.log"), logging.StreamHandler()]
)

class NetworkGuardian:
    def __init__(self):
        self.packet_queue = Queue()
        self.running = True
        self.DOS_THRESHOLD = 50        
        self.SCAN_THRESHOLD = 15       
        self.whitelist = set() 
        self.blacklist = {}            
        self.syn_counts = defaultdict(int)
        self.port_history = defaultdict(set)
        self.last_cleanup = datetime.now()

    def _log_alert(self, level, msg, color=Colors.RESET):
        logging.info(f"{color}[{level}] {msg}{Colors.RESET}")

    def is_isolated(self, ip):
        if ip in self.blacklist:
            if datetime.now() < self.blacklist[ip]:
                return True
            else:
                del self.blacklist[ip]
        return False

    def analyze_packet(self, pkt):
        if not pkt.haslayer(IP):
            return

        src_ip = pkt[IP].src
        if src_ip in self.whitelist or self.is_isolated(src_ip):
            return

        # 1. זיהוי שאילתות DNS (שמות אתרים) - זה יוסיף הרבה "חיים" למסך
        if pkt.haslayer(DNSQR):
            query = pkt[DNSQR].qname.decode(errors='ignore')
            # נתעלם משאילתות פנימיות משעממות של ווינדוס
            if not query.endswith(".local."):
                self._log_alert("DNS", f"Device {src_ip} is looking for: {query}", Colors.CYAN)

        # 2. זיהוי DoS (SYN Flood)
        if pkt.haslayer(TCP) and pkt[TCP].flags == "S":
            self.syn_counts[src_ip] += 1
            if self.syn_counts[src_ip] > self.DOS_THRESHOLD:
                self.blacklist[src_ip] = datetime.now() + timedelta(minutes=5)
                self._log_alert("CRITICAL", f"!!! DoS DETECTED: Isolating {src_ip} !!!", Colors.RED)

        # 3. זיהוי סריקת פורטים
        dst_port = pkt[TCP].dport if pkt.haslayer(TCP) else (pkt[UDP].dport if pkt.haslayer(UDP) else None)
        if dst_port:
            self.port_history[src_ip].add(dst_port)
            if len(self.port_history[src_ip]) > self.SCAN_THRESHOLD:
                self._log_alert("WARNING", f"Port Scan detected from {src_ip}", Colors.YELLOW)
                self.port_history[src_ip].clear()

        # 4. Deep Packet Inspection (DPI)
        if pkt.haslayer(Raw):
            try:
                payload = pkt[Raw].load.decode('utf-8', errors='ignore').lower()
                suspicious = ["admin", "password", "etc/passwd", "select * from"]
                for word in suspicious:
                    if word in payload:
                        self._log_alert("SECURITY", f"Suspicious keyword '{word}' detected from {src_ip}", Colors.MAGENTA)
            except:
                pass

    def packet_worker(self):
        while self.running:
            try:
                packet = self.packet_queue.get(timeout=1)
                self.analyze_packet(packet)
                self.packet_queue.task_done()
            except Empty:
                continue
            
            if datetime.now() - self.last_cleanup > timedelta(minutes=1):
                self.syn_counts.clear()
                self.port_history.clear()
                self.last_cleanup = datetime.now()

    def start(self):
        print(f"{Colors.CYAN}NetworkGuardian Engine Starting...{Colors.RESET}")
        worker = threading.Thread(target=self.packet_worker, daemon=True)
        worker.start()

        print(f"{Colors.GREEN}[*] Worker Thread active. Sniffing all traffic...{Colors.RESET}")
        try:
            # הורדנו את הפילטר "ip" כדי לתפוס גם DNS (שמשתמש ב-UDP) וגם IPv6
            sniff(prn=lambda x: self.packet_queue.put(x), store=0)
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")
        except KeyboardInterrupt:
            self.running = False

if __name__ == "__main__":
    guardian = NetworkGuardian()
    guardian.start()