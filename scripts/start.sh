#!/bin/bash

SCRIPT="\033[0;31mS\033[0;32mt\033[0;34ma\033[1;33mr\033[0;31mt\033[0m"

echo -e "$SCRIPT: Initializing Variables"
PKG_NAME="meca500"
BASE_DIR=$(git rev-parse --show-toplevel)

SRC_DIR="$BASE_DIR/src/"
SHR_DIR="$BASE_DIR/share/"
CFG_DIR="$BASE_DIR/linuxcnc/configs"
DEB_DIR="$BASE_DIR/debian"

MACH="sim-meca500"

linuxcnc "$CFG_DIR/$MACH/$MACH.ini"
