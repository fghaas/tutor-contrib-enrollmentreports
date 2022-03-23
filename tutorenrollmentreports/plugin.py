from .__about__ import __version__
from glob import glob
import os
import pkg_resources
import click
from tutor import config as tutor_config
from tutor.commands.local import local as local_command_group

templates = pkg_resources.resource_filename(
    "tutorenrollmentreports", "templates"
)

config = {
    "add": {
        "MAIL_TO": [],
    },
    "defaults": {
        "VERSION": __version__,
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}enrollmentreports:{{ ENROLLMENTREPORTS_VERSION }}",  # noqa: E501
        "DB_NAME": "{{ OPENEDX_MYSQL_DATABASE }}",
        "MAIL_FROM": "{{ SMTP_USERNAME }}",
        "K8S_CRONJOB_SCHEDULE": "0 0 1 * *",
    },
}

hooks = {
    "build-image": {
        "enrollmentreports": "{{ ENROLLMENTREPORTS_DOCKER_IMAGE }}",
    },
    "remote-image": {
        "enrollmentreports": "{{ ENROLLMENTREPORTS_DOCKER_IMAGE }}",
    },

}


@local_command_group.command(help="Run the enrollment reports script")
@click.pass_obj
def enrollmentreports(context):
    config = tutor_config.load(context.root)
    job_runner = context.job_runner(config)
    job_runner.run_job(
        service="enrollmentreports",
        command="ansible-playbook enrollment-report.yml"

    )


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "tutorenrollmentreports", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
