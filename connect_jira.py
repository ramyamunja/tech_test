from jira import JIRA
from pprint import pprint

j_user = "admin"
j_pwd = "password"
j_port = "8888"
j_server = "http://192.168.15.38"
# connection with JIRA server
connect = JIRA(j_server + ":" + j_port, auth=(j_user, j_pwd))


def project_lists():
    # To list all projects under one particular user
    pprint(connect.projects())
    for each_project in connect.projects():
        project = connect.project(str(each_project))
        pprint(project.raw)
        return project.raw


def project_issues():
    # To list all the issue in particular project and their attributes
    # all_issues = {}
    for each_issue in connect.search_issues("project=YRISC_INSTALLATION"):
        issue = connect.issue(str(each_issue))
        pprint(issue.raw)
        return issue.raw
        # all_issues[str(each_issue)] = {}
        # all_issues[str(each_issue)]["comments"] = [{each_comment.author.displayName: each_comment.body}
        #                                            for each_comment in issue.fields.comment.comments]
        # all_issues[str(each_issue)]["description"] = issue.fields.description
        # all_issues[str(each_issue)]["summary"] = issue.fields.summary
        # all_issues[str(each_issue)]["created"] = issue.fields.created
        # all_issues[str(each_issue)]["reporter"] = issue.fields.reporter.displayName
        # all_issues[str(each_issue)]["assignee"] = issue.fields.assignee.displayName
        # all_issues[str(each_issue)]["votes"] = issue.fields.votes.votes
        # all_issues[str(each_issue)]["progress"] = issue.fields.progress.progress
        # all_issues[str(each_issue)]["status"] = issue.fields.status.name


def create_issues():
    # here to create a issue on particular project
    document_issue = {"project": {"key": "YRINSTALL"},
                      "summary": "testing from python api",
                      "description": "written by ramya, rakesh",
                      "issuetype": {"name": "Bug"}
                      }
    insert_issue = connect.create_issue(document_issue)
    print(insert_issue)


def add_comment(issue_id, comment_message):
    # To add a comment on a particular issue
    comment_info = connect.add_comment(issue_id, comment_message)
    print(comment_info)


def add_vote(issue_id):
    # To add vote to an issue
    vote_info = connect.add_vote(issue_id)
    print(vote_info)


def assign_issue(issue_id, assignee_name):
    # Assign an issue to user, Here it will return TRUE if assigned successfully
    user = connect.assign_issue(issue_id, assignee_name)
    print(user)


def comment_lists(issue_id):
    # Here it will list all comments on particular issue
    list_comments = connect.comments(issue_id)
    print([{each_comment.author.displayName: each_comment.body} for each_comment in list_comments])


# not working
def remove_user(user):
    # Removing a user from project
    user_del = connect.delete_user(user)
    print(user_del)

def issue_details(issueid):
    issue = connect.issue(issueid)
    print(issue.raw)
    
   
print("This is edited by Ramya Munja")
