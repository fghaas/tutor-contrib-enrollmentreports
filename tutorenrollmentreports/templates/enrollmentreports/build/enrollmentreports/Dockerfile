FROM ubuntu:20.04
RUN mkdir -p /etc/ansible/roles/enrollmentreports /etc/ansible/group_vars
RUN apt-get update && \
    apt install -y ansible git default-mysql-client rsync

RUN git -C /etc/ansible/roles clone https://github.com/hastexo/ansible-role-enrollmentreports.git enrollmentreports
RUN echo "postfix postfix/main_mailer_type string Internet site" > postfix_install.txt
RUN debconf-set-selections postfix_install.txt
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y postfix
COPY enrollment-report.yml .
