const codeArea=document.getElementById('code-area');
const lineNumbers=document.getElementById('line-numbers');
const outputArea=document.getElementById('output-area');
const runBtn=document.getElementById('run-button');

//Update line numbers based on code area content
function updateLineNumbers(){
    const lines=codeArea.value.split('\n').length;
    lineNumbers.innerHTML = Array.from({length: lines}, (_, i) => i + 1).join('<br>');
}

runBtn.addEventListener("click", () => {
    outputArea.textContent = "Running code...\n\n" + codeArea.value;
});

// Sync line numbers on typing & scroll
codeArea.addEventListener("input", updateLineNumbers);
codeArea.addEventListener("scroll", () => {
    lineNumbers.scrollTop = codeArea.scrollTop;
});

// Initial setup
updateLineNumbers();