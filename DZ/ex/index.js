$(function() {
    var button = $('#button1');

    button.click(function (event) {
        event.preventDefault();

        var from = $('#from1')[0];
        var to = $('#to1')[0];
        var func = $('#function1')[0];

        from = parseFloat(from.value);
        to = parseFloat(to.value);

        var d1 = [];

        for (var i = from; i < to; i += 0.05) {

            var x = i;
            var y = eval(func.value);

            d1.push([i, y]);
        }

        $.plot("#placeholder", [d1]);
    });

});
