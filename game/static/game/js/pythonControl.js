/*
Code for Life

Copyright (C) 2015, Ocado Innovation Limited

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

ADDITIONAL TERMS – Section 7 GNU General Public Licence

This licence does not grant any right, title or interest in any “Ocado” logos,
trade names or the trademark “Ocado” or any other trademarks or domain names
owned by Ocado Innovation Limited or the Ocado group of companies or any other
distinctive brand features of “Ocado” as may be secured from time to time. You
must not distribute any modification of this program using the trademark
“Ocado” or claim any affiliation or association with Ocado or its employees.

You are not authorised to use the name Ocado (or any of its trade names) or
the names of any author or contributor in advertising or for publicity purposes
pertaining to the distribution of this program, without the prior written
authorisation of Ocado.

Any propagation, distribution or conveyance of this program must include this
copyright notice and these terms. You must not misrepresent the origins of this
program; modified versions of the program must be marked as such and not
identified as the original program.
*/
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
            try {
                this.setCode(
                    localStorage.getItem('pythonWorkspace-' + LEVEL_ID));
            } catch (e) {
                this.reset();
            }
        }
    };

    this.teardown = function () {
        if (localStorage && !ANONYMOUS) {
            var text = this.getCode();
            try {
                localStorage.setItem('pythonWorkspace-' + LEVEL_ID, text);

            } catch (e) {
                // No point in even logging, as page is unloading
            }
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
