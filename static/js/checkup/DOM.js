// Update emoji status based on selected slider value

window.addEventListener("DOMContentLoaded", () => {
  const emojiRating = new EmojiRating("#emoji");
});

class EmojiRating {
  constructor(qs) {
    this.input = document.querySelector(qs);

    if (this.input) {
      this.input.addEventListener("input", this.refreshValue.bind(this));
      this.input.value = this.input.min;
    }
  }
  refreshValue(e) {
    this.input.defaultValue = e.target.value;
  }
}
