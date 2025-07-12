#!/bin/bash

#!/bin/bash

# Installer for Snippy for macOS and Linux

set -e # Exit immediately if a command exits with a non-zero status.

INSTALL_DIR="/usr/local/bin"
INSTALL_PATH="$INSTALL_DIR/snippy"
REPO_URL="https://raw.githubusercontent.com/yasakei/Snippy/main/snippy.py"

echo "Installing Snippy..."

# Check for sudo
if [ "$EUID" -ne 0 ]; then
    echo "Please run with sudo or as root."
    exit 1
fi

echo "Downloading snippy script from GitHub..."
# Download the script using curl or wget
if command -v curl &> /dev/null; then
    curl -sSL "$REPO_URL" -o "$INSTALL_PATH"
elif command -v wget &> /dev/null; then
    wget -qO "$INSTALL_PATH" "$REPO_URL"
else
    echo "Error: You need curl or wget to download the script."
    exit 1
fi

echo "Making Snippy executable..."
chmod +x "$INSTALL_PATH"

echo ""
echo "Snippy has been installed successfully to $INSTALL_PATH"
echo "You can now run it from anywhere by typing 'snippy'."
echo "Try it out: snippy list"

exit 0

