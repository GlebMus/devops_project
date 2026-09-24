#!/usr/bin/env bash

set -e

PROXY_IP="192.168.56.20"
BACKEND_PORT="8080"
POSTGRES_PORT="5432"

ufw default deny incoming
ufw default allow outgoing

ufw allow 22/tcp

ufw allow from "$PROXY_IP" to any port "$BACKEND_PORT" proto tcp

ufw deny "$BACKEND_PORT"/tcp

ufw deny "$POSTGRES_PORT"/tcp

ufw --force enable

ufw status numbered
