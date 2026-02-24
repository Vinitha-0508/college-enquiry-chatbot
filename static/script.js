console.log("script.js loaded");

function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    if (!input || !chatBox) {
        console.error("HTML element not found");
        return;
    }

    const message = input.value.trim();
    if (message === "") return;

    // ----------- Create User Message (SAFE METHOD) -----------
    const userDiv = document.createElement("div");
    userDiv.className = "user";
    userDiv.textContent = message;
    chatBox.appendChild(userDiv);

    chatBox.scrollTop = chatBox.scrollHeight;

    // ----------- Send to Backend -----------
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {

        const botDiv = document.createElement("div");
        botDiv.className = "bot";
        botDiv.textContent = data.reply;
        chatBox.appendChild(botDiv);

        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(err => {
        console.error(err);

        const errorDiv = document.createElement("div");
        errorDiv.className = "bot";
        errorDiv.textContent = "Server error. Please try again.";
        chatBox.appendChild(errorDiv);
    });

    input.value = "";
}


// ----------- Press Enter to Send -----------
document.getElementById("user-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});
