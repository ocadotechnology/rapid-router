var ocargo = ocargo || {};

ocargo.Tab = function(radioElement, labelElement, paneElement) {
    var _currentStateId;

    var _states = {};

    this.addState = function(stateId, imageUrl, text) {
        _states[stateId] = {imageUrl: imageUrl, text: text};
        return this;
    };

    this.transitTo = function(stateId) {
        labelElement[0].children[0].src = _states[stateId].imageUrl;
        labelElement[0].children[1].innerHTML = _states[stateId].text;
        _currentStateId = stateId;
    };

    this.isInState = function(stateId) {
        return _currentStateId === stateId;
    };

    this.select = function() {
        radioElement.change();
        radioElement.prop('checked', true);
    };

    this.setOnChange = function(onChangeCallback) {
        this.onChangeCallback = onChangeCallback;
        this.enable();
    };

    this.enable = function() {
        radioElement.off('change');
        radioElement.attr('disabled', false);

        radioElement.change(this.onChangeCallback);
    };

    this.disable = function() {
        radioElement.off('change');
        radioElement.attr('disabled', true);
    };

    if (paneElement) {
        this.setPaneEnabled = function (enabled) {
            paneElement.css('display', enabled ? 'block' : 'none');
        };
        this.setPaneEnabled(false);
    }
};

ocargo.Tab.addToggle = function (tabElementId, isSelected, goBack) {
    $(tabElementId).click(function (event) {
        if (isSelected()) {
            goBack();
            event.preventDefault();
        }
    });
};