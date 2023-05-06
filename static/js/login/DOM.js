// Targeting DOM elements
const loginContainer = document.getElementById("auth"); // form container
const loginBtn = document.getElementById("login-btn"); // form submit button
const loginForm = document.getElementById("auth-form"); // form

const email = document.getElementById("email"); // email field
const password = document.getElementById("password"); // password field

// Function to validate Registation fields and update css
const validateField = (field) => {
  const notice = document.getElementById(`${field.id}-notice`); // target the field's error notice
  const isValid = field.checkValidity(); // check field's validity

  // Change field css status based on validity
  if (isValid) {
    field.classList.remove("is-danger");
    field.classList.add("is-success");
    notice.style.display = "none";
  } else {
    field.classList.remove("is-success");
    field.classList.add("is-danger");
    notice.style.display = "block";
  }
};

// Function to validate Registration form + enable/disable submit button
const validateForm = (e) => {
  const isValid = email.checkValidity() && password.checkValidity(); // validates all form fields

   // Change button status based on form validity
  if (isValid) {
    loginBtn.removeAttribute("disabled");
  } else {
    loginBtn.setAttribute("disabled", "");
  }
};

// Event listener that validates the form continuously (on mouseover)
loginContainer.addEventListener("mouseover", validateForm);

// Event listener that validates email on change
email.addEventListener("input", (e) => {
  validateField(email);
});

// Event listener that validates password on change
password.addEventListener("input", (e) => {
  validateField(password);
});

// Event listener that triggers action + css changes once submit btn is clicked
loginBtn.addEventListener("click", (e) => {
  loginBtn.classList.add("is-loading");
  setTimeout(() => {
    loginForm.submit();
  }, 1000);
});
