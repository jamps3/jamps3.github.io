(function () {
  const input = document.querySelector("#blog-search");
  const list = document.querySelector("#post-list");
  if (!input || !list) return;

  const cards = Array.from(list.querySelectorAll(".blog-card"));
  const empty = document.createElement("p");
  empty.className = "empty-search-message";
  empty.textContent = "No matching posts found.";
  empty.hidden = true;
  list.after(empty);

  input.addEventListener("input", () => {
    const query = input.value.trim().toLowerCase();
    let visibleCount = 0;

    for (const card of cards) {
      const haystack = card.textContent.toLowerCase();
      const visible = !query || haystack.includes(query);
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    }

    empty.hidden = visibleCount !== 0;
  });
})();

(function () {
  if (!navigator.clipboard) return;

  document.querySelectorAll("pre > code").forEach((code) => {
    const pre = code.parentElement;
    const button = document.createElement("button");
    button.className = "copy-code-button";
    button.type = "button";
    button.textContent = "Copy";

    button.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(code.innerText);
        button.textContent = "Copied!";
        setTimeout(() => {
          button.textContent = "Copy";
        }, 1200);
      } catch {
        button.textContent = "Failed";
        setTimeout(() => {
          button.textContent = "Copy";
        }, 1200);
      }
    });

    pre.classList.add("has-copy-button");
    pre.appendChild(button);
  });
})();
