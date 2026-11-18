import random
from datetime import datetime, timezone

DEVICES = [
    "192.168.1.10",
    "192.168.1.11",
    "192.168.1.12",
    "192.168.1.15"
]

SERVERS = [
    ("142.250.183.14", "google.com"),
    ("157.240.22.35", "facebook.com"),
    ("104.18.32.47", "example.com"),
    ("1.1.1.1", "cloudflare-dns.com")
]

PROTOCOLS = ["TCP", "UDP", "DNS"]

def generate_event():
    source_ip = random.choice(DEVICES)
    destination_ip, domain = random.choice(SERVERS)

    protocol = random.choice(PROTOCOLS)

    bytes_sent = random.randint(10, 50000)
    bytes_received = random.randint(500, 200000)

    duration = random.randint(10, 50000)

    event= {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "src_ip": source_ip,
        "dst_ip": destination_ip,
        "protocol": protocol,
        "domain": domain,
        "bytes_sent": bytes_sent,
        "bytes_received": bytes_received,
        "duration_ms": duration
    }

    return event
