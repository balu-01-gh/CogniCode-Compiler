document.addEventListener("DOMContentLoaded", () => {
    console.log("editor.js loaded");

    // Get DOM elements (MATCH HTML IDs)
    const codeArea = document.getElementById("code-area");
    const lineNumbers = document.getElementById("line-numbers");
    const outputArea = document.getElementById("output-area");
    const runBtn = document.getElementById("runBtn");

    // Safety check
    if (!codeArea || !lineNumbers || !outputArea || !runBtn) {
        console.error("One or more DOM elements not found. Check IDs.");
        return;
    }

    // -------------------------------
    // Line Numbers Logic
    // -------------------------------
    function updateLineNumbers() {
        const lines = codeArea.value.split("\n").length;
        lineNumbers.innerHTML = "";

        for (let i = 1; i <= lines; i++) {
            lineNumbers.innerHTML += i + "<br>";
        }
    }

    // Sync scrolling
    codeArea.addEventListener("scroll", () => {
        lineNumbers.scrollTop = codeArea.scrollTop;
    });

    // Update line numbers on typing
    codeArea.addEventListener("input", updateLineNumbers);

    // Initial line numbers
    updateLineNumbers();

    // -------------------------------
    // RUN BUTTON → BACKEND CALL
    // -------------------------------
    runBtn.addEventListener("click", async () => {
        console.log("Run button clicked");
        outputArea.textContent = "Running...\n";

        const code = codeArea.value;

        try {
            const response = await fetch("http://127.0.0.1:8000/run", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ code })
            });

            const result = await response.json();

            if (result.output !== undefined) {
                outputArea.textContent = result.output || "(no output)";
            } else if (result.error) {
                outputArea.textContent = "Error:\n" + result.error;
            } else {
                outputArea.textContent = "Unknown response from backend";
            }

        } catch (err) {
            outputArea.textContent = "Connection error:\n" + err;
        }
    });
});
