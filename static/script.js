function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatBox = document.getElementById("chat-box");
    
    // Display user message
    chatBox.innerHTML += "<div>User: " + userInput + "</div>";
    
    // Simulate bot response (you can replace this with actual bot logic)
    var botResponse = "Bot: Thanks for your message! How can I assist you?";
    chatBox.innerHTML += "<div>" + botResponse + "</div>";
    
    // Clear user input field
    document.getElementById("user-input").value = "";
    
    // Scroll to bottom of chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}
