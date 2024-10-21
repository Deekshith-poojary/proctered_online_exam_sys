import winreg

def set_proxy(enable, proxy_server):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",0, winreg.KEY_WRITE)


        if enable:
            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxy_server)
            print("Proxy enabled.")
        else:
            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
            print("Proxy disabled.")

        winreg.CloseKey(key)
    except Exception as e:
        print("Error:", e)
set_proxy(enable=True,proxy_server="127.0.0.1:8080")
