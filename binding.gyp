{
	'targets': [{
		'target_name': 'pty',
		'default_configuration': 'Release',
		"include_dirs" : [
			"<!(node -e \"require('nan')\")"
		],
		'conditions': [
			['OS=="win"', {
				'include_dirs' : [
					'3rd/winpty/include',
				],
				'dependencies' : [
					'3rd/winpty/winpty.gyp:winpty-agent',
					'3rd/winpty/winpty.gyp:winpty',
				],
				'sources' : [
					'src/pty_win.cpp'
				],
				'libraries': [
					'shlwapi.lib'
				],
			}, {
				'sources': [
					'src/pty_unix.cpp'
				],
				'libraries': [
					'-lutil',
					'-L/usr/lib',
					'-L/usr/local/lib'
				],
			}],
			]
	}]
}
