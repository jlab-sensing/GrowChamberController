#!/usr/bin/env python3
import telnetlib, time, sys, os

HOST = os.environ.get("LF11_HOST", "192.168.1.123")
PORT = int(os.environ.get("LF11_PORT", "50123"))
LEVEL = int(os.environ.get("LF11_LEVEL_ON", "1000"))  # 0..2000

def send(tn, cmd):
    tn.write((cmd + "\r\n").encode("ascii"))
    time.sleep(0.1)
    _ = tn.read_very_eager()  # ignore output

def main():
    if not (0 <= LEVEL <= 2000):
        print("LEVEL must be 0..2000", file=sys.stderr)
        sys.exit(2)
    try:
        with telnetlib.Telnet(HOST, PORT, timeout=5) as tn:
            send(tn, "?")
            send(tn, "ecr! 1")
            send(tn, "mode m")
            send(tn, f"lo {LEVEL}")
            send(tn, "ls all")
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
