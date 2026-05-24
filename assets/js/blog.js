(function () {
  const input = document.querySelector("#blog-search");
  const list = document.querySelector("#post-list");
  if (!input || !list) return;

  const cards = Array.from(list.querySelectorAll(".blog-card"));
  const sourceFilter = document.querySelector("#source-filter");
  const langFilter = document.querySelector("#lang-filter");
  const searchIndex = new Map();
  const empty = document.createElement("p");
  empty.className = "empty-search-message";
  empty.textContent = "No matching posts found.";
  empty.hidden = true;
  list.after(empty);

  function getCardText(card) {
    const indexed = searchIndex.get(card.dataset.url);
    if (!indexed) return card.textContent.toLowerCase();

    return [
      indexed.title,
      indexed.excerpt,
      indexed.content,
      indexed.date,
      indexed.source,
      indexed.lang,
      ...(indexed.categories || []),
      ...(indexed.tags || []),
    ].join(" ").toLowerCase();
  }

  function applyFilters() {
    const query = input.value.trim().toLowerCase();
    const source = sourceFilter ? sourceFilter.value : "all";
    const lang = langFilter ? langFilter.value : "all";
    let visibleCount = 0;

    for (const card of cards) {
      const haystack = getCardText(card);
      const matchesQuery = !query || haystack.includes(query);
      const matchesSource = source === "all" || card.dataset.source === source;
      const matchesLang = lang === "all" || card.dataset.lang === lang;
      const visible = matchesQuery && matchesSource && matchesLang;
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    }

    empty.hidden = visibleCount !== 0;
  }

  input.addEventListener("input", applyFilters);
  if (sourceFilter) sourceFilter.addEventListener("change", applyFilters);
  if (langFilter) langFilter.addEventListener("change", applyFilters);

  fetch("/search.json")
    .then((response) => {
      if (!response.ok) throw new Error("Search index unavailable");
      return response.json();
    })
    .then((items) => {
      for (const item of items) {
        searchIndex.set(item.url, item);
      }
      applyFilters();
    })
    .catch(() => {
      applyFilters();
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
