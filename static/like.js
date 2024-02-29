// like.js
document.addEventListener('DOMContentLoaded', function() {
    const likeButton = document.getElementById('like-btn');
    const likeCount = document.getElementById('like-count');

    likeButton.addEventListener('click', function() {
        // Increment like count and update display
        const currentLikes = parseInt(likeCount.textContent);
        const newLikes = currentLikes + 1;
        likeCount.textContent = newLikes;

        // Send asynchronous request to server to update like count
        fetch('articles/update_likes/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is included
            },
            body: JSON.stringify({ article_id: {{ article.id }} })  // Send article ID to server
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to update likes');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            // Roll back like count update on error
            likeCount.textContent = currentLikes;
        });
    });

    // Function to retrieve CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Check if cookie name matches the requested name
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    // Extract and decode cookie value
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
