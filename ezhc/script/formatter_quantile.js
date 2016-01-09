function() {

    var fmt_val = d3.format(',.2f');
    var fmt_qtile = d3.format('.1%');

    var percentile = function(v, arr){
        var c = 0;
        for (var i=0; i<arr.length; i++) {
            if (arr[i]<v) { c += 1; }
        }
        return c/arr.length;
    };

    var get_percentile = function(point){
        var v = point.y;
        var arr = point.series.points.map(function(d){ return d.y; });
        return percentile(v, arr);
    }

    var s = Highcharts.dateFormat('%A, %b %e, %Y', this.x) + '<br/>';

    for (point of this.points) {   
        window.ppoint = point;     
        s += `<span style="color:${point.series.color}">${point.series.name}</span>: <b>${fmt_val(point.y)}</b> (percentile: ${fmt_qtile(get_percentile(point))})<br/>`; 
    }

    return s;

}

