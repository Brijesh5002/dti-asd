document.addEventListener('DOMContentLoaded', () => {
    const imageUpload = document.getElementById('imageUpload');
    const detectButton = document.getElementById('detectButton');
    const previewImage = document.getElementById('previewImage');
    const resultText = document.getElementById('resultText');

    imageUpload.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (event) => {
                previewImage.src = event.target.result;
                previewImage.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    });

    detectButton.addEventListener('click', async () => {
        if (!imageUpload.files.length) {
            alert('Please upload an image first');
            return;
        }

        const formData = new FormData();
        formData.append('image', imageUpload.files[0]);

        try {
            const response = await fetch('http://localhost:5000/detect', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();

            if (result.is_asd) {
                resultText.textContent = `ASD Detected (Probability: ${(result.asd_probability * 100).toFixed(2)}%)`;
                resultText.style.color = 'red';
            } else {
                resultText.textContent = `No ASD Detected (Probability: ${(result.asd_probability * 100).toFixed(2)}%)`;
                resultText.style.color = 'green';
            }
        } catch (error) {
            console.error('Error:', error);
            resultText.textContent = 'Detection failed. Please try again.';
            resultText.style.color = 'orange';
        }
    });
});