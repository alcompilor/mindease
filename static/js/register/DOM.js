import { dateLimit } from "./functions.js";

// Targeting DOM elements
const registerContainer = document.getElementById("auth"); // form container
const registerBtn = document.getElementById("register-btn"); // form submit button
const registerForm = document.getElementById("auth-form"); // form

const firstName = document.getElementById("first-name"); // first name field
const lastName = document.getElementById("last-name"); // last name field
const email = document.getElementById("email"); // email field
const password = document.getElementById("password"); // password field
const passwordConfirm = document.getElementById("password-confirm"); // confirm password field
const gender = document.getElementById("gender"); // gender dropdown
const dateBirth = document.getElementById("date-birth"); // date of birth datepicker
const tos = document.getElementById("tos"); // terms & conditions checkbox

const passwordNote = document.getElementById("password-notice"); // notice under password field

// Function to validate password using regex
const validatePassword = () => {
  // Get current pass entered in field
  const currentPass = password.value;

  // Define all required regex
  const regexUpper = new RegExp("(?=.*?[A-Z])");
  const regexLower = new RegExp("(?=.*?[a-z])");
  const regexDigit = new RegExp("(?=.*?[0-9])");
  const regexSpecial = new RegExp("(?=.*?[#?!@$%^&*-])");
  const regexLength = new RegExp(".{8,}");

  // Validate if currentPass meets regex reqs
  const isValidRegex =
    regexUpper.test(currentPass) &&
    regexLower.test(currentPass) &&
    regexDigit.test(currentPass) &&
    regexSpecial.test(currentPass) &&
    regexLength.test(currentPass);

  // Set custom validity based on regex reqs
  if (!isValidRegex) {
    password.setCustomValidity(
      "Password does not meet complexity requirements"
    );
  } else {
    password.setCustomValidity("");
  }

  // Update password notice to show relevant error
  if (!regexLength.test(currentPass)) {
    passwordNote.textContent = "Password must be at least 8 chars";
  } else if (!regexUpper.test(currentPass) || !regexLower.test(currentPass)) {
    passwordNote.textContent =
      "Must contain a mixture of both uppercase and lowercase letters.";
  } else if (!regexDigit.test(currentPass) || !regexSpecial.test(currentPass)) {
    passwordNote.textContent =
      "Must contain a mixture of both digits and special characters.";
  }
};

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
  const isValid =
    firstName.checkValidity() &&
    lastName.checkValidity() &&
    email.checkValidity() &&
    password.checkValidity() &&
    passwordConfirm.checkValidity() &&
    gender.checkValidity() &&
    dateBirth.checkValidity() &&
    tos.checkValidity(); // validates all form fields

  // Change button status based on form validity
  if (isValid) {
    registerBtn.removeAttribute("disabled");
  } else {
    registerBtn.setAttribute("disabled", "");
  }
};

// Function to match passwords in the Registration form
const matchPassword = () => {
  if (password.value != passwordConfirm.value) {
    passwordConfirm.setCustomValidity("Passwords Don't Match"); // set custom validity
  } else {
    passwordConfirm.setCustomValidity(""); // remove custom validity
  }
};

// Event listener that validates the form continuously (on mouseover)
registerContainer.addEventListener("mouseover", validateForm);

// Event listener that validates first name on change
firstName.addEventListener("input", (e) => {
  validateField(firstName);
});

// Event listener that validates last name on change
lastName.addEventListener("input", (e) => {
  validateField(lastName);
});

// Event listener that validates email on change
email.addEventListener("input", (e) => {
  validateField(email);
});

// Event listener that validates password on change
password.addEventListener("input", (e) => {
  validatePassword();
  validateField(password);
  matchPassword();
  validateField(passwordConfirm);
});

// Event listener that validates password confirmation on change
passwordConfirm.addEventListener("input", (e) => {
  matchPassword();
  validateField(passwordConfirm);
});

// Event listener that triggers action + css changes once submit btn is clicked
registerBtn.addEventListener("click", (e) => {
  registerBtn.classList.add("is-loading");
  setTimeout(() => {
    registerForm.submit();
  }, 1500);
});

// Event listener to init terms & conditions modal
document.addEventListener("DOMContentLoaded", () => {
  // Setting date interval in datepicker
  dateBirth.setAttribute("max", dateLimit("max"));
  dateBirth.setAttribute("min", dateLimit("min"));

  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add("is-active");
  }

  function closeModal($el) {
    $el.classList.remove("is-active");
  }

  function closeAllModals() {
    (document.querySelectorAll(".modal") || []).forEach(($modal) => {
      closeModal($modal);
    });
  }

  // Add a click event on buttons to open a specific modal
  (document.querySelectorAll(".js-modal-trigger") || []).forEach(($trigger) => {
    const modal = $trigger.dataset.target;
    const $target = document.getElementById(modal);

    $trigger.addEventListener("click", () => {
      openModal($target);
    });
  });

  // Add a click event on various child elements to close the parent modal
  (
    document.querySelectorAll(
      ".modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button"
    ) || []
  ).forEach(($close) => {
    const $target = $close.closest(".modal");

    $close.addEventListener("click", () => {
      closeModal($target);
    });
  });

  // Add a keyboard event to close all modals
  document.addEventListener("keydown", (event) => {
    const e = event || window.event;

    if (e.keyCode === 27) {
      // Escape key
      closeAllModals();
    }
  });
});
