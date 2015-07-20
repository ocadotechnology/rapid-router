var ocargo = ocargo || {};

ocargo.utils = {

    // Function to sort an array of objects by a key value and return the array.
    sortObjects : function(arr,key){

        var sortedArray = arr.sort(function(a, b) {

            if (a[key] < b[key]) {
                return -1;
            }
            if (a[key] > b[key]) {
                return 1;
            }
            return 0;
        });

        return sortedArray;

    },

    /**
     * Track JS error details in Universal Analytics
     */

    trackJavaScriptError : function(e) {
        var ie = window.event || {},
            errMsg = e.message || ie.errorMessage;
        var errSrc = (e.filename || ie.errorUrl) + ': ' + (e.lineno || ie.errorLine);
        ga('send', 'event', 'JavaScript Error', errMsg, errSrc, { 'nonInteraction': 1 });
    },

    getURLParameter : function (name) {
        return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null
    },
    isIOSMode: function () {
        return this.getURLParameter('mode') === 'ios';
    }

};

/**
 * Cross-browser event listener
 * from here: https://gist.github.com/KrisOlszewski/10287367
 */

if (window.addEventListener) {
    window.addEventListener('error', ocargo.utils.trackJavaScriptError, false);
} else if (window.attachEvent) {
    window.attachEvent('onerror', ocargo.utils.trackJavaScriptError);
} else {
    window.onerror = ocargo.utils.trackJavaScriptError;
}