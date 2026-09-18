[app]

title = VzlomApp
package.name = vzlomapp
package.domain = org.vzlomapp

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

version = 0.1

# Файл должен находиться рядом с buildozer.spec
source.main = vzlom5.py

# Не указывай точную версию Python — python-for-android сам выберет совместимую
requirements = python3,kivy==2.3.1,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
