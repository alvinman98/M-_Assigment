{
    'name': 'Custom Job Snippet',
    'description': 'Snippet to display Job',
    'category': 'Website',
    'version': '1.0',
    'depends': ['website', 'hr_recruitment'],
    'data': [
        'views/templates.xml',  # XML template
    ],
    'assets': {  # Frontend assets
        'web.assets_frontend': [
            'as_snippet_job/static/src/js/random_jobs.js',  # Custom JS file
            'as_snippet_job/static/css/random_jobs.css',  # Custom CSS file
        ],
    },
    'installable': True,
    'application': False,
}
