$(document).ready(function () {
    let shadowRoot = $("editor-wc")[0].shadowRoot;

    // Set editor height and margin
    $(shadowRoot).find("#root").css("height", "100%");
    $(shadowRoot).find(".proj-container").css("margin", "0 10px 0 0");

    // Fix project bar height
    $(shadowRoot).find(".project-bar").css("block-size", "auto");

    // Focus on text output tab
    $(shadowRoot).find(".react-tabs__tab-text").click();

    // Remove visual output and split view tabs
    $(shadowRoot).find("#react-tabs-4").hide();
    $(shadowRoot).find(".output-view-toggle").hide();

    // Make editor font size not small
    $(shadowRoot).find(".editor").removeClass("editor--small");

    // Ensure window doesn't scroll to bottom of page
    window.scrollTo(0, 0);
});
