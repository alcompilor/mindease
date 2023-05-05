const saveBtn = document.getElementById("journal-btn");
const journalForm = document.getElementById("journal-form");
const journalSubmissionDate = document.getElementById(
  "journal-submission-date"
);

const journalSearchInput = document.getElementById("journal-search-input");
const journalSearchButton = document.getElementById("journal-searchbtn");

const cardsContainer = document.getElementById("myspace-journals-cards");

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

if (journals.length > 0) {
  const reversedJournals = journals.reverse();

  reversedJournals.forEach((element) => {
    const title = element["journal_content"]["title"];
    const content = element["journal_content"]["content"];
    const date = new Date(
      element["journal_content"]["date"]
    ).toLocaleDateString("sv-SE");

    createCard(title, content, date);
  });
}

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

const searchParams = new URLSearchParams(window.location.search);
const isSearch = searchParams.has("q");

const card = document.getElementById("journal-card");

if (!card && !isSearch) {
  document.getElementById("journals-none").textContent =
    "You have no journals. Add a few but keep in mind that journals can't be deleted nor edited 😉";
}

if (!card && isSearch) {
  document.getElementById("journals-none").textContent =
    "There were no journals found 👀";
}

if (isSearch) {
  query = searchParams.get("q");
  if (query != "") {
    journalSearchInput.value = searchParams.get("q");
  } else {
    window.location = window.location.href.split("?")[0];
  }
}
