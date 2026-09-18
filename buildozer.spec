[app]
title = VzlomApp
package.name = vzlomapp
package.domain = org.vzlom
source.file = vzlom5.py
source.main = vzlom5.py
source.include_exts = py
requirements = python3,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
