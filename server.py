"""Atech Mock UI local preview server.
Run with: python server.py
"""
import http.server
import socketserver
import webbrowser
import os
import socket
import sys

# Ensure UTF-8 output if possible
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

DEFAULT_PORT = 8088
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def get_free_port(start_port=DEFAULT_PORT):
    for port in range(start_port, start_port + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return start_port

def run():
    port = get_free_port(DEFAULT_PORT)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), Handler) as httpd:
        url = f"http://localhost:{port}"
        print("=" * 65)
        print(f"  [ATECH] PROMPT-TO-PRODUCT MOCK UI SERVER RUNNING")
        print(f"  [ATECH] LOCAL URL: {url}")
        print("=" * 65)
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    run()
