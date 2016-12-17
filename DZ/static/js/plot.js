$(function () {
    var from = $('#from1')[0];
    var to = $('#to1')[0];
    var func = $('#function1')[0];
    var button = $('#button1');

    var interval;

    button.click(function (event) {
        event.preventDefault();
        from = parseFloat(from.value);
        to = parseFloat(to.value);

        clearInterval(interval);

        interval = setInterval(draw_interval, 100);
    });

    function draw_interval () {
        $.plot(
            $('#result'),
            [
                {
                    label: 'Label',
                    data: [[0, 1], [1, 2]],
                }
            ],
            {
                series: {
                    lines: { show: true },
                    points: { show: true }
                },
                yaxis: {
                    min: from,
                    max: to
                }
		    }
		);
    }
});

$(function() {
		var d1 = [];
		for (var i = 0; i < 14; i += 0.5) {
			d1.push([i, Math.sin(i)]);
		}
		var d2 = [[0, 3], [4, 8], [8, 5], [9, 13]];
		// A null signifies separate line segments
		var d3 = [[0, 12], [7, 12], null, [7, 2.5], [12, 2.5]];
		$.plot("#placeholder", [ d1, d2, d3 ]);
		// Add the Flot version string to the footer
		$("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
	});
