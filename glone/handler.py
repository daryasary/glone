import requests
import subprocess
import shlex

from glone.config import user_data_url, group_projects_url, user_projects_url


def clone(path, name):
    command = shlex.split('git clone {} projects/{}'.format(path, name))
    subprocess.Popen(command)


def clone_project_group(projects):
    for project in projects:
        try:
            clone(project['ssh_url_to_repo'], project['name'])
        except Exception as e:
            print("Error on %s: %s" % (project['ssh_url_to_repo'], e.strerror))


def convert_user_name(username):
    try:
        response = requests.get(user_data_url.format(username))
    except Exception as e:
        print(str(e))
        return None
    response = response.json()
    return response[0].get('id', None) if len(response) else None


def fetch_group_projects(group_id, token):
    response = requests.get(group_projects_url.format(group_id, token))
    if not response.ok:
        return "Unsuccessful request, try again."

    group = response.json()
    clone_project_group(group['projects'])


def fetch_user_projects(username, token):
    user_id = convert_user_name(username)

    response = requests.get(user_projects_url.format(user_id, token))

    if not response.ok:
        return "Unsuccessful request, try again."

    projects = response.json()
    clone_project_group(projects)

