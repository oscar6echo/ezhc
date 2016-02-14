
var isNumber = function(n) { return !isNaN(parseFloat(n)) && isFinite(n); };

var fmt_nb_pct = function(d) { if (isNumber(d)) { var f = d3.format("+,.1%"); return f(d) }
                               else { return d; }
                             }
var fmt_nb_flo = function(d) { if (isNumber(d)) { var f = d3.format("+,.2f"); return f(d) }
                               else { return d; }
                             }


function get_timeseries(uuid, n, extremes) {
    var opt = window.opts[uuid],
        data = opt.series[n].data,
        name = opt.series[n].name,
        mint = extremes.min,
        maxt = extremes.max,
        ts = { 'name':name, 'data': [] };
        
    for (var i=0; i<data.length; i++) {
        var t = data[i][0];
        if (t>=mint & t<=maxt) {        
            ts.data.push({t: t, v: data[i][1]})
        }
    }
    return ts;
}


function get_min(ts) {
    var arr = ts.data.map(function(d){ return d.v; });
    return Math.min(...arr);
}


function get_max(ts) {
    var arr = ts.data.map(function(d){ return d.v; });
    return Math.max(...arr);
}


function get_avg(ts) {
    var arr = ts.data.map(function(d){ return d.v; });
    var s = arr.reduce(function(a, b){ return a+b; });
    return s/arr.length;
}


function get_max_drawdown(ts, nb_bd) {
    var dd = Number.POSITIVE_INFINITY,
        val, ref_val;

    for (var i=nb_bd; i<ts.data.length; i++) {
        val = ts.data[i].v;
        ref_val = ts.data[i-nb_bd].v;
        dd = Math.min(val-ref_val, dd);
    }
    return dd;
}


function create_table_2(uuid, chart) {
    if (typeof window.charts == "undefined") {
        window.charts = {};
    }
    window.charts[uuid] = chart;

    $('#'+uuid+' .nb_bdays').val(20)
    $('#'+uuid+' .slider').val(20)

    $('#'+uuid+' .slider').on('input', function(){
        $('#'+uuid+' .nb_bdays').val($(this).val());
        update_table_2(uuid);
    });

    $('#'+uuid+' .nb_bdays').on('input', function(){
        $('#'+uuid+' .slider').val($(this).val());
        update_table_2(uuid);
    });

    $('#'+uuid+' .container_table').html('<table class="dtable display compact" cellspacing="0" style="width: 75%"></table>' );

    var data = update_table_data_2(uuid, chart);
    var dtable = init_table_2(uuid, chart, data);
    
    window.data = data;
    window.dtable = dtable;
    console.log('create_table_2 '+uuid);
}


function init_table_2(uuid, chart, data) {
    var dtable = $('#'+uuid+' .dtable').DataTable( {
        data: data.arr,
        columns: data.col,
        // dom: "CTftip",
        dom: "tB",
        order: [],
        lengthMenu: [[-1], ["All"]],
        columnDefs: [
            { "width": "40%", "targets": 0 },
            { "width": "13%", "targets": [1, 2, 3, 4] }
          ],
    } );
    var dtablejq = $('#'+uuid+' .dtable').dataTable();
    color_dtable_series_name_2(uuid, chart, dtablejq);

    window.dtable = dtable;
    window.dtablejq = dtablejq;

    console.log('init_table_2 '+uuid);
    return dtable;
}


function color_dtable_series_name_2(uuid, chart, dtablejq) {
    var color_series = chart.series.map(function(d) { return d.color; });
    $('#'+uuid+' td:first-child').each(function(i, d) { $(this).css('color', color_series[i]); })
}


function update_table_2(uuid) {
    var chart = window.charts[uuid],
        data = update_table_data_2(uuid, chart),
        dtable = $('#'+uuid+' .dtable').DataTable()
    dtable.clear();
    dtable.rows.add(data.arr);
    dtable.draw();
    color_dtable_series_name_2(uuid, chart, dtablejq)

    window.data = data;
    console.log('update_table_2 '+uuid);
}


function update_table_data_2(uuid, chart) {     
    var extremes = chart.xAxis[0].getExtremes(),
        results = [],
        ts, min, max, avf, max_dd;

    window.extremes = extremes;

    for (var k=0; k<chart.series.length-1; k++) {
        var name = chart.series[k].name,
            is_visible = chart.series[k].visible;
        
        if (is_visible) {
            ts = get_timeseries(uuid, k, extremes);
            min = get_min(ts);
            max = get_max(ts);
            avg = get_avg(ts);
            nb_bdays = $('#'+uuid+' .nb_bdays').val();
            max_dd = get_max_drawdown(ts, nb_bdays);
            
            results.push({'name': name,
                          'min': min,
                          'max': max,
                          'avg': avg,
                          'max_dd': max_dd,
                        });
        }

    }

    dtable_arr = results.map(function(d) { return [ d.name,
                                                    fmt_nb_flo(d.min), 
                                                    fmt_nb_flo(d.max),
                                                    fmt_nb_flo(d.avg),
                                                    fmt_nb_flo(d.max_dd)
                                                    ]; });
    dtable_col = ['Series', 'Min', 'Max', 'Avg', 'Max Drawdown'].map(function(d) { return {title: d}; });
    data = {arr: dtable_arr, col: dtable_col};

    $('#'+uuid+' .table_date').text(ts.data.length+' business days from '+Highcharts.dateFormat('%d-%b-%y', extremes.min) + ' to ' + Highcharts.dateFormat('%d-%b-%y', extremes.max));
    
    console.log('update_table_data_2 '+uuid);
    return data;

};

