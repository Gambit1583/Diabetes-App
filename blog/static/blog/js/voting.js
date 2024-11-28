
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('.upvote').forEach(button => {
                button.addEventListener('click', function() {
                    const postId = this.getAttribute('data-post-id');
                    fetch(`/blog/post/${postId}/upvote/`)
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById(`upvotes-${postId}`).textContent = data.upvotes;
                            document.getElementById(`downvotes-${postId}`).textContent = data.downvotes;
                        });
                });
            });
        
            document.querySelectorAll('.downvote').forEach(button => {
                button.addEventListener('click', function() {
                    const postId = this.getAttribute('data-post-id');
                    fetch(`/blog/post/${postId}/downvote/`)
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById(`upvotes-${postId}`).textContent = data.upvotes;
                            document.getElementById(`downvotes-${postId}`).textContent = data.downvotes;
                        });
                });
            });
        
            document.querySelectorAll('.upvote-comment').forEach(button => {
                button.addEventListener('click', function() {
                    const commentId = this.getAttribute('data-comment-id');
                    fetch(`/blog/comment/${commentId}/upvote/`)
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById(`upvotes-${commentId}`).textContent = data.upvotes;
                            document.getElementById(`downvotes-${commentId}`).textContent = data.downvotes;
                        });
                });
            });
        
            document.querySelectorAll('.downvote-comment').forEach(button => {
                button.addEventListener('click', function() {
                    const commentId = this.getAttribute('data-comment-id');
                    fetch(`/blog/comment/${commentId}/downvote/`)
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById(`upvotes-${commentId}`).textContent = data.upvotes;
                            document.getElementById(`downvotes-${commentId}`).textContent = data.downvotes;
                        });
                });
            });
        });
   