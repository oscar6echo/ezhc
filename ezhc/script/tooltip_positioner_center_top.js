function (labelWidth, labelHeight, point) {
    var roundUp100 = function(d) { return 100*Math.floor(d/100); },
        labelWidth = roundUp100(labelWidth),
        chart = window.charts['__uuid__'];

    var tooltipX, tooltipY;
    // test X: point.plotX in center
    var testX = (point.plotX + labelWidth * 0.7 > chart.plotWidth / 2) && (point.plotX - labelWidth * 0.7 < chart.plotWidth / 2);
    // test Y: point.plotY in top
    var testY = point.plotY < labelHeight * 0.7;

    if (testX && testY) {
        // put tooltip at center bottom
        tooltipX = chart.plotLeft + (chart.plotWidth - labelWidth) / 2;
        tooltipY = chart.plotTop + chart.plotHeight - labelHeight;
    } else {
        // put tooltip at center top
        tooltipX = chart.plotLeft + (chart.plotWidth - labelWidth) / 2;
        tooltipY = chart.plotTop;
    }

    return {
        x: tooltipX,
        y: tooltipY
    };
}

