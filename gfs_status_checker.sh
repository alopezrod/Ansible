#!/bin/bash -le

export ANSIBLE_HOST_KEY_CHECKING=False

vault kv get -tls-skip-verify -field=data -format=json gfs-devops-dev/gfs-devops-dev/ansible-creds > ansible_secret.json
python fetch_gfs_instance_list.py
ansible-playbook executeshell.yml -i inventory.txt --extra-vars "@ansible_secret.json" -e env="nonprod"
