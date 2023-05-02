const saveBtn = document.getElementById("journal-btn");
const journalForm = document.getElementById("journal-form");
const journalSubmissionDate = document.getElementById("journal-submission-date");

saveBtn.addEventListener("click", () => {
  journalSubmissionDate.value = new Date().toLocaleDateString("sv-SE");
  journalForm.submit();
});

// Fetch all the details element.
const details = document.querySelectorAll("details");

// Add the onclick listeners.
details.forEach((targetDetail) => {
  targetDetail.addEventListener("click", () => {
    // Close all the details that are not targetDetail.
    details.forEach((detail) => {
      if (detail !== targetDetail) {
        detail.removeAttribute("open");
      }
    });
  });
});

const card = document.getElementById("journal-card");
if (!card) document.getElementById("journals-none").style.display = "block";