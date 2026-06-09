#!/usr/bin/env python3
import os
import shutil
from datetime import datetime, timedelta

def create_sample_files(directory):
    """Create sample files for demonstration"""
    os.makedirs(directory, exist_ok=True)
    
    files_created = 0
    for i in range(5):
        filename = f"{directory}/file_{i}.txt"
        with open(filename, 'w') as f:
            f.write(f"Sample file {i}\n")
            f.write(f"Created: {datetime.now()}\n")
        files_created += 1
    
    return files_created

def list_files(directory):
    """List all files in directory"""
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return
    
    files = os.listdir(directory)
    print(f"\n=== Files in {directory} ===")
    for file in files:
        file_path = os.path.join(directory, file)
        size = os.path.getsize(file_path)
        print(f"  {file} ({size} bytes)")

def backup_files(source_dir, backup_dir):
    """Backup files to another directory"""
    os.makedirs(backup_dir, exist_ok=True)
    
    if not os.path.exists(source_dir):
        print(f"Source directory not found: {source_dir}")
        return 0
    
    files = os.listdir(source_dir)
    count = 0
    for file in files:
        src = os.path.join(source_dir, file)
        dst = os.path.join(backup_dir, file)
        shutil.copy2(src, dst)
        count += 1
    
    return count

def delete_old_files(directory, days=7):
    """Delete files older than specified days"""
    if not os.path.exists(directory):
        return 0
    
    cutoff_time = datetime.now() - timedelta(days=days)
    count = 0
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        
        if file_time < cutoff_time:
            os.remove(file_path)
            count += 1
    
    return count

if __name__ == "__main__":
    work_dir = "./demo_files"
    backup_dir = "./demo_backup"
    
    print("=" * 50)
    print("FILE AUTOMATION DEMO")
    print("=" * 50)
    
    # Create sample files
    print("\n1. Creating sample files...")
    created = create_sample_files(work_dir)
    print(f"   Created: {created} files")
    
    # List files
    list_files(work_dir)
    
    # Backup files
    print("\n2. Backing up files...")
    backed_up = backup_files(work_dir, backup_dir)
    print(f"   Backed up: {backed_up} files")
    list_files(backup_dir)
    
    # Get directory stats
    print("\n3. Directory Statistics:")
    total_size = sum(os.path.getsize(os.path.join(work_dir, f)) for f in os.listdir(work_dir))
    print(f"   Total files: {len(os.listdir(work_dir))}")
    print(f"   Total size: {total_size} bytes")
    
    print("\n" + "=" * 50)
