document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('predictionForm').onsubmit = async function(event) {
        event.preventDefault();
        
        const size = document.getElementById('size').value;
        const bedrooms = document.getElementById('bedrooms').value;
        const bathrooms = document.getElementById('bathrooms').value;
        
        try {
            const response = await fetch('/predict/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    size: size,
                    bedrooms: bedrooms,
                    bathrooms: bathrooms
                })
            });
            
            const result = await response.json();
            if (response.ok) {
                document.getElementById('result').textContent = `Predicted House Price: ${result.predicted_price}`;
            } else {
                document.getElementById('result').textContent = `Error: ${result.error}`;
            }
        } catch (error) {
            document.getElementById('result').textContent = `An unexpected error occurred: ${error.message}`;
        }
    };
});
