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


def test_create_hacker():
    print("\n--- Test: Create Hacker ---")
    hacker = Hacker("ZeroTrace")
    print(hacker)

def test_hacker_exposed():
    print("\n--- Test: Hacker Exposed ---")
    # Instantiate target Rigs
    rig1 = Rig("BigRig")
    rig2 = Rig("RobsRig")
    hacker = Hacker("ZeroTrace")
    print(hacker)
    hacker.acquire_rig("GhostRig")
    hacker.rig.store_asset(Asset("Data Spike"))
    hacker.rig.store_asset(Asset("Data Spike"))
    hacker.rig.store_asset(Asset("Data Spike"))
    print(hacker.rig)
    hacker.launch_attack(rig1)
    hacker.launch_attack(rig1)
    hacker.launch_attack(rig1)
    hacker.launch_attack(rig2)
    hacker.launch_attack(rig2)
    print(hacker)


def test_increase_decrease_trace_level():
    print("\n--- Test: increase trace level ---")
    hacker = Hacker("ZeroTrace")
    print(hacker)
    hacker.increase_trace_level()
    print(hacker)
    hacker.decrease_trace_level()
    print(hacker)
    hacker.decrease_trace_level()
    print(hacker)


def test_acquire_rig():
    print("\n--- Test: Acquire Rig ---")
    hacker = Hacker("ZeroTrace")
    print(hacker)
    hacker.acquire_rig("GhostRig")
    print(hacker)
    print(hacker.rig)


def test_encrypt_decrypt_asset():
    print("\n--- Test: Encrypt Asset in Hacker Inventory---")
    hacker = Hacker("ZeroTrace")
    print(hacker)
    hacker.encrypt_asset("CryptoToken")
    print(hacker)
    hacker.decrypt_asset("CryptoToken")
    print(hacker)


def test_scan_inventory():
    print("\n--- Test: Scann Inventory---")
    hacker = Hacker("ZeroTrace")
    print(hacker)
    token = hacker.scan_inventory("CryptoToken")
    print(hacker)
    print(token)
    hacker.decrypt_asset("Hardware Patch")
    print(hacker)


def test_launch_attack():
    print("\n--- Test: Launch Attack ---")
    # Instantiate Hackers
    hacker1 = Hacker("ZeroTrace")
    hacker1.acquire_rig("BigRig")
    print(hacker1)

    # Instantiate Rigs
    rig1 = Rig("RobsRig")
    print(rig1)

    hacker1.launch_attack(rig1)
    print(rig1)
    hacker1.launch_attack(rig1)
    print(rig1)
    print(hacker1.rig)


def test_extract_assets():
    print("\n--- Test: Extract Assets ---")
    hacker = Hacker("ZeroTrace")
    hacker.acquire_rig("GhostRig")
    target_rig = Rig("BigRig")
    target_rig.broken_state = True
    hacker.extract_assets(target_rig)
    print(hacker)
    print(target_rig)

def test_store_retrieve_asset():
    print("\n--- Test: Store Asset in Rig storage ---")
    hacker = Hacker("ZeroTrace")
    hacker.acquire_rig("GhostRig")
    print(hacker)
    print(hacker.rig)
    hacker.rig.store_asset(Asset("Security Chip"))
    print(hacker.rig)
    hacker.retrieve_asset("Security Chip")
    print(hacker.rig)
    print(hacker)
    hacker.store_asset("Security Chip")
    print(hacker)
    print(hacker.rig)


def test_hit_repair():
    print("\n--- Test: Hit Rig ---")
    rig = Rig("GhostRig")
    print(rig)
    rig.hit()
    print(rig)
    rig.hit()
    print(rig)
    print("\n--- Test: Repair Rig ---\n")
    rig.repair()
    print(rig)


def test_upgrade_rig_without_patch():
    print("\n--- Test: Upgrade Rig ---")
    hacker = Hacker("ZeroTrace")
    hacker.acquire_rig("GhostRig")
    print(hacker.rig)
    hacker.rig.upgrade()
    print(hacker.rig)


def test_upgrade_rig():
    print("\n--- Test: Upgrade Rig ---")
    rig = Rig("GhostRig")
    print(rig)
    rig.upgrade()
    rig.store_asset(Asset("Hardware Patch"))
    print(rig)
    rig.upgrade()
    print(rig)


def test_generate_asset():
    print("\n--- Test: Generate Asset ---")
    rig = Rig("GhostRig")
    print(rig)
    rig.generate_asset()
    print(rig)


# Test Asset class
def test_asset_class():
    print("\n--- Test: Asset class ---")
    data_spike = Asset("Data Spike")
    print(data_spike)
    data_spike.encrypted = True
    print(data_spike)
    data_spike.encrypted = False
    print(data_spike)

if __name__ == "__main__":
    # Test Asset class
    test_asset_class()

    # Test Rig class
    # test_hit_repair()
    # test_upgrade_rig()
    # test_generate_asset()
    # test_store_retrieve_asset()

    # Test Hacker class
    # test_create_hacker()
    # test_acquire_rig()
    # test_increase_decrease_trace_level()
    # test_hacker_exposed()
    # test_encrypt_decrypt_asset()
    # test_store_retrieve_asset() # Need to add this for the Hacker class
    # test_scan_inventory()
    # test_extract_assets()

