(function (view) {

var
    constructors    = ['SVGSVGElement', 'SVGGElement']
    , dummy         = document.createElement('dummy');

if (!constructors[0] in view) {
    return false;
}

if (Object.defineProperty) {

    var innerHTMLPropDesc = {

        get : function () {

            dummy.innerHTML = '';

            Array.prototype.slice.call(this.childNodes)
            .forEach(function (node, index) {
                dummy.appendChild(node.cloneNode(true));
            });

            return dummy.innerHTML;
        },

        set : function (content) {
            var
                self        = this
                , parent    = this
                , allNodes  = Array.prototype.slice.call(self.childNodes)

                , fn        = function (to, node) {
                    if (node.nodeType !== 1) {
                        return false;
                    }

                    var newNode = document.createElementNS('http://www.w3.org/2000/svg', node.nodeName.toLowerCase());

                    Array.prototype.slice.call(node.attributes)
                    .forEach(function (attribute) {
                        newNode.setAttribute(attribute.name, attribute.value);
                    });

                    if (node.nodeName === 'TEXT') {
                        newNode.textContent = node.innerHTML;
                    }

                    to.appendChild(newNode);

                    if (node.childNodes.length) {

                        Array.prototype.slice.call(node.childNodes)
                        .forEach(function (node, index) {
                            fn(newNode, node);
                        });

                    }
                };

            // /> to </tag>
            content = content.replace(/<(\w+)([^<]+?)\/>/, '<$1$2></$1>');

            // Remove existing nodes
            allNodes.forEach(function (node, index) {
                node.parentNode.removeChild(node);
            });


            dummy.innerHTML = content;

            Array.prototype.slice.call(dummy.childNodes)
            .forEach(function (node) {
                fn(self, node);
            });

        }
        , enumerable        : true
        , configurable      : true
    };

    try {
        constructors.forEach(function (constructor, index) {
            Object.defineProperty(window[constructor].prototype, 'innerHTML', innerHTMLPropDesc);
        });
    } catch (ex) {
        // TODO: Do something meaningful here
    }

} else if (Object['prototype'].__defineGetter__) {

    constructors.forEach(function (constructor, index) {
        window[constructor].prototype.__defineSetter__('innerHTML', innerHTMLPropDesc.set);
        window[constructor].prototype.__defineGetter__('innerHTML', innerHTMLPropDesc.get);
    });

}

} (window));