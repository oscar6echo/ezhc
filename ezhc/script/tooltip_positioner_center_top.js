function (labelWidth, labelHeight, point) {
    var roundUp100 = function(d) { return 100*Math.floor(d/100); },
        labelWidth = roundUp100(labelWidth);

    var tooltipX, tooltipY;
    // test X: point.plotX in center
    var testX = (point.plotX + labelWidth * 0.7 > chart__uuid__.plotWidth / 2) && (point.plotX - labelWidth * 0.7 < chart__uuid__.plotWidth / 2);
    // test Y: point.plotY in top
    var testY = point.plotY < labelHeight * 0.7;

    if (testX && testY) {
        // put tooltip at center bottom
        tooltipX = chart__uuid__.plotLeft + (chart__uuid__.plotWidth - labelWidth) / 2;
        tooltipY = chart__uuid__.plotTop + chart__uuid__.plotHeight - labelHeight;
    } else {
        // put tooltip at center top
        tooltipX = chart__uuid__.plotLeft + (chart__uuid__.plotWidth - labelWidth) / 2;
        tooltipY = chart__uuid__.plotTop;
    }

    return {
        x: tooltipX,
        y: tooltipY
    };
}
