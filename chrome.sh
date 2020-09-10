#!/bin/bash

# Let the wrapped binary know that it has been run through the wrapper.
#
# This env variable will (only) be used by Chrome to determine the
# executable path when creating desktop shortcuts so let's set it to
# our system wrapper as the default is set to the google-chrome wrapper
# absolute path which is specific to the flatpak version.
export CHROME_WRAPPER="/usr/bin/eos-google-chrome"

HERE="`dirname ${BASH_SOURCE[0]}`"

exec "$HERE/chrome-real" "$@"
