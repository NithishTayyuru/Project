const API_URL = 'http://localhost:5000';
let userId = 1; // Mock user ID (you can use a real one if needed)

const chatContainer = document.getElementById('chat-container');
const chatMessages = document.getElementById('chat-messages');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const resetButton = document.getElementById('reset-button');

// Show chat directly
chatContainer.classList.remove('hidden');

// Send message to chat
sendButton.addEventListener('click', async () => {
    const message = messageInput.value.trim();
    if (!message) return;

    const messageElement = document.createElement('div');
    messageElement.classList.add('message', 'text-gray-800', 'mb-2');
    messageElement.textContent = `You: ${message}`;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    messageInput.value = ''; // Clear the input field

    // Send the message to the backend
    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: userId, message: message })
        });

        if (response.ok) {
            const data = await response.json();
            const aiMessageElement = document.createElement('div');
            aiMessageElement.classList.add('message', 'text-indigo-600', 'mb-2');
            aiMessageElement.textContent = `AI: ${data.message}`;
            chatMessages.appendChild(aiMessageElement);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        } else {
            alert('Error sending message');
        }
    } catch (err) {
        alert('Error communicating with server');
    }
});

// Reset Chat
resetButton.addEventListener('click', () => {
    chatMessages.innerHTML = ''; // Clear the chat messages
});
