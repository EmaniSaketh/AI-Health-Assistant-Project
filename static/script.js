document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Event listeners for the Quick Reply buttons
document.getElementById('quick-replies').addEventListener('click', function(e) {
    if (e.target.classList.contains('quick-button')) {
        const query = e.target.getAttribute('data-query');
        // Set the input value and immediately send the message
        document.getElementById('user-input').value = query;
        sendMessage();
    }
});


function sendMessage() {
    const userInput = document.getElementById('user-input');
    const userMessage = userInput.value.trim();
    if (userMessage === '') return;

    appendMessage(userMessage, 'user');
    userInput.value = '';
    
    // Hide Quick Replies after the first user message for a cleaner look
    document.getElementById('quick-replies').style.display = 'none';

    // Send message to the Flask server (backend)
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage(data.response, 'assistant');
    })
    .catch(error => {
        console.error('Error:', error);
        appendMessage('Sorry, an error occurred while connecting to the server.', 'assistant');
    });
}

function appendMessage(text, sender) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    
    // Highlight key medical terms for better clarity (e.g., 'burn' becomes <strong>burn</strong>)
    const highlightedText = text.replace(/(burn|cut|choking|fever|sprain|fracture|cpr|emergency)/gi, '<strong>$1</strong>'); 
    
    messageDiv.innerHTML = highlightedText;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}