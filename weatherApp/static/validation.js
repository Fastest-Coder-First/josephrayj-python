document.addEventListener("DOMContentLoaded", function () {
  // Get the form element
  const form = document.querySelector(".needs-validation");

  // Add event listener for form submission
  form.addEventListener("submit", function (event) {
    // Check if the form is valid
    if (!form.checkValidity()) {
      event.preventDefault(); // Prevent form submission if invalid
      event.stopPropagation(); // Stop event propagation

      // Add Bootstrap validation classes to form fields
      form.classList.add("was-validated");
    }
  });

  // Add event listeners for form field changes
  const usernameField = form.querySelector("#username");
  const passwordField = form.querySelector("#password");
  const confirmPasswordField = form.querySelector("#confirmPassword");

  // Username validation
  usernameField.addEventListener("input", function () {
    if (usernameField.checkValidity()) {
      usernameField.classList.remove("is-invalid");
      usernameField.classList.add("is-valid");
    } else {
      usernameField.classList.remove("is-valid");
      usernameField.classList.add("is-invalid");
    }
  });

  // Password validation
  passwordField.addEventListener("input", function () {
    if (passwordField.checkValidity()) {
      passwordField.classList.remove("is-invalid");
      passwordField.classList.add("is-valid");
    } else {
      passwordField.classList.remove("is-valid");
      passwordField.classList.add("is-invalid");
    }
  });

  // Confirm password validation
  confirmPasswordField.addEventListener("input", function () {
    if (confirmPasswordField.checkValidity()) {
      confirmPasswordField.classList.remove("is-invalid");
      confirmPasswordField.classList.add("is-valid");
    } else {
      confirmPasswordField.classList.remove("is-valid");
      confirmPasswordField.classList.add("is-invalid");
    }
  });
});
