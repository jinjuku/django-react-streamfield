django.jQuery(document).on("formset:added", function(event, $row, formsetName) {
  // Remove existing containers.
  $row.find(".c-sf-container").remove();

  // Get current row number.
  var attr = $row[0].id;
  var regex = /^.*\-(\d+)$/;
  var m = attr.match(regex);
  if (m.length) {
    // Find init scripts in row.
    $row.find("script").each(function() {
      var id = m[1];
      var script = $(this).text();
      // Update with correct id.
      var s = script.replace("__prefix__", id);
      // Reinitialize.
      eval(s);
    });
  }
});
