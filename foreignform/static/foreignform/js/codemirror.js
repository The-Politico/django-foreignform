var cmJQuery = null;

if (typeof jQuery !== 'undefined') {
  cmJQuery = jQuery;
} else if (typeof django !== 'undefined') {
  //use jQuery come with django admin
  cmJQuery = django.jQuery
} else {
  console.error('Cant find jQuery, please make sure your have jQuery imported.');
}

if (!!cmJQuery) {
  cmJQuery(function() {
    cmJQuery.each(cmJQuery('.codemirror-json-editor'), function(i, elem) {
      if (typeof elem.cm !== 'undefined') return;
      try {
        elem.value = JSON.stringify(JSON.parse(elem.value), null, 2);
      } catch(e) {}
      var cm = CodeMirror.fromTextArea(elem, {
        mode: { name: "javascript", json: true },
        lineNumbers: true,
        lineWrapping: true,
        tabMode: "indent",
        tabSize: 2,
        gutters: ["CodeMirror-lint-markers"],
        lint: true,
      });
      elem.cm = cm;
    });
  });
}
