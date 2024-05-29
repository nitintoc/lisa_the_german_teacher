document.getElementById('authForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const apiKey = document.getElementById('api_key').value;

    fetch('/authenticate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ api_key: apiKey })
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('message');
        if (data.error) {
            messageDiv.textContent = data.error;
            messageDiv.style.color = 'red';
        } else {
            messageDiv.textContent = data.message;
            messageDiv.style.color = 'green';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
