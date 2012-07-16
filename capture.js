var page = require('webpage').create(),
    address, output, size, viewport_width, viewport_height, timeout;

if (phantom.args.length < 2 || phantom.args.length > 6) {
    console.log('Usage: capture.js URL filename viewport_width viewport_height timeout');
    phantom.exit();
} else {
    
    address = phantom.args[0];
    output = phantom.args[1];
    viewport_width = phantom.args[2];
    viewport_height = phantom.args[3];
    timeout = phantom.args[4];
    
    page.viewportSize = { width: viewport_width, height: viewport_height };
    
    page.open(address, function (status) {
        if (status !== 'success') {
            console.log('Unable to load the address!');
        } else {
        	page.includeJs("http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js", function() {
        		// Once jQuery is loaded, run our modifier
        		page.evaluate(
        		    function(viewport_width, viewport_height) {
        		        // Overwrite the <body> element with the content of #map
                        
                        $('body').html($("div#map"));
                        $("div#map").width("100%");
                        $("div#map").height($(window).height());
                        map.zoomTo(8);
                        return true;
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