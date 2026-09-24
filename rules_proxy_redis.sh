#!/usr/bin/env bash

set -e

ZONE="public"
PROXY_PORT="5000"
REDIS_PORT="6379"

firewall-cmd --permanent \
    --zone="$ZONE" \
    --add-service=ssh

firewall-cmd --permanent \
    --zone="$ZONE" \
    --add-port="$PROXY_PORT"/tcp

firewall-cmd --permanent \
    --zone="$ZONE" \
    --remove-port="$REDIS_PORT"/tcp 2>/dev/null || true

firewall-cmd --reload

firewall-cmd --zone="$ZONE" --list-all
