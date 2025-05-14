#!/usr/bin/env python3
import subprocess, sys

def main():
    try:
        subprocess.check_call(["pre-commit", "install", "--install-hooks"])
        print("✅ pre-commit hooks installed")
    except subprocess.CalledProcessError as e:
        print("❌ pre-commit install failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()