FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN python3 -m venv /enrollmentreports/venv/
ENV PATH "/enrollmentreports/venv/bin:$PATH"
RUN mkdir -p /etc/ansible/roles/enrollment_report && \
    mkdir -p /etc/ansible/group_vars
RUN apt-get update && \
    apt install ansible -y && \
    apt-get install rsync -y && \
    apt-get install default-mysql-client -y

RUN git clone https://github.com/hastexo/ansible-role-enrollmentreports.git /etc/ansible/roles/enrollment_report
RUN echo "postfix postfix/main_mailer_type string Internet site" > postfix_install.txt
RUN echo "postfix postfix/mailname string mail.example.com" >> postfix_install.txt
RUN debconf-set-selections postfix_install.txt
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y postfix
COPY enrollment-report.yml .
COPY run_enrollment_reports.sh .
COPY inventory/config.yml /etc/ansible/group_vars/all
RUN  useradd mysql

