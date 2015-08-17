

FORMATTER_PERCENT = "function() { return (this.value > 0 ? ' + ' : '') + this.value + '%'; }"
FORMATTER_OTHER = "function() { return (this.value > 0 ? ' + ' : '') + this.value; }"

TOOLTIP_HEADER_FORMAT = '<b>{series.name}</b><br>'

TOOLTIP_POINT_FORMAT_PERCENT = '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>'
TOOLTIP_POINT_FORMAT_OTHER = '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>'


TOOLTIP_POSITIONER = "function() { return { x: 400, y: 1 }; }"


JS_JSON_PARSE = """
options = JSON.stringify(options);

options = JSON.parse(options, function(key, value) {

    if (value && (typeof value==="string")) {

        if (value.substr(0,8) == "function") {
            var startBody = value.indexOf('{') + 1;
            var endBody = value.lastIndexOf('}');
            var startArgs = value.indexOf('(') + 1;
            var endArgs = value.indexOf(')');

            return new Function(value.substring(startArgs, endArgs),
                                value.substring(startBody, endBody));
        }

        if (value.substr(0,9)=="(function") {
            var startBody = value.indexOf('{') + 1;
            var endBody = value.lastIndexOf('}');
            var startArgs = value.indexOf('(', 1) + 1;
            var endArgs = value.indexOf(')');

            var func = new Function(value.substring(startArgs, endArgs),
                                    value.substring(startBody, endBody));
            return func();
        }
    }

    return value;
});
"""
