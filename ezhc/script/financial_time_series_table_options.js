
if (options.xAxis==undefined) {
	options.xAxis = {};
}
if (options.xAxis.event==undefined) {
	options.xAxis.events = {};	
}

options.xAxis.events = {setExtremes: update_table__uuid__};
options.xAxis.events = {afterSetExtremes: update_table__uuid__};
