#!/bin/bash
set -e

#tail -f ./logs/es_config_interface_api.log
sudo journalctl -u grafana_loki_interface_api.service -f