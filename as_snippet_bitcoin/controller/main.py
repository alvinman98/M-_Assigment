import json, os
import requests
from odoo import http
from odoo.http import Response

class BitcoinController(http.Controller):
    @http.route('/bitcoin_data', type='http', auth="public", methods=['GET'])
    def get_bitcoin_data(self):
        """
        Retrieve Bitcoin price data for the past 7 days from Yahoo Finance.
        If the request fails, use data from a local JSON backup.

        Returns:
            Response: JSON with prices and timestamps in milliseconds.
        """
        
        api_url = "https://query1.finance.yahoo.com/v8/finance/chart/BTC-USD?range=7d&interval=1h"
        def fetch_data(url):
            response = requests.get(url)
            response.raise_for_status()
            return response.json()

        def extract_prices_and_timestamps(data):
            # Extract prices and timestamps from the data
            prices = data['chart']['result'][0]['indicators']['quote'][0]['close']
            timestamps = data['chart']['result'][0]['timestamp']
            return {
                'prices': prices,
                'timestamps': [ts * 1000 for ts in timestamps]  # Convert to milliseconds
            }

        try:
            data = fetch_data(api_url)
            formatted_data = extract_prices_and_timestamps(data)
            return Response(json.dumps(formatted_data), content_type='application/json', status=200)
        
        except requests.exceptions.RequestException:
            from odoo.modules import get_module_resource
            json_file_path = os.path.join(get_module_resource('as_snippet_bitcoin', 'backup_data'), 'BTC-USD.json')
            
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
                formatted_data = extract_prices_and_timestamps(data)
            
            return Response(json.dumps(formatted_data), content_type='application/json', status=200)