const registerContainer = document.getElementById("register");
const registerBtn = document.getElementById("register-btn");

const firstName = document.getElementById("first-name");
const lastName = document.getElementById("last-name");
const email = document.getElementById("email");
const gender = document.getElementById("gender");
const dateBirth = document.getElementById("date-birth");
const tos = document.getElementById("tos");

const validateField = (field) => {
    const isValid = field.checkValidity();
    if (isValid) {
        field.classList.remove("is-danger");
        field.classList.add("is-success");
    } else {
        field.classList.remove("is-success");
        field.classList.add("is-danger");
    }
}

const validateForm = (e) => {
    const isValid = firstName.checkValidity() &&
        lastName.checkValidity() &&
        email.checkValidity() &&
        gender.checkValidity() &&
        dateBirth.checkValidity() &&
        tos.checkValidity();
    
    if (isValid) {
        registerBtn.removeAttribute("disabled");
    } else {
        registerBtn.setAttribute("disabled", "");
    }
}

registerContainer.addEventListener("mouseover", validateForm)

firstName.addEventListener("change", (e) => {
    validateField(firstName);
});

lastName.addEventListener("change", (e) => {
    validateField(lastName);
});

email.addEventListener("change", (e) => {
    validateField(email);
});

registerBtn.addEventListener("click", (e) => {
    registerBtn.classList.add("is-loading");
})

document.addEventListener('DOMContentLoaded', () => {
  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add('is-active');
  }

  function closeModal($el) {
    $el.classList.remove('is-active');
  }

  function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
      closeModal($modal);
    });
  }

  // Add a click event on buttons to open a specific modal
  (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
    const modal = $trigger.dataset.target;
    const $target = document.getElementById(modal);

    $trigger.addEventListener('click', () => {
      openModal($target);
    });
  });

  // Add a click event on various child elements to close the parent modal
  (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
    const $target = $close.closest('.modal');

    $close.addEventListener('click', () => {
      closeModal($target);
    });
  });

  // Add a keyboard event to close all modals
  document.addEventListener('keydown', (event) => {
    const e = event || window.event;

    if (e.keyCode === 27) { // Escape key
      closeAllModals();
    }
  });
});

