from jira import JIRA
import requests


j_user = "admin"
j_pwd = "password"
j_port = "8888"
j_server = "http://192.168.15.38"

# connection with JIRA server
connect = JIRA(j_server + ":" + j_port, auth=(j_user, j_pwd))


# to get list of Uers
def list_users():
    response = requests.get(j_server + ":" + j_port+"/rest/api/2/user/search?username=.",
                            auth=(j_user, j_pwd))
    print(response.json())


# to get details about particular project ; input is project id or Key
def project_details(project_id):
    project = connect.project(project_id)
    print(project.raw)


# to get details about particular issue ; input is issue key or ID
def issue_details(issue_id):
    issue = connect.issue(issue_id)
    print(issue.raw)


# Renaming a user
def rename_user(old_name, new_name):
    result = connect.rename_user(old_name, new_name)
    print(result)
