"""
File: main.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
from Asset import Asset
from Rig import Rig

def test_acquire_rig():
    print("\n--- Test: Acquire Rig ---")
    hacker = Hacker("ZeroTrace")
    hacker.acquire_rig("GhostRig")
    print(hacker)
    print(hacker.rig)

def test_upgrade_rig():
    pass

def test_upgrade_without_rig():
    pass

def test_encrypt_decrypt():
    pass

def test_encrypt_without_chip():
    pass

def test_launch_attack():
    pass

def test_attack_with_high_trace():
    pass

def test_extract_assets():
    pass

def test_store_and_retrieve():
    pass

def test_scan_inventory():
    pass

if __name__ == "__main__":
    test_acquire_rig()