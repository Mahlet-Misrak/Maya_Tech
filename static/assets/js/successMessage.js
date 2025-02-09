document.getElementById('contactForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(this);

    try {
        const response = await fetch(this.action, {
            method: 'POST',
            body: formData
        });

        const successMessage = document.getElementById('successMessage');
        const errorMessage = document.getElementById('errorMessage');
        const responseMessage = document.getElementById('responseMessage');

        if (response.ok) {
            successMessage.classList.remove('hidden');
            successMessage.classList.add('success');
            errorMessage.classList.add('hidden');
        } else {
            errorMessage.classList.remove('hidden');
            errorMessage.classList.add('error');
            successMessage.classList.add('hidden');
        }

        responseMessage.classList.remove('hidden');
    } catch (error) {
        const errorMessage = document.getElementById('errorMessage');
        const successMessage = document.getElementById('successMessage');
        const responseMessage = document.getElementById('responseMessage');

        errorMessage.classList.remove('hidden');
        errorMessage.classList.add('error');
        successMessage.classList.add('hidden');
        responseMessage.classList.remove('hidden');
    }
});
