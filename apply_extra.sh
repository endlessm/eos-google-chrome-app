#!/usr/bin/bash

ar x chrome.deb
rm -f chrome.deb
tar xf data.tar.xz
rm -f control.tar.?z data.tar.?z debian-binary

mv opt/google/chrome/chrome opt/google/chrome/chrome-real
cp /app/scripts/chrome opt/google/chrome/chrome
