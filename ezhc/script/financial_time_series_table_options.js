
if (options.xAxis==undefined) {
	options.xAxis = {};
}
if (options.xAxis.event==undefined) {
	options.xAxis.events = {};	
}

options.xAxis.events = {
    setExtremes: update_table__uuid__,
    afterSetExtremes: update_table__uuid__
};

options.plotOptions.series.events = {
    hide: update_table__uuid__,
    show: update_table__uuid__
};
