{
	'targets': [{
		'target_name': 'pty',
		"sources": [ "src/pty.cpp" ],
		'default_configuration': 'Release',
		"include_dirs" : [
			"<!(node -e \"require('nan')\")"
		],
		'libraries': [
			'-lutil',
		],

	}]
}
