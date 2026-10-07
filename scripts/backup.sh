#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Su dung: $0 <thu_muc_can_sao_luu>"
    exit 1
fi

SOURCE="$1"

if [ ! -d "$SOURCE" ]; then
    echo "Thu muc khong ton tai!"
    exit 2
fi

SOURCE="$(realpath "$SOURCE")"
PROJECT_DIR="$(dirname "$SOURCE")"
BACKUP_DIR="$HOME/backup"
LOG_FILE="$PROJECT_DIR/logs/backup.log"

mkdir -p "$BACKUP_DIR"

NAME=$(basename "$SOURCE")
TIME=$(date +"%Y%m%d_%H%M%S")
TARGET="$BACKUP_DIR/${NAME}_${TIME}.tar.gz"

tar -czf "$TARGET" "$SOURCE"

if [ $? -eq 0 ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $TARGET" >> "$LOG_FILE"
    echo "Sao luu thanh cong: $TARGET"
    exit 0
else
    echo "Sao luu that bai!"
    exit 3
fi
