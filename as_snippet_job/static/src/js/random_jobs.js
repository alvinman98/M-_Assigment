odoo.define('my_custom_snippet.random_jobs', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    publicWidget.registry.RandomJobsSnippet = publicWidget.Widget.extend({
        selector: '.o_random_jobs_snippet',
        start: function () {
            this._super.apply(this, arguments);
            this.fetchRandomJobs();
        },
        fetchRandomJobs: async function () {
            try {
                const response = await fetch('/random_jobs'); // Fetch random jobs from Odoo
                const jobs = await response.json(); // Parse the JSON response

                // Get the container to display jobs
                const jobContainer = document.getElementById('jobContainer');

                // Clear any existing content
                jobContainer.innerHTML = '';
                
                // Check if jobs are found
                if (!jobs || jobs.length === 0) {
                    jobContainer.innerHTML = '<p>No jobs found</p>';
                    return;
                }

                // Display jobs in the console (or update the HTML as needed)
                jobs.forEach(job => {
                    const jobItem = document.createElement('div');
                    jobItem.className = 'job';
                    jobItem.innerHTML = `
                        <h3>${job.name}</h3>
                        <p>${job.description}</p>
                        <a href="${job.link}" class="btn btn-primary">View Job</a>
                    `;
                    jobContainer.appendChild(jobItem);
                });
            } catch (error) {
                console.error('Error fetching Jobs:', error);
            }
        },
    });

    return publicWidget.registry.RandomJobsSnippet;
});