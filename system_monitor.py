#!/usr/bin/env python3
import psutil
from datetime import datetime

def get_system_info():
    """Get current system information"""
    print("=" * 50)
    print("SYSTEM MONITORING REPORT")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # CPU Usage
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"\nCPU Usage: {cpu_percent}%")
    if cpu_percent > 80:
        print("   WARNING: High CPU usage!")
    
    # Memory Usage
    memory = psutil.virtual_memory()
    print(f"\nMemory Usage: {memory.percent}%")
    print(f"   Used: {memory.used / (1024**3):.2f} GB")
    print(f"   Total: {memory.total / (1024**3):.2f} GB")
    if memory.percent > 80:
        print("   WARNING: High memory usage!")
    
    # Disk Usage
    disk = psutil.disk_usage('/')
    print(f"\nDisk Usage: {disk.percent}%")
    print(f"   Used: {disk.used / (1024**3):.2f} GB")
    print(f"   Total: {disk.total / (1024**3):.2f} GB")
    if disk.percent > 80:
        print("   WARNING: High disk usage!")
    
    # Process Count
    process_count = len(psutil.pids())
    print(f"\nRunning Processes: {process_count}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    get_system_info()
