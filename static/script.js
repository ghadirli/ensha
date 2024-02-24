document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('logout-link').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default action (navigation)

        // Create a new XMLHttpRequest object
        var xhr = new XMLHttpRequest();

        // Configure the request
        xhr.open('POST', '/accounts/logout/', true); // Specify the method and URL

        // Retrieve CSRF token from the hidden input field
        var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

        // Set the CSRF token header
        xhr.setRequestHeader('X-CSRFToken', csrfToken);

        // Define the callback function for when the request completes
        xhr.onload = function() {
            if (xhr.status === 200) {
                // Successful request
                window.location.href = '/'; // Redirect to homepage or any other page
            } else {
                // Handle error
                console.error('Logout request failed with status:', xhr.status);
            }
        };

        // Send the request
        xhr.send();
    });
});
