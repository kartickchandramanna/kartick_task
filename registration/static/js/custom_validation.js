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
        'first_name': 'Please provide a first name.',
        'last_name': 'Please provide a last name.',
        'age': 'Please provide a age.',
        'date_of_birth': 'Please provide a date of birth.',
        'phone': 'Please provide a phone number.',
        'email': {
          required: "Please provide an valid email address.",
          customEmail: "Please enter a valid email."
        },
        'street_name': 'Please provide a street name.',
        'pincode': 'Please provide a pincode.',
        'city': 'Please provide a city.',
        'state': 'Please provide a state.',
        'country_code': 'Please provide a country code.',
        'model_name': 'Please select a model name.',
        'manufacturing_date': 'Please provide a manufacturing date.',
        'manufacturer': 'Please select a manufacturer.',
        'color': 'Please select a color.',
      }
    });
  });