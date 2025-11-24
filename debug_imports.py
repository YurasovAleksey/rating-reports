import sys
import os

print("=== Python Path ===")
for path in sys.path:
    print(f"  {path}")

print("\n=== Virtual Environment ===")
print(f"VENV: {os.path.exists('.venv')}")
if os.path.exists('.venv'):
    site_packages = [
        '.venv/lib/python3.11/site-packages',
        '.venv/lib/python3.10/site-packages', 
        '.venv/Lib/site-packages'  # Windows
    ]
    for sp in site_packages:
        exists = os.path.exists(sp)
        print(f"  {sp}: {exists}")
        if exists:
            print(f"    Tabulate: {os.path.exists(os.path.join(sp, 'tabulate'))}")

print("\n=== Import Test ===")
try:
    import tabulate
    print("✅ Tabulate imported successfully")
    print(f"   Location: {tabulate.__file__}")
except ImportError as e:
    print(f"❌ Tabulate import failed: {e}")

try:
    import pytest
    print("✅ Pytest imported successfully")
except ImportError as e:
    print(f"❌ Pytest import failed: {e}")
