$(document).ready(function () {
      
    // Custom email validation using regex
    $.validator.addMethod("customEmail", function (value, element) {
      // Define your custom email regex pattern
      var emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      return this.optional(element) || emailPattern.test(value);
    });

    // Form validation
    $('#myForm').validate({
      rules: {
        // Define validation rules for each field
        'first_name': 'required',
        'last_name': 'required',
        'age': 'required',
        'date_of_birth': 'required',
        'phone': 'required',
        'email': {
          required: true,
          customEmail: true
        },
        'street_name': 'required',
        'pincode': 'required',
        'city': 'required',
        'state': 'required',
        'country_code': 'required',
        'model_name': 'required',
        'manufacturing_date': 'required',
        'manufacturer': 'required',
        'color': 'required',
      },
      messages: {
        // Define custom error messages for each field
        'first_name': 'Please provide a valid first name.',
        'last_name': 'Please provide a valid last name.',
        'age': 'Please provide a valid age.',
        'date_of_birth': 'Please provide a valid date of birth.',
        'phone': 'Please provide a valid phone number.',
        'email': {
          required: "Please provide an valid email address.",
          customEmail: "Please enter a valid email address."
        },
        'street_name': 'Please provide a valid street name.',
        'pincode': 'Please provide a valid pincode.',
        'city': 'Please provide a valid city.',
        'state': 'Please provide a valid state.',
        'country_code': 'Please provide a valid country code.',
        'model_name': 'Please provide a valid model name.',
        'manufacturing_date': 'Please provide a valid manufacturing date.',
        'manufacturer': 'Please provide a valid manufacturer.',
        'color': 'Please provide a valid color.',
      }
    });
  });