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

    }

};