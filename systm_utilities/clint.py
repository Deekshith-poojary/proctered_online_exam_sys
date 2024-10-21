import requests
import getpass  # Importing getpass to securely input the password
import setp
import subprocess
process = None
# Function to get username and password from user input
def get_credentials():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")  # Securely input the password
    return username, password

# Function to send the credentials to the server for authentication
def authenticate(username, password):
    url = 'http://127.0.0.1:8000/authenticate'  # URL of the local server
    payload = {
        'username': username,
        'password': password
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Login successful!")
            setp.set_proxy(enable=True,proxy_server="127.0.0.1:8080")
            #while (True):
            #    d=requests.get("127.0.0.1:8000/get_end")
            global process
            if process is None or process.poll() is not None:  # Check if the subprocess is not running
                print(1)
                process=subprocess.Popen(['mitmdump','-s','proxy.py'])

#                if not d.status_code==100:
 #                   set_proxy(enable=False,proxy_server="127.0.0.1:8080")
  #                  break
        else:
            print("Login failed: " + response.json().get("message"))
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")

if __name__ == "__main__":
    username, password = get_credentials()
    authenticate(username, password)
