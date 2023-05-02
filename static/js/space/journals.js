const saveBtn = document.getElementById("journal-btn");
const journalForm = document.getElementById("journal-form");
const journalSubmissionDate = document.getElementById(
  "journal-submission-date"
);

const journalSearchInput = document.getElementById("journal-search-input");
const journalSearchButton = document.getElementById("journal-searchbtn");

const cardsContainer = document.getElementById("myspace-journals-cards");

const reversedJournals = journals.reverse();

saveBtn.addEventListener("click", () => {
  journalSubmissionDate.value = new Date().toLocaleDateString("sv-SE");
  journalForm.submit();
});

const createCard = (title, content, date) => {
  const cardDiv = document.createElement("div");
  const cardDetails = document.createElement("details");
  const cardSummary = document.createElement("summary");
  const cardPara = document.createElement("p");

  cardDiv.id = "journal-card";

  cardSummary.innerHTML = `${title} <span id="journal-date">${date}</span>`;
  cardPara.textContent = content;

  cardDetails.append(cardSummary, cardPara);
  cardDiv.appendChild(cardDetails);

  cardsContainer.appendChild(cardDiv);
};

reversedJournals.forEach((element) => {
  const title = element["journal_content"]["title"];
  const content = element["journal_content"]["content"];
  const date = new Date(element["journal_content"]["date"]).toLocaleDateString(
    "sv-SE"
  );

  createCard(title, content, date);
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
