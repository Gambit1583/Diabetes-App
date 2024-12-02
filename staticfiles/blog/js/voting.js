// Function to get the CSRF token from the cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// Post upvote handler
document.querySelectorAll('.upvote').forEach(button => {
    button.addEventListener('click', function() {
        const postId = this.getAttribute('data-post-id');
        fetch(`/blog/post/${postId}/upvote/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken  // Adding CSRF token for security
            },
            body: JSON.stringify({})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            document.getElementById(`upvotes-${postId}`).textContent = data.upvotes;
        })
        .catch(error => {
            console.error('Error:', error);
            alert("An error occurred while upvoting. Please try again.");
        });
    });
});

// Post downvote handler
document.querySelectorAll('.downvote').forEach(button => {
    button.addEventListener('click', function() {
        const postId = this.getAttribute('data-post-id');
        fetch(`/blog/post/${postId}/downvote/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken  // Adding CSRF token for security
            },
            body: JSON.stringify({})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            document.getElementById(`downvotes-${postId}`).textContent = data.downvotes;
        })
        .catch(error => {
            console.error('Error:', error);
            alert("An error occurred while downvoting. Please try again.");
        });
    });
});

// Comment upvote handler
document.querySelectorAll('.upvote-comment').forEach(button => {
    button.addEventListener('click', function() {
        const commentId = this.getAttribute('data-comment-id');
        fetch(`/blog/comment/${commentId}/upvote/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken  // Adding CSRF token for security
            },
            body: JSON.stringify({})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            document.getElementById(`upvotes-${commentId}`).textContent = data.upvotes;
        })
        .catch(error => {
            console.error('Error:', error);
            alert("An error occurred while upvoting the comment. Please try again.");
        });
    });
});

// Comment downvote handler
document.querySelectorAll('.downvote-comment').forEach(button => {
    button.addEventListener('click', function() {
        const commentId = this.getAttribute('data-comment-id');
        fetch(`/blog/comment/${commentId}/downvote/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken  // Adding CSRF token for security
            },
            body: JSON.stringify({})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            document.getElementById(`downvotes-${commentId}`).textContent = data.downvotes;
        })
        .catch(error => {
            console.error('Error:', error);
            alert("An error occurred while downvoting the comment. Please try again.");
        });
    });
});
