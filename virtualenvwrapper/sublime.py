#!/usr/bin/env python
import os
import json
import logging

log = logging.getLogger(__name__)
def post_mkproject(args):
	"""
	It reads current path and the project path, generating a Sublime project 
	file in JSON format
	"""
	#original shell script:
	# PROJECT_NAME=`basename $PWD`
	# sed s#PROJECT_PATH#"$PWD"# $WORKON_HOME/sublime.template > 
	# $PWD/$PROJECT_NAME.sublime-project

	# current_path = os.getcwd()
	project_name = os.path.basename(os.getenv('VIRTUAL_ENV'))
	project_path = os.getenv('PROJECT_HOME')
	filename = "{project_name}.sublime-project".format(project_name=project_name)
	filepath = os.path.join(project_path, project_name, filename)

	template = {
		"folders": [
			{"path": os.path.join(project_path, project_name) }
		]
	}

	target = open (filepath, 'a')
	target.write(json.dumps(template))
	target.close()

	return
