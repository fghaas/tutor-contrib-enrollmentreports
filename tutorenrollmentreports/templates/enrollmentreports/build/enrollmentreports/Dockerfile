FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN python3 -m venv /enrollmentreports/venv/
ENV PATH "/enrollmentreports/venv/bin:$PATH"
RUN mkdir -p /etc/ansible/roles/enrollmentreports /etc/ansible/group_vars
RUN apt-get update && \
    apt install -y ansible rsync default-mysql-client

RUN git -C /etc/ansible/roles clone https://github.com/hastexo/ansible-role-enrollmentreports.git enrollmentreports
RUN echo "postfix postfix/main_mailer_type string Internet site" > postfix_install.txt
RUN debconf-set-selections postfix_install.txt
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y postfix
COPY enrollment-report.yml .
