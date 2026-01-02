[app]
# (str) App version
version = 0.1
title = Crochet Pattern Viewer
package.name = crochetviewer
package.domain = org.crochet

source.dir = .
source.include_exts = py

requirements = python3,kivy,pypdf

orientation = portrait
fullscreen = 1

android.permissions = READ_EXTERNAL_STORAGE




# ... your other settings ...

# Android specific
android.api = 34
android.minapi = 21
android.ndk = 25.2.9519653
android.sdk = 34

# Accept SDK license
android.accept_sdk_license = True

# Skip update (uses cached SDK)
android.skip_update = False

# Gradle version
android.gradle_dependencies = 

[buildozer]
log_level = 2
warn_on_root = 1


# Add permissions if needed
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE




