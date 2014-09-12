var ocargo = ocargo || {};

ocargo.PythonControl = function() {

    /***************/
    /** Constants **/
    /***************/

    var DEFAULT_CODE = "import van\n\nv = van.Van()\n";

    /***********/
    /** State **/
    /***********/

    var codePanel;
    var console;

    /********************/
    /** Public methods **/
    /********************/

    this.run = function() {
        ocargo.model.reset(0);
        Sk.failed = false;
        Sk.configure({output: outf, read: builtinRead});
        //Sk.canvas = "mycanvas";
        Sk.pre = "consoleOutput";
        try {
            Sk.importMainWithBody("<stdin>", false, codePanel.getValue());
            if (!Sk.failed) {
                ocargo.model.programExecutionEnded();
            }
        }
        catch(e) {
            outf(e.toString() + "\n")
        }
    };

    this.prepare = function() {
        return {
            success: true, 
            program:{run: this.run}, 
        };
    };

    this.reset = function() {
        this.clearCodePanel();
        this.clearConsole();
    }

    this.clearCodePanel = function() {
        this.setCode("");
    }

    this.clearConsole = function() {
        $('#consoleOutput').text("");
    }

    this.setCode = function(code) {
        codePanel.setValue(DEFAULT_CODE + code);
    }

    /*********************/
    /** Private methods **/
    /*********************/

    function createCodePanel() {
        return CodeMirror.fromTextArea(document.getElementById('code'), {
            parserfile: ["parsepython.js"],
            autofocus: true,
            theme: "eclipse",
            //path: "static/env/codemirror/js/",
            lineNumbers: true,
            textWrapping: false,
            indentUnit: 4,
            height: "160px",
            fontSize: "9pt",
            autoMatchParens: true,
            parserConfig: {'pythonVersion': 2, 'strictErrors': true}
        });
    }

    function builtinRead(x) {
        if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
        return Sk.builtinFiles["files"][x];
    }

    function outf (outputText) {
        ocargo.animation.appendAnimation({
            type: 'console',
            text: outputText
        });
    };

    /*************************/
    /** Initialisation code **/
    /*************************/

    codePanel = createCodePanel();
    consoleOutput = $('#consoleOutput');

    // Limit the code so that it stops after 2 seconds
    Sk.execLimit = 2000;

    this.reset();
}
