# File Permission Checker

This Python script checks and displays detailed file or directory permissions, ownership, and other metadata. It is useful for system administrators and developers who need to inspect access rights on Linux-based systems.

# Features:
- Displays numeric (e.g., `755`) and symbolic (e.g., `rwxr-xr-x`) permissions  
- Retrieves owner and group information  
- Checks if the file is executable  
- Shows the last modified timestamp  
- Ensures the script runs with root privileges for accurate access checks  

# Usage:
Run the script with superuser privileges and provide the file or directory path when prompted: 

{bash}
sudo python3 check_permissions.py


This script is particularly helpful for security audits and troubleshooting file access issues.
