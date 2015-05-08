var chart = AmCharts.makeChart("chartdiv2", {
    "type": "pie",
	"theme": "none",
    "titles": [{
        "text": "Entities Extracted",
        "size": 16
    }],
    "dataProvider": [
{
"keyword": "moto",
"occurences": 49338

},{
"keyword": "motorola",
"occurences": 14426

},{
"keyword": "seo",
"occurences": 12091

},{
"keyword": "retailer",
"occurences": 6335

},{
"keyword": "tweet",
"occurences": 4717

},{
"keyword": "android",
"occurences": 3652

},{
"keyword": "",
"occurences": 3008

},{
"keyword": "technology",
"occurences": 2958

},{
"keyword": "post",
"occurences": 2777

},{
"keyword": "usaheadlines",
"occurences": 2561

},{
"keyword": "#google",
"occurences": 2386

},{
"keyword": "video",
"occurences": 1768

},{
"keyword": "smartwatch",
"occurences": 1706

},{
"keyword": "brand",
"occurences": 1581

},{
"keyword": "twitter",
"occurences": 1574

},{
"keyword": "deals",
"occurences": 1413

},{
"keyword": "tech",
"occurences": 1331

},{
"keyword": "at&t",
"occurences": 1281

},{
"keyword": "newsupdates",
"occurences": 1255

},{
"keyword": "flagship",
"occurences": 1192

},{
"keyword": "motorolamotox",
"occurences": 1182

},{
"keyword": "hands-on",
"occurences": 1152

},{
"keyword": "phone",
"occurences": 1142

},{
"keyword": "maker",
"occurences": 1126

},{
"keyword": "flipkart",
"occurences": 1107

},{
"keyword": "apple",
"occurences": 1075

},{
"keyword": "hint",
"occurences": 982

},{
"keyword": "review",
"occurences": 941

},{
"keyword": "aluminum",
"occurences": 931

},{
"keyword": "successor",
"occurences": 856

},{
"keyword": "phones",
"occurences": 843

},{
"keyword": "verizon",
"occurences": 822

},{
"keyword": "teardown",
"occurences": 764

},{
"keyword": "iphone",
"occurences": 743

},{
"keyword": "specs",
"occurences": 736

},{
"keyword": "cell",
"occurences": 725

},{
"keyword": "hours",
"occurences": 725

},{
"keyword": "contest",
"occurences": 657

},{
"keyword": "engadget",
"occurences": 647

},{
"keyword": "unboxing",
"occurences": 644

},{
"keyword": "hands",
"occurences": 590

},{
"keyword": "lg",
"occurences": 562

},{
"keyword": "nexus",
"occurences": 558

},{
"keyword": "gadgets",
"occurences": 557

},{
"keyword": "release",
"occurences": 541

},{
"keyword": "sleeve",
"occurences": 537

},{
"keyword": "today",
"occurences": 517

},{
"keyword": "battery",
"occurences": 504

},{
"keyword": "selena",
"occurences": 488

},{
"keyword": "motorolamotog",
"occurences": 486

},{
"keyword": "devices",
"occurences": 476

},{
"keyword": "leaks",
"occurences": 467

},{
"keyword": "motorola’s",
"occurences": 463

},{
"keyword": "desire",
"occurences": 445

},{
"keyword": "topshop",
"occurences": 430

},{
"keyword": "toyotainnova_in",
"occurences": 429

},{
"keyword": "youtube",
"occurences": 425

},{
"keyword": "#apple",
"occurences": 423

},{
"keyword": "smarty",
"occurences": 422

},{
"keyword": "pricing",
"occurences": 419

},{
"keyword": "monster",
"occurences": 415

},{
"keyword": "galaxy",
"occurences": 413

},{
"keyword": "photos",
"occurences": 402

},{
"keyword": "motox",
"occurences": 394

},{
"keyword": "ct",
"occurences": 392

},{
"keyword": "#motorola",
"occurences": 381

},{
"keyword": "developer",
"occurences": 380

},{
"keyword": "screen",
"occurences": 378

},{
"keyword": "photo",
"occurences": 365

},{
"keyword": "credit",
"occurences": 359

},{
"keyword": "#triplethefun",
"occurences": 335

},{
"keyword": "google",
"occurences": 334

},{
"keyword": "htc",
"occurences": 324

},{
"keyword": "news",
"occurences": 324

},{
"keyword": "arms-on",
"occurences": 300

},{
"keyword": "soreen",
"occurences": 300

},{
"keyword": "leather",
"occurences": 294

},{
"keyword": "multirom",
"occurences": 292

},{
"keyword": "brentwood",
"occurences": 290

},{
"keyword": "bluetooth",
"occurences": 288

},{
"keyword": "photograph",
"occurences": 287

},{
"keyword": "itunes",
"occurences": 283

},{
"keyword": "generation",
"occurences": 281

},{
"keyword": "next-gen",
"occurences": 279

},{
"keyword": "soni",
"occurences": 275

},{
"keyword": "bradfield",
"occurences": 273

},{
"keyword": "turbo",
"occurences": 272

},{
"keyword": "signature",
"occurences": 270

},{
"keyword": "impressions",
"occurences": 254

},{
"keyword": "motorola_ca",
"occurences": 250

},{
"keyword": "backtoschool",
"occurences": 248

},{
"keyword": "semi",
"occurences": 244

},{
"keyword": "life",
"occurences": 242

},{
"keyword": "stores",
"occurences": 241

},{
"keyword": "daily",
"occurences": 240

},{
"keyword": "ifa",
"occurences": 239

},{
"keyword": "prices",
"occurences": 235

},{
"keyword": "update",
"occurences": 235

},{
"keyword": "images",
"occurences": 233

},{
"keyword": "read",
"occurences": 229

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
