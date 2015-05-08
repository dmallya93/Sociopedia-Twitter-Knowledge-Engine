var chart = AmCharts.makeChart("chartdiv", {
    "type": "pie",
	"theme": "none",
    "titles": [{
        "text": "Visitors countries",
        "size": 16
    }],
    "dataProvider": [
{
"keyword": "moto",
"occurences": 15737

},{
"keyword": "motorola",
"occurences": 12668

},{
"keyword": "android",
"occurences": 5856

},{
"keyword": "#google",
"occurences": 1986

},{
"keyword": "motorolamoto360",
"occurences": 1817

},{
"keyword": "lggwatchr",
"occurences": 1724

},{
"keyword": "technology",
"occurences": 1552

},{
"keyword": "september",
"occurences": 1350

},{
"keyword": "motox",
"occurences": 1298

},{
"keyword": "dickyfirmanzyah",
"occurences": 1140

},{
"keyword": "tweet",
"occurences": 1065

},{
"keyword": "nothing",
"occurences": 954

},{
"keyword": "deals",
"occurences": 916

},{
"keyword": "recovery",
"occurences": 868

},{
"keyword": "#motorola",
"occurences": 823

},{
"keyword": "cell",
"occurences": 803

},{
"keyword": "oneheart",
"occurences": 762

},{
"keyword": "review",
"occurences": 754

},{
"keyword": "moto360",
"occurences": 682

},{
"keyword": "specs",
"occurences": 669

},{
"keyword": "iphone",
"occurences": 628

},{
"keyword": "alternative",
"occurences": 604

},{
"keyword": "hits",
"occurences": 582

},{
"keyword": "malaysia",
"occurences": 580

},{
"keyword": "update",
"occurences": 580

},{
"keyword": "makeuseof",
"occurences": 541

},{
"keyword": "motorolamotox",
"occurences": 528

},{
"keyword": "gionee",
"occurences": 473

},{
"keyword": "daily",
"occurences": 450

},{
"keyword": "sony",
"occurences": 450

},{
"keyword": "watches",
"occurences": 429

},{
"keyword": "video",
"occurences": 427

},{
"keyword": "lg",
"occurences": 402

},{
"keyword": "ecosystem",
"occurences": 395

},{
"keyword": "droidturbo",
"occurences": 390

},{
"keyword": "giveaway",
"occurences": 374

},{
"keyword": "twitter",
"occurences": 372

},{
"keyword": "kbs",
"occurences": 315

},{
"keyword": "phones",
"occurences": 291

},{
"keyword": "tech",
"occurences": 264

},{
"keyword": "car",
"occurences": 236

},{
"keyword": "motorolamotog",
"occurences": 234

},{
"keyword": "sleeve",
"occurences": 230

},{
"keyword": "weekend",
"occurences": 225

},{
"keyword": "vs",
"occurences": 211

},{
"keyword": "style",
"occurences": 210

},{
"keyword": "vzwbuzz",
"occurences": 208

},{
"keyword": "powerhouse",
"occurences": 205

},{
"keyword": "prizes",
"occurences": 199

},{
"keyword": "hero3+",
"occurences": 182

},{
"keyword": "mobile",
"occurences": 181

},{
"keyword": "thetechdad",
"occurences": 178

},{
"keyword": "phone",
"occurences": 175

},{
"keyword": "lag",
"occurences": 169

},{
"keyword": "lcd",
"occurences": 168

},{
"keyword": "gen",
"occurences": 162

},{
"keyword": "vehicle",
"occurences": 161

},{
"keyword": "smartwatch",
"occurences": 156

},{
"keyword": "ahgiveaway",
"occurences": 128

},{
"keyword": "a",
"occurences": 127

},{
"keyword": "androidheadline",
"occurences": 126

},{
"keyword": "photo",
"occurences": 126

},{
"keyword": "body",
"occurences": 125

},{
"keyword": "pictures",
"occurences": 110

},{
"keyword": "mobiles",
"occurences": 109

},{
"keyword": "youtube",
"occurences": 108

},{
"keyword": "armor",
"occurences": 105

},{
"keyword": "date",
"occurences": 103

},{
"keyword": "shahadballan",
"occurences": 102

},{
"keyword": "apple",
"occurences": 98

},{
"keyword": "apps",
"occurences": 96

},{
"keyword": "monster",
"occurences": 92

},{
"keyword": "punjab",
"occurences": 91

},{
"keyword": "smartphone",
"occurences": 91

},{
"keyword": "today",
"occurences": 90

},{
"keyword": "nexus",
"occurences": 89

},{
"keyword": "yamaha",
"occurences": 89

},{
"keyword": "cellular",
"occurences": 82

},{
"keyword": "years",
"occurences": 82

},{
"keyword": "brand",
"occurences": 77

},{
"keyword": "skin",
"occurences": 77

},{
"keyword": "kimono-sleeve",
"occurences": 76

},{
"keyword": "thanthi",
"occurences": 76

},{
"keyword": "stay",
"occurences": 75

},{
"keyword": "chance",
"occurences": 74

},{
"keyword": "flipkart",
"occurences": 73

},{
"keyword": "motogp",
"occurences": 73

},{
"keyword": "post",
"occurences": 72

},{
"keyword": "via",
"occurences": 70

},{
"keyword": "jacket",
"occurences": 69

},{
"keyword": "tribute",
"occurences": 67

},{
"keyword": "life",
"occurences": 66

},{
"keyword": "records",
"occurences": 66

},{
"keyword": "tbt",
"occurences": 64

},{
"keyword": "khairykj",
"occurences": 63

},{
"keyword": "guys",
"occurences": 62

},{
"keyword": "winter",
"occurences": 62

},{
"keyword": "pair",
"occurences": 60

},{
"keyword": "deal",
"occurences": 59

},{
"keyword": "design",
"occurences": 58

}],
"valueField": "occurences",
    "titleField": "keyword",
    "startEffect": "elastic",
    "startDuration": 2,
    "labelRadius": 15,
    "innerRadius": "50%",
    "depth3D": 10,
    "balloonText": "[[keyword]]<br><span style='font-size:14px'><b>[[occurences]]</b> ([[percents]]%)</span>",
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
