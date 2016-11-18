# eos-google-chrome-app

## Description

This package is used by EOS to package Google Chrome as a flatpak, to provide
the "client side" entry point to the sandboxed application, that knows how
to run itself from outside the flatpak sandboxed environment.

## Detailed description

This package provides a launcher script (`eos-google-chrome-app`) that will
be called by the system helper program installed in the OS as part of the
eos-google-chrome-helper package.

Adittionally, the wrapper script keeps and monitors a process running inside the flatpak
sandbox for Chrome while the browser is running, to prevent uninstalling / updating
it while running, relying on flatpak's own locking mechanisms.

## License

eos-google-chrome-app is Copyright (C) 2016 Endless Mobile, Inc. and
is licensed under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of
the License, or (at your option) any later version.

See the COPYING file for the full version of the GNU GPLv2 license
