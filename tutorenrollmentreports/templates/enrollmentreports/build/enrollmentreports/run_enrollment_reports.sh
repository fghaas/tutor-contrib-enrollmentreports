#!/bin/bash
echo ">> starting the postfix service"
service postfix start
postconf -e "smtp_address_preference = ipv4"
postconf -e "smtp_sasl_password_maps = static:{{ SMTP_USERNAME }}:{{ SMTP_PASSWORD }}"
postconf -e "relayhost = {{ SMTP_HOST }}:{{ SMTP_PORT }}"
postconf -e "smtpd_use_tls=yes"
postfix reload
ansible-playbook enrollment-report.yml

