{
    'name': 'Bitcoin Chart Snippet',
    'description': 'Snippet to display Bitcoin Price Chart',
    'category': 'Website',
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/snippet_template.xml',  # XML template
    ],
    'assets': {  # Frontend assets
        'web.assets_frontend': [
            'as_snippet_bitcoin/static/src/js/bitcoin_chart.js',  # Custom JS file
            'as_snippet_bitcoin/static/src/css/bitcoin_chart.css',  # Custom CSS file
            'https://cdn.jsdelivr.net/npm/chart.js',  # Chart.js library
        ],
    },
    'installable': True,
    'application': False,
}
