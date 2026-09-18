[app]

# (str) Title of your application
title = VzlomApp

# (str) Package name
package.name = vzlomapp

# (str) Package domain (needed for android packaging)
package.domain = org.vzlom

# (str) Source file where the main entry point is located
source.main = vzlom5.py

# (list) Source files to include (let it be empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Обязательно укажи python3 и все библиотеки, которые импортирует твой vzlom5.py (например, requests)
requirements = python3,requests

# (str) Supported orientations
orientation = portrait

# (int) List of permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
