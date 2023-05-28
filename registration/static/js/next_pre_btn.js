
    $(document).ready(function () {

      // Step 1 to Step 2
      $('.next').click(function () {
        if ($('#myForm').valid()) {
          $('#step1').hide();
          $('#step2').show();
        }
      });

      // Step 2 to Step 1
      $('.prev').click(function () {
        $('#step2').hide();
        $('#step1').show();
      });
    });
