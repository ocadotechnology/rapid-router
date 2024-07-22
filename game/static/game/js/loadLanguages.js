function loadLanguage(path, langStr, callback) {
  var xobj = new XMLHttpRequest();
  xobj.overrideMimeType("application/javascript");
  xobj.open('GET', path + langStr + '.js', true);
  xobj.onreadystatechange = function () {
    if (xobj.readyState == 4 && xobj.status == "200") {
      eval(xobj.responseText);
      callback();
    } else if (xobj.status == "404") {
      loadLanguage(path, "en", callback);
    }
  };
  xobj.send(null);
}

function reloadWorkspace(workspace) {
  var blocklyDom = Blockly.Xml.workspaceToDom(workspace);
  workspace.clear();
  Blockly.Xml.domToWorkspace(blocklyDom, workspace);
  workspace.updateToolbox(BLOCKLY_XML);
}
