#!/usr/bin/env python3
import socket

ports = [55127, 9090, 7790, 8085]
print("Port Health Check (RAID-C44912)\n")
for port in ports:
    s = socket.socket()
    try:
        result = s.connect_ex(("localhost", port))
        print(f"Port {port}: {'UP' if result == 0 else 'DOWN'}")
    except Exception as e:
        print(f"Port {port}: DOWN - {e}")
    finally:
        s.close()
