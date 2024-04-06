document.addEventListener('DOMContentLoaded', function() {
    const newsletterForm = document.getElementById('newsletterForm');
    const newsletterMessage = document.getElementById('newsletterMessage');

    newsletterForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const fullName = document.getElementById('fullName').value;
        const emailAddress = document.getElementById('emailAddress').value;

        if (fullName.trim() === '' || emailAddress.trim() === '') {
            newsletterMessage.textContent = 'Please fill out all fields.';
        } else {
            newsletterMessage.textContent = `Thank you, ${fullName}! You've successfully subscribed to our newsletter.`;
            newsletterForm.reset();
        }
    });
});