var ocargo = ocargo || {};

ocargo.Tab = function(radioElement, labelElement, paneElement) {
    this.getText = function() {
        return labelElement[0].children[1].innerHTML;
    };

    this.setContents = function(newImageURL, newText) {
        labelElement[0].children[0].src = newImageURL;
        labelElement[0].children[1].innerHTML = newText;
    };

    this.getContents = function() {
        return labelElement[0].children[1].innerHTML;
    };

    this.select = function() {
        radioElement.change();
        radioElement.prop('checked', true);
    };

    this.setOnChange = function(onChangeCall) {
        this.setEnabled = function(enabled) {
            if(enabled) {
                radioElement.off('change');
                radioElement.change(onChangeCall);
                radioElement.attr('disabled', false);
            }
            else {
                radioElement.off('change');
                radioElement.attr('disabled', true);
            }
        };

        this.setEnabled(true);
    };

    if(paneElement) {
        this.setPaneEnabled = function(enabled) {
            paneElement.css('display', enabled ? 'block' : 'none');
        };
        this.setPaneEnabled(false);
    }
};