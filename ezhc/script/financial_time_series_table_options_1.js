
if (options.xAxis==undefined) {
	options.xAxis = {};
}
if (options.xAxis.event==undefined) {
	options.xAxis.events = {};	
}

options.xAxis.events = {
    setExtremes:      function() { update_table_1('__uuid__'); },
    afterSetExtremes: function() { update_table_1('__uuid__'); }
};

options.plotOptions.series.events = {
    hide: function() { update_table_1('__uuid__'); },
    show: function() { update_table_1('__uuid__'); }
};
