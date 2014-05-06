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

	current_path = os.getcwd()
	project_name = os.path.basename(current_path)
	filepath = os.path.join(current_path,project_name)
	filename = filepath + ".sublime-project"

	template = {
		"folders": [
			{"path": current_path }
		]
	}

	target = open (filename,'a')
	target.write(json.dumps(template))
	target.close()
	
	print "post_mkproject_job_done"
	"""testing beacon"""
	
	return
