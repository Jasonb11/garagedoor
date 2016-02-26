$(document).ready(function() {

  var updateStatus = function() {
    $.get('/door', function (data) {
      $('#statusField').text(data.open ? 'Open' : 'Closed');
      setTimeout(updateStatus, 5000);
    });
  };

  updateStatus();

  $('#toggleButton').click(function(e) {
    e.preventDefault();

    $.post('/door');
  });
});
