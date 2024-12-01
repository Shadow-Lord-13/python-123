import sys
import os

#sys.argv[1] to get the value from the command line
username = sys.argv[1]

#Password is fetched from the env varible "pwd"
password = os.getenv("pwd")
print(f"Username: {username} || Password: {password}")