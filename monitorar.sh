#!/usr/bin/env bash

# Ajustar as constantes
JAVA_PID="1234"
DB_CONTAINER="postgres-loucos-por-cafe"

OUT="metricas.csv"

echo "timestamp,java_cpu_pct,java_mem_pct,java_rss_kb,db_cpu_pct,db_mem_usage" > "$OUT"

while kill -0 "$JAVA_PID" 2>/dev/null; do
    TIMESTAMP=$(date '+%F %T')

    JAVA_DATA=$(ps -p "$JAVA_PID" -o %cpu=,%mem=,rss= | xargs)

    if [ -z "$JAVA_DATA" ]; then
        break
    fi

    DB_DATA=$(docker stats --no-stream \
        --format '{{.CPUPerc}},{{.MemUsage}}' \
        "$DB_CONTAINER" 2>/dev/null)

    if [ -z "$DB_DATA" ]; then
        DB_DATA="NA,NA"
    fi

    echo "$TIMESTAMP,$JAVA_DATA,$DB_DATA" | tee -a "$OUT"

    sleep 1
done
