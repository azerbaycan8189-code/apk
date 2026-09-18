[app]

title = VzlomApp
package.name = vzlomapp
package.domain = org.vzlom

source.dir = .
source.main = vzlom5.py
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3==3.11.9,kivy==2.3.1,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
