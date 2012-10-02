var page = require('webpage').create(),
    address, output, size, viewport_width, viewport_height, timeout, element;

if (phantom.args.length < 2 || phantom.args.length > 7) {
    console.log('Usage: capture.js URL filename viewport_width viewport_height timeout element');
    phantom.exit();
} else {
    
    address = phantom.args[0];
    output = phantom.args[1];
    viewport_width = phantom.args[2];
    viewport_height = phantom.args[3];
    timeout = phantom.args[4];
    element = phantom.args[5] || "";
    
    console.log("address: ", address);
    console.log("output: ", output);
    console.log("viewport_width: ", viewport_width);
    console.log("viewport_height: ", viewport_height);
    console.log("timeout: ", timeout);
    console.log("element: ", element);
    
    page.viewportSize = { width: viewport_width, height: viewport_height };
    
    page.open(address, function (status) {
        if (status !== 'success') {
            console.log('Unable to load the address!');
            phantom.exit();
        } else {
            console.log("Success...parsing...");
        	page.includeJs("http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js", function() {
        	    console.log("jQuery loaded...");
        		// Once jQuery is loaded, run our modifier
        		page.evaluate(
        		    function(viewport_width, viewport_height, element) {
                        // document.body.bgColor = 'white';
        		        // Overwrite the <body> element with the content of #map                        
        		        console.log("element:");
        		        console.log(element);
                        if(element) {
                            console.log("ELEMENT!");
                            $('body').html($("#"+element));
                            return true;
                        } else {
                            console.log("NO ELEMENT");
                            return true;
                        }
                        // $('body').html($("div#map"));
                        // $("div#map").width("100%");
                        // $("div#map").height($(window).height());
                        // map.zoomTo(8);
        		    }
        		);
        		// Take screenshot and exit
        		window.setTimeout(function () {
            		page.render(output);
            		phantom.exit();                
                }, timeout);
        	});
        }
    });    
}