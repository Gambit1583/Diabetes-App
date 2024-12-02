function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(`${name}=`)) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function setupVoteHandlers(voteType, targetType) {
    document.querySelectorAll(`.${voteType}-${targetType}`).forEach(button => {
        button.addEventListener('click', function() {
            const id = this.getAttribute(`data-${targetType}-id`);
            fetch(`/${targetType}/${id}/${voteType}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    document.getElementById(`${voteType}s-${id}`).textContent = data[`${voteType}s`];
                    const oppositeType = voteType === 'upvote' ? 'downvote' : 'upvote';
                    document.getElementById(`${oppositeType}s-${id}`).textContent = data[`${oppositeType}s`];
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert(`An error occurred while ${voteType}ing. Please try again.`);
                });
        });
    });
}

// Initialize vote handlers
setupVoteHandlers('upvote', 'post');
setupVoteHandlers('downvote', 'post');
setupVoteHandlers('upvote', 'comment');
setupVoteHandlers('downvote', 'comment');

