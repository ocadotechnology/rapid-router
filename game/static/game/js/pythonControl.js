var ocargo = ocargo || {};

var DEFAULT_CODE = "import van\n\nv = van.Van()\n";
var appendCodeToPanel = function (code, panel) {
    var oldValue = panel.getValue();
    var newValue = DEFAULT_CODE + code.replace(/<br\s*[\/]?>/gi, '\n');
    if (newValue !== oldValue) {
        panel.setValue(newValue);
    }
};

ocargo.PythonControl = function () {
    /***********/
    /** State **/
    /***********/

    var codePanel;
    var console;

    /********************/
    /** Public methods **/
    /********************/

    this.run = function () {
        ocargo.model.reset(0);
        Sk.failed = false;

        try {
            Sk.importMainWithBody("<stdin>", false, codePanel.getValue());
            if (!Sk.failed) {
                ocargo.model.programExecutionEnded();
            }
        } catch (e) {
            outf(e.toString() + "\n");
        }
    };

    this.prepare = function () {
        return {
            success: true,
            program: {run: this.run},
        };
    };

    this.reset = function () {
        this.clearCodePanel();
        this.clearConsole();
    };

    this.clearCodePanel = function () {
        this.setCode(DEFAULT_CODE);
    };

    this.clearConsole = function () {
        console.text("");
    };

    this.appendToConsole = function (str) {
        console.text(console.text() + str);
    };

    this.setCode = function (code) {
        codePanel.setValue(code.replace(/<br\s*[\/]?>/gi, '\n'));
    };

    this.appendCode = function (code) {
        appendCodeToPanel(code, codePanel);
    };

    this.getCode = function () {
        return codePanel.getValue();
    };

    this.loadPreviousAttempt = function () {
        function decodeHTML(text) {
            var e = document.createElement('div');
            e.innerHTML = text;
            return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
        }

        if (PYTHON_WORKSPACE) {
            this.setCode(PYTHON_WORKSPACE);
        } else {
            this.reset();
        }
    };

    /*********************/
    /** Private methods **/
    /*********************/

    function createCodePanel(id) {
        var cm = CodeMirror.fromTextArea(document.getElementById(id), {
            mode: {
                name: "python",
                version: 2
            },
            autofocus: true,
            theme: "eclipse",
            lineNumbers: true,
            lineWrapping: false,
            indentUnit: 2,
            tabSize: 2,
            height: "160px",
            fontSize: "9pt"
        });

        cm.addKeyMap({
            Tab: function (cm) {
                if (cm.somethingSelected()) {
                    cm.indentSelection("add");
                } else {
                    cm.execCommand("insertSoftTab");
                }
            },
            "Shift-Tab": function (cm) {
                cm.indentSelection("subtract");
            }
        });

        return cm;
    }

    function builtinRead(x) {
        if (Sk.builtinFiles === undefined || Sk.builtinFiles.files[x] === undefined) {
            throw "File not found: '" + x + "'";
        }
        return Sk.builtinFiles.files[x];
    }

    function outf(outputText) {
        ocargo.animation.appendAnimation({
            type: 'console',
            text: outputText
        });
    }
    
    /*************************/
    /** Initialisation code **/
    /*************************/
    codePanel = createCodePanel('code');
    console = $('#consoleOutput');

    var codeView = createCodePanel('pythonView');
    codeView.setValue(DEFAULT_CODE);
    codeView.setOption("readOnly", "nocursor");
    function redrawPythonView(){
    	appendCodeToPanel(ocargo.blocklyCompiler.workspaceToPython(), codeView);
    	setTimeout(redrawPythonView, 100);
    }
    $(redrawPythonView);

    // Limit the code so that it stops after 2 seconds
    Sk.execLimit = 2000;

    // Configure Skulpt
    Sk.configure({output: outf, read: builtinRead});
    //Sk.canvas = "mycanvas";
    Sk.pre = "consoleOutput";

    this.reset();
};
