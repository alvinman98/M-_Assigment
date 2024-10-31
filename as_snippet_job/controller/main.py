from odoo import http
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slug
import random, json

class CustomJobSnippet(http.Controller):
    @http.route('/random_jobs', type='http', auth="public", csrf=False)
    def get_random_jobs(self):
        jobs = request.env['hr.job'].search([], limit=100)  # Fetch all jobs
        if not jobs:
            return []  # Return an empty list if no jobs are found
        random_jobs = random.sample(jobs, min(len(jobs), 4))  # Get 4 random jobs
        data = [{'id': job.id, 'name': job.name, 'description': job.description or "No Description", 'link': f"/jobs/detail/{slug(job)}"} for job in random_jobs]
        formated_data = json.dumps(data)
        return formated_data