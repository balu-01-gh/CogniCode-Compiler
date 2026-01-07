console.log("CogniCode editor loaded");

const codeArea = document.getElementById("codeArea");
const lineNumbers = document.getElementById("lineNumbers");
const outputArea = document.getElementById("outputArea");
const runBtn = document.getElementById("runBtn");

function updateLineNumbers() {
    const lines = codeArea.value.split("\n").length;
    lineNumbers.innerHTML = "";
    for (let i = 1; i <= lines; i++) {
        lineNumbers.innerHTML += i + "<br>";
    }
}

codeArea.addEventListener("input", updateLineNumbers);
codeArea.addEventListener("scroll", () => {
    lineNumbers.scrollTop = codeArea.scrollTop;
});

updateLineNumbers();

runBtn.addEventListener("click", async () => {
    outputArea.textContent = "Running...\n";

    try {
        const response = await fetch("http://127.0.0.1:8000/run", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: codeArea.value })
        });

        const result = await response.json();

        if (result.output !== undefined) {
            outputArea.textContent = result.output || "(no output)";
        } else {
            outputArea.textContent = "Error:\n" + result.error;
        }

    } catch (err) {
        outputArea.textContent = "Connection error:\n" + err;
    }
});
