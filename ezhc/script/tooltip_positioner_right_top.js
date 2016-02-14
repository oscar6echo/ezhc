//function() { return { x: 400, y: 1 }; }

function (labelWidth, labelHeight, point) {
    var roundUp100 = function(d) { return 100*Math.floor(d/100); },
        labelWidth = roundUp100(labelWidth),
        chart = window.charts['__uuid__'];

    var tooltipX, tooltipY;
    // test X: point.plotX in right
    var testX = point.plotX + labelWidth * 0.7 > chart.plotWidth;
    // test Y: point.plotY in top
    var testY = point.plotY < labelHeight * 0.7;

    if (testX && testY) {
        // put tooltip at right bottom
        tooltipX = chart.plotLeft + chart.plotWidth - labelWidth;
        tooltipY = chart.plotTop + chart.plotHeight - labelHeight;
    } else {
        // put tooltip at right top
        tooltipX = chart.plotLeft + chart.plotWidth - labelWidth;
        tooltipY = chart.plotTop;
    }

    return {
        x: tooltipX,
        y: tooltipY
    };
}
