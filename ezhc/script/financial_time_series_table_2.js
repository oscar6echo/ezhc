
var isNumber = function(n) { return !isNaN(parseFloat(n)) && isFinite(n); };

var fmt_nb_pct = function(d) { if (isNumber(d)) { var f = d3.format("+,.1%"); return f(d) }
                               else { return d; }
                             }
var fmt_nb_flo = function(d) { if (isNumber(d)) { var f = d3.format("+,.2f"); return f(d) }
                               else { return d; }
                             }


function get_timeseries__uuid__(n, extremes) {
    
    var opt = opt__uuid__,
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
    window.ttt = ts;
    var arr = ts.data.map(function(d){ return d.v; });
    var s = arr.reduce(function(a, b){ return a+b; });
    return s/arr.length;
}


function get_max_drawdown(ts, nb_bd) {
    var dd = Number.POSITIVE_INFINITY,
        val, ref_val;
    window.ts = ts;

    for (var i=nb_bd; i<ts.data.length; i++) {
        val = ts.data[i].v;
        ref_val = ts.data[i-nb_bd].v;
        dd = Math.min(val-ref_val, dd);
    }
    return dd;
}


function create_table__uuid__(chart) {

    $('#__uuid__ .nb_bdays').val(20)
    $('#__uuid__ .slider').val(20)

    $('#__uuid__ .slider').on('input', function(){
        $('#__uuid__ .nb_bdays').val($(this).val());
        update_table__uuid__();
    });

    $('#__uuid__ .nb_bdays').on('input', function(){
        $('#__uuid__ .slider').val($(this).val());
        update_table__uuid__();
    });

    $('#__uuid__ .container_table').html('<table class="dtable display compact" cellspacing="0" style="width: 75%"></table>' );

    var data = update_table_data_2(chart);
    var dtable = init_table(chart, data);
    
    window.chart__uuid__ = chart;
    window.data = data;
    window.dtable = dtable;
    console.log('create_table');
}


function init_table(chart, data) {
    var dtable = $('#__uuid__ .dtable').DataTable( {
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
    var dtablejq = $('#__uuid__ .dtable').dataTable();
    color_dtable_series_name(chart, dtablejq);

    window.dtable = dtable;
    window.dtablejq = dtablejq;

    console.log('init_table');
    return dtable;
}


function color_dtable_series_name(chart, dtablejq) {
    var color_series = chart.series.map(function(d) { return d.color; });
    $('#__uuid__ td:first-child').each(function(i, d) { $(this).css('color', color_series[i]); })

}


function update_table__uuid__() {
    var data = update_table_data_2(chart__uuid__);
    var dtable = $('#__uuid__ .dtable').DataTable()
    dtable.clear();
    dtable.rows.add(data.arr);
    dtable.draw();
    color_dtable_series_name(chart__uuid__, dtablejq)

    window.data = data;
    console.log('update_table');
}


function update_table_data_2(chart) {
     
    var extremes = chart.xAxis[0].getExtremes(),
        results = [],
        ts, min, max, avf, max_dd;

    window.extremes = extremes;

    for (var k=0; k<chart.series.length-1; k++) {
        var name = chart.series[k].name,
            is_visible = chart.series[k].visible;
        
        if (is_visible) {
            ts = get_timeseries__uuid__(k, extremes);
            min = get_min(ts);
            max = get_max(ts);
            avg = get_avg(ts);
            nb_bdays = $("#__uuid__ .nb_bdays").val();
            max_dd = get_max_drawdown(ts, nb_bdays);
            
            results.push({'name': name,
                          'min': min,
                          'max': max,
                          'avg': avg,
                          'max_dd': max_dd,
                        });
        }

    }

    dtable_arr = results.map(function(d) { return [  d.name,
                                                    fmt_nb_flo(d.min), 
                                                    fmt_nb_flo(d.max),
                                                    fmt_nb_flo(d.avg),
                                                    fmt_nb_flo(d.max_dd)
                                                    ]; });
    dtable_col = ['Series', 'Min', 'Max', 'Avg', 'Max Drawdown'].map(function(d) { return {title: d}; });
    data = {arr: dtable_arr, col: dtable_col};

    $('#__uuid__ .table_date').text(ts.data.length+' business days from '+Highcharts.dateFormat('%d-%b-%y', extremes.min) + ' to ' + Highcharts.dateFormat('%d-%b-%y', extremes.max));
    
    console.log('update_table_data_2');
    return data;

};

