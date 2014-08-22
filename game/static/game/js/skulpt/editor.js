var ocargo = ocargo || {};

$(document).ready(function () {
    ocargo.consoleOutput = $('#consoleOutput');
    var outf = function (outputText) {
        ocargo.animation.appendAnimation({
            type: 'console',
            text: outputText
        });
    };
    
    ocargo.editor = CodeMirror.fromTextArea(document.getElementById('code'), {
        parserfile: ["parsepython.js"],
        autofocus: true,
        theme: "solarized dark",
        //path: "static/env/codemirror/js/",
        lineNumbers: true,
        textWrapping: false,
        indentUnit: 4,
        height: "160px",
        fontSize: "9pt",
        autoMatchParens: true,
        parserConfig: {'pythonVersion': 2, 'strictErrors': true}
    });

   ocargo.editor.run = function() {
        ocargo.model.reset(0);
        Sk.failed = false;
        Sk.configure({output: outf, read: builtinRead});
        //Sk.canvas = "mycanvas";
        Sk.pre = "consoleOutput";
        try {
            Sk.importMainWithBody("<stdin>", false, ocargo.editor.getValue());
            if (!Sk.failed) {
                ocargo.model.programExecutionEnded();
            }
        } catch(e) {
            outf(e.toString() + "\n")
        }
    };

    ocargo.editor.prepare = function() {
        return {success: true, program:{ run: function() { ocargo.editor.run() }}};
    };

    ocargo.editor.reset = function() {
        document.getElementById("code").value = "import van\nv = van.Van()";
        $('#consoleOutput').text('');
    }

    function builtinRead(x) {
        if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
        return Sk.builtinFiles["files"][x];
    }

    // Limit the code so that it stops after 2 seconds
    Sk.execLimit = 2000;

    ocargo.editor.focus();
});
