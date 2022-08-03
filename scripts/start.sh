#!/bin/bash

SCRIPT="\033[0;31mS\033[0;32mt\033[0;34ma\033[1;33mr\033[0;31mt\033[0m"


MACH="meca500"
MACHPATH="meca500/meca500-test.ini"
while getopts "nms" opt; do
  case "${opt}" in
    n)
      NOINSTALL="yes"
      ;;
    m)
      MACHPATH="min-meca500/meca500-min.ini"
      ;;
    s)
      MACHPATH="sim-meca500/sim-meca500.ini"
      ;;
    \?)
      echo "MECA 500 Start"
      echo " Usage:"
      echo " -n Don't reinstall"
      echo " -m Run min meca500"
      echo " -s Run Sim"
      echo ""
      echo " ./start.sh -nm"
      exit 0
      ;;
  esac
done

echo -e "$SCRIPT: Initializing Variables"
PKG_NAME="meca500"
BASE_DIR=$(git rev-parse --show-toplevel)

SRC_DIR="$BASE_DIR/src/"
SHR_DIR="$BASE_DIR/share/"
CFG_DIR="$BASE_DIR/linuxcnc/configs"
DEB_DIR="$BASE_DIR/debian"

if [ $NOINSTALL ]; then
  echo -e $SCRIPT "Skipping install"
else
    cd "$BASE_DIR/scripts" || exit_error "$SCRIPT: Could not cd to $BASE_DIR/src"
  ./install.sh
fi

linuxcnc "$CFG_DIR/$MACHPATH"
