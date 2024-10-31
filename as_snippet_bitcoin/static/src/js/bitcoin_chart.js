odoo.define('as_snippet_bitcoin.bitcoin_chart', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    /**
     * BitcoinChart Widget to fetch and display Bitcoin prices in a chart.
     */
    publicWidget.registry.BitcoinChart = publicWidget.Widget.extend({
        selector: '#bitcoin-chart-section',

        /**
         * Initialize the widget and render the Bitcoin chart.
         */
        start: function () {
            this._super.apply(this, arguments);
            this.renderBitcoinChart();
        },

        /**
         * Fetch Bitcoin price data and render it in a line chart.
         *
         * This function makes an asynchronous request to the '/bitcoin_data' endpoint,
         * retrieves the price data, and uses the Chart.js library to display it.
         *
         * @async
         * @returns {Promise<void>}
         */
        renderBitcoinChart: async function () {
            try {
                const response = await fetch('/bitcoin_data');
                const data = await response.json();

                const ctx = document.getElementById('bitcoinChart').getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: data.timestamps.map(ts => new Date(ts).toLocaleString()),
                        datasets: [{
                            label: 'BTC-USD',
                            data: data.prices,
                            borderColor: '#FF9900',
                            backgroundColor: 'rgba(255, 153, 0, 0.2)',
                            borderWidth: 2,
                        }],
                    },
                    options: {
                        scales: {
                            x: { title: { display: true, text: 'Time' } },
                            y: { title: { display: true, text: 'Price (USD)' } },
                        },
                    },
                });
            } catch (error) {
                console.error('Error fetching Bitcoin prices:', error);
            }
        },
    });

    return publicWidget.registry.BitcoinChart;
});