#!/bin/bash
# filepath: zip_current_dir.sh

# Finn katalogen der scriptet ligger
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Gå til parent directory (root folder)
cd "$SCRIPT_DIR/.."

# Lag en zip-fil med samme navn som parent folder
PARENT_DIR_NAME="$(basename "$(pwd)")"
ZIPNAME="${PARENT_DIR_NAME}.zip"
zip -r "$ZIPNAME" . -x "scripts/*" "$ZIPNAME"

echo "Alt i $(pwd) er pakket i $ZIPNAME (scripts folder ekskludert)"