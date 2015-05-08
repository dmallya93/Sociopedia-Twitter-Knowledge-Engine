var chart = AmCharts.makeChart("chartdiv", {
    "type": "pie",
	"theme": "none",
    "titles": [{
        "text": "Visitors countries",
        "size": 16
    }],
    "dataProvider": [{
        "country": "United States",
        "visits": 7252
    }, {
        "country": "China",
        "visits": 3882
    }, {
        "country": "Japan",
        "visits": 1809
    }, {
        "country": "Germany",
        "visits": 1322
    }, {
        "country": "United Kingdom",
        "visits": 1122
    }, {
        "country": "France",
        "visits": 414
    }, {
        "country": "India",
        "visits": 384
    }, {
        "country": "Spain",
        "visits": 211
    }],
    "valueField": "visits",
    "titleField": "country",
    "startEffect": "elastic",
    "startDuration": 2,
    "labelRadius": 15,
    "innerRadius": "50%",
    "depth3D": 10,
    "balloonText": "[[title]]<br><span style='font-size:14px'><b>[[value]]</b> ([[percents]]%)</span>",
    "angle": 15,
    "exportConfig":{	
      menuItems: [{
      icon: '/lib/3/images/export.png',
      format: 'png'	  
      }]  
	}
});
jQuery('.chart-input').off().on('input change',function() {
	var property	= jQuery(this).data('property');
	var target		= chart;
	var value		= Number(this.value);
	chart.startDuration = 0;

	if ( property == 'innerRadius') {
		value += "%";
	}

	target[property] = value;
	chart.validateNow();
});