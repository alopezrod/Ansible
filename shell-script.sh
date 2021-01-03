#!/bin/sh

find /var/log/audit/ -mtime +20 | xargs  tar -czvPf  /var/log/audit/audit.log$(date +%F).tar.gz

aws s3 cp /var/log/audit/*.tar.gz s3://efx-cloud-fintech-prod-devops-artifacts/audit_logs/$HOSTNAME/

rm /var/log/audit/*.tar.gz -I

find /var/log/audit/ -name "*.log.*" -type f -mtime +20 -exec rm -f {} \;
