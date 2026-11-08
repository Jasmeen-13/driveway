(() => {
    const form = document.querySelector("[data-compare-form]");
    if (!form) {
        return;
    }

    const status = form.querySelector("[data-compare-status]");
    const checkboxes = Array.from(
        form.querySelectorAll('input[type="checkbox"][name="car"]')
    );
    const maximum = 3;

    function selectedCount() {
        return checkboxes.filter((checkbox) => checkbox.checked).length;
    }

    function updateStatus(message) {
        const count = selectedCount();
        const summary = `${count} of ${maximum} cars selected.`;

        if (message) {
            status.textContent = `${message} ${summary}`;
        } else {
            status.textContent = summary;
        }
    }

    form.addEventListener("change", (event) => {
        if (!checkboxes.includes(event.target)) {
            return;
        }

        if (event.target.checked && selectedCount() > maximum) {
            event.target.checked = false;
            updateStatus("You can select up to three cars.");
            return;
        }

        updateStatus();
    });

    form.addEventListener("submit", (event) => {
        if (selectedCount() < 2) {
            event.preventDefault();
            updateStatus("Select at least two cars to compare.");
            status.focus();
        }
    });
        updateStatus();
})();
