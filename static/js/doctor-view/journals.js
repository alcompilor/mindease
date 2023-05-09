const cardsContainer = document.getElementById("doctor-journals-cards"); // journal cards main container

// Function to create a journal card element
const createCard = (title, content, date) => {
  const cardDiv = document.createElement("div");
  const cardDetails = document.createElement("details");
  const cardSummary = document.createElement("summary");
  const cardPara = document.createElement("p");

  cardDiv.id = "doctor-journal-card";

  cardSummary.innerHTML = `${title} <span id="doctor-journal-date">${date}</span>`;
  cardPara.textContent = content;

  cardDetails.append(cardSummary, cardPara);
  cardDiv.appendChild(cardDetails);

  cardsContainer.appendChild(cardDiv);
};

if (journals.length > 0) {
  // if theres at least one journal
  const reversedJournals = journals.reverse(); // reorder journals

  reversedJournals.forEach((element) => {
    // create card for each journal
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
