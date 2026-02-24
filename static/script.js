function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value;

    if (message.trim() === "") {
        return;
    }

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.reply;
    });

    input.value = "";
}