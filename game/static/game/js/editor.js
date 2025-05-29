$(document).ready(function () {
    let shadowRoot = $("editor-wc")[0].shadowRoot;

    // Set editor height and margin
    $(shadowRoot).find("#root").css("height", "inherit");
    $(shadowRoot).find(".proj-container").css("margin", "0 10px 0 0");

    // Fix project bar height
    $(shadowRoot).find(".project-bar").css("block-size", "auto");

    // Focus on text output tab
    $(shadowRoot).find(".react-tabs__tab-text").click();

    // Remove other tab options
    $(shadowRoot).find(".react-tabs__tab-container").remove();

    // Make editor font size not small
    $(shadowRoot).find(".editor").removeClass("editor--small");
});
