#!/usr/bin/env python3
import os, socket
output=f"""=== System Info ===
Hostname: {socket.gethostname()}
Current user: {os.getlogin()}
Current directory: {os.getcwd()}
Files in this folder: {str(', ').join(os.listdir('.'))}
"""
print(output)

