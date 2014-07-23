var ocargo = ocargo || {};

$(document).ready(function () {
    ocargo.consoleOutput = $('#consoleOutput');
    var outf = function (outputText) {
        ocargo.animation.queueAnimation({
            timestamp: ocargo.model.timestamp,
            type: 'console',
            text: outputText,
        });
    };
    
    // set default code
    document.getElementById("code").value = "import van\nv = van.Van()";

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
        parserConfig: {'pythonVersion': 2, 'strictErrors': true},
    });

   ocargo.editor.run = function() {
        ocargo.model.reset(0);
        Sk.configure({output: outf, read: builtinRead});
        //Sk.canvas = "mycanvas";
        Sk.pre = "consoleOutput";
        try {
            Sk.importMainWithBody("<stdin>", false, ocargo.editor.getValue());
            ocargo.model.programExecutionEnded();
        } catch(e) {
            outf(e.toString() + "\n")
        }
    };

    ocargo.editor.prepare = function() {
        return { run: function() { ocargo.editor.run() }};
    };

    $("#skulpt_run").click(function (e) { $('#play')[0].click(); });


    $('#clearConsole').click(function (e) {
        $('#consoleOutput').text('');
    });

    function builtinRead(x) {
        if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
        return Sk.builtinFiles["files"][x];
    }

    // Limit the code so that it stops after 2 seconds
    Sk.execLimit = 2000;

    ocargo.editor.focus();
});
