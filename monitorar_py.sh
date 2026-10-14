#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -ne 2 ]; then
    echo "./monitorar_py.sh <pid> <output.csv>"
    exit 1
fi

# Ajustar as constantes
APP_PID=$1
OUT=$2

echo "timestamp,cpu_pct,mem_pct,rss_kb" > "$OUT"

while kill -0 "$APP_PID" 2>/dev/null; do
    TIMESTAMP=$(date '+%F %T')

    APP_DATA=$(ps -C gunicorn -o %cpu=,%mem=,rss= | xargs | sed 's/\s/,/g')

    if [ -z "$APP_DATA" ]; then
        break
    fi

    echo "$TIMESTAMP,$APP_DATA" | tee -a "$OUT"

    sleep 1
done
