#!/bin/bash
# Install Script to setup Meca500 arm
#  Written by
#      David AKA DJSftree
#      Chad A. Woitas AKA satiowadahc
#  Last Updated July 27, 2022


SCRIPT="\033[0;31mI\033[0;32mn\033[0;34ms\033[1;33mt\033[0;31ma\033[0;32nl\033[0;34ml\033[0m"


echo -e "$SCRIPT: Initializing Variables"
PKG_NAME="meca500"
BASE_DIR=$(git rev-parse --show-toplevel)

SRC_DIR="$BASE_DIR/src/"
SHR_DIR="$BASE_DIR/share/"
CFG_DIR="$BASE_DIR/linuxcnc/configs"
DEB_DIR="$BASE_DIR/debian"

ASSET_DIR="/usr/local/share/$PKG_NAME"
CONFG_DIR="/home/$(whoami)/linuxcnc/configs/"
BINRY_DIR="/usr/local/bin"


echo -e "$SCRIPT: Creating Debian Package"
rm -rf "$DEB_DIR/$PKG_NAME"
mkdir -p "$DEB_DIR/$PKG_NAME"
mkdir -p "$DEB_DIR/$PKG_NAME/$ASSET_DIR"
mkdir -p "$DEB_DIR/$PKG_NAME/$CONFG_DIR"
mkdir -p "$DEB_DIR/$PKG_NAME/$BINRY_DIR"
mkdir -p "$DEB_DIR/$PKG_NAME/DEBIAN"
# TODO: Need to auto increment the version number
cp "$BASE_DIR/scripts/control" "$DEB_DIR/$PKG_NAME/DEBIAN/"

echo -e "$SCRIPT: Building Debian Package"
cp -R "$SHR_DIR/" "$DEB_DIR/$PKG_NAME/$ASSET_DIR"
cp -R "$CFG_DIR/" "$DEB_DIR/$PKG_NAME/$CONFG_DIR"
cp "$SRC_DIR/meca500gui.py" "$DEB_DIR/$PKG_NAME/$BINRY_DIR/meca500gui"
sudo chmod +x "$DEB_DIR/$PKG_NAME/$BINRY_DIR/meca500gui"

dpkg-deb --build "$DEB_DIR/$PKG_NAME"
sudo apt install "$DEB_DIR/$PKG_NAME.deb" --reinstall