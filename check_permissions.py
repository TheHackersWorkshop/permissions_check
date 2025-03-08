import os
import pwd
import grp
import stat
from datetime import datetime

def check_permissions():
    # Ask for the directory or file path
    path = input("Enter the directory or file path to check permissions: ")

    # Ensure the script is running with root privileges
    if os.geteuid() != 0:
        print("Error: This script requires root privileges. Please run as root or with sudo.")
        return

    # Check if the path exists
    if not os.path.exists(path):
        print(f"Error: The specified path '{path}' does not exist.")
        return

    # Get file status using os.stat() (owner, group, permissions, etc.)
    try:
        file_stat = os.stat(path)

        # Numeric Permissions (e.g., 755, 644, etc.)
        permissions = oct(file_stat.st_mode)[-3:]

        # Owner and Group (UID and GID)
        owner_uid = file_stat.st_uid
        group_gid = file_stat.st_gid

        # Owner name
        owner_name = pwd.getpwuid(owner_uid).pw_name

        # Group name
        group_name = grp.getgrgid(group_gid).gr_name

        # Check if the file is executable
        is_executable = 'Yes' if os.access(path, os.X_OK) else 'No'

        # Last modified time
        modified_time = datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

        # Display information
        print("\nFile Information:")
        print(f"Path: {path}")
        print(f"Permissions (numeric): {permissions}")
        print(f"Owner (UID): {owner_uid} ({owner_name})")
        print(f"Group (GID): {group_gid} ({group_name})")
        print(f"Executable: {is_executable}")
        print(f"Last Modified: {modified_time}")

        # Optionally, for more detailed output, show symbolic permissions (e.g., rwxr-xr-x)
        symbolic_permissions = stat.filemode(file_stat.st_mode)
        print(f"Permissions (symbolic): {symbolic_permissions}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check_permissions()
