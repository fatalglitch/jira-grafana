from jira import JIRA
import json
import re
import pprint

options = {
	'server': ''
}

jira = JIRA(options)

#issue = jira.issue('SOC-1234').fields
#print issue.raw
#print json.dumps(issue.raw, indent=4, sort_keys=True)

# pyson = json.loads(jsondict)
# jsondict = issue.raw
#print jsondict['fields']

issues = jira.search_issues('project=SOC and status=Closed and Company="HPL / Bloodsport"', maxResults=5, fields='summary, comment')
pprint.pprint([(issue.key, issue.fields.summary) for issue in issues])
