[app]
title = Due Date Calculator
package.name = duedatecalculator
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 1.0
requirements = python3,kivy==2.1.0,kivymd
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
permissions = INTERNET