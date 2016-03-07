$(document).ready(function() {

  var updateStatus = function() {
    $.get('/door', function (data) {
      var statusMessage = (data.open ? 'OPENED' : 'CLOSED')
        + ' for ' + data.elapsed;

      $('.status').text(statusMessage);
      if (data.open) {
        $('#toggleButton').addClass('open btn-danger').removeClass('btn-success');
      } else {
        $('#toggleButton').removeClass('open btn-danger').addClass('btn-success');
      }

      setTimeout(updateStatus, 5000);
    });
  };

  updateStatus();

  $('#toggleButton').click(function(e) {
    e.preventDefault();

    $.post('/door');

    $(this).prop('disabled', true);

    var button = $(this);

    setTimeout(function() {
      button.prop('disabled', false);
    }, 2000);
  });
});
