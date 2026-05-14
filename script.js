document.getElementById('feedbackForm').addEventListener('submit', function(e) {
    e.preventDefault();
    document.getElementById('feedbackForm').style.display = 'none';
    document.getElementById('successMessage').style.display = 'block';
});