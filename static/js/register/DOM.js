// Targeting DOM elements
const registerContainer = document.getElementById("register"); // form container
const registerBtn = document.getElementById("register-btn"); // form submit button

const firstName = document.getElementById("first-name"); // first name field
const lastName = document.getElementById("last-name"); // last name field
const email = document.getElementById("email"); // email field
const password = document.getElementById("password"); // password field
const passwordConfirm = document.getElementById("password-confirm"); // confirm password field
const gender = document.getElementById("gender"); // gender dropdown
const dateBirth = document.getElementById("date-birth"); // date of birth datepicker
const tos = document.getElementById("tos"); // terms & conditions checkbox

// Function to validate Registation fields and update css
const validateField = (field) => {
  const notice = document.getElementById(`${field.id}-notice`); // target the field's error notice
  const isValid = field.checkValidity(); // check field's validity
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
firstName.addEventListener("change", (e) => {
  validateField(firstName);
});

// Event listener that validates last name on change
lastName.addEventListener("change", (e) => {
  validateField(lastName);
});

// Event listener that validates email on change
email.addEventListener("change", (e) => {
  validateField(email);
});

// Event listener that validates password on change
password.addEventListener("change", (e) => {
  matchPassword();
  validateField(password);
  validateField(passwordConfirm);
});

// Event listener that validates password confirmation on change
passwordConfirm.addEventListener("change", (e) => {
  matchPassword();
  validateField(passwordConfirm);
});

// Event listener that triggers action + css changes once submit btn is clicked
registerBtn.addEventListener("click", (e) => {
  registerBtn.classList.add("is-loading");
});

// Event listener to init terms & conditions modal
document.addEventListener("DOMContentLoaded", () => {
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
