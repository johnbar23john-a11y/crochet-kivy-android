[app]
title = Crochet Pattern Viewer
package.name = crochetviewer
package.domain = org.crochet

source.dir = .
source.include_exts = py

requirements = python3,kivy,pypdf

orientation = portrait
fullscreen = 1

android.permissions = READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
