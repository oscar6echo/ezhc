//function() { return { x: 400, y: 1 }; }

function (labelWidth, labelHeight, point) {
    var roundUp100 = function(d) { return 100*Math.floor(d/100); },
        labelWidth = roundUp100(labelWidth),
        chart = window.charts['__uuid__'];

    var tooltipX, tooltipY;
    // test X: point.plotX in left
    var testX = point.plotX < labelWidth * 0.7;
    // test Y: point.plotY in top
    var testY = point.plotY < labelHeight * 0.7;

    if (testX && testY) {
        // put tooltip at left bottom
        tooltipX = chart.plotLeft;
        tooltipY = chart.plotTop + chart.plotHeight - labelHeight;
    } else {
        // put tooltip at left top
        tooltipX = chart.plotLeft;
        tooltipY = chart.plotTop;
    }

    return {
        x: tooltipX,
        y: tooltipY
    };
}
