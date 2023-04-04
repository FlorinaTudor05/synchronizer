import sys
import os
import shutil
import time

# Function to synchronize two folders
def sync_folders(source, replica):
    # Create replica folder if it doesn't exist
    if not os.path.exists(replica):
        os.makedirs(replica)
    
    # Loop through all files/folders in source
    for item in os.listdir(source):
        s = os.path.join(source, item)
        r = os.path.join(replica, item)
        # If item is a file, copy it to replica
        if os.path.isfile(s):
            shutil.copy2(s, r)
            print(f"Copied {s} to {r}")
        # If item is a folder, recursively sync it
        elif os.path.isdir(s):
            sync_folders(s, r)
    
    # Loop through all items in replica
    for item in os.listdir(replica):
        s = os.path.join(source, item)
        r = os.path.join(replica, item)
        # If item in replica doesn't exist in source, remove it
        if not os.path.exists(s):
            if os.path.isfile(r):
                os.remove(r)
                print(f"Removed {r}")
            elif os.path.isdir(r):
                shutil.rmtree(r)
                print(f"Removed {r}")

# Function to log messages to console and file
def log(msg, log_file):
    print(msg)
    with open(log_file, "a") as f:
        f.write(f"{msg}\n")

# Parse command line arguments
if len(sys.argv) != 4:
    print("Usage: python sync.py [source_folder] [replica_folder] [log_file]")
    sys.exit(1)
source_folder = sys.argv[1]
replica_folder = sys.argv[2]
log_file = sys.argv[3]

# Sync folders and log messages
while True:
    log(f"Syncing folders {source_folder} and {replica_folder}", log_file)
    sync_folders(source_folder, replica_folder)
    log("Sync complete", log_file)
    time.sleep(60) # Sync every minute

