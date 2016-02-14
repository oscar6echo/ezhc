
function create_table_0(uuid, chart) {
    if (typeof window.charts == "undefined") {
        window.charts = {};
    }
    window.charts[uuid] = chart;
    console.log('create_table_0 '+uuid);
}
