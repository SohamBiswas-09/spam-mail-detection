document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('detectionForm');
    const submitBtn = document.querySelector('.detect-btn');
    const resultDiv = document.getElementById('result');
    const emailInput = document.getElementById('emailText');
  
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const emailText = emailInput.value.trim();
      if (!emailText) {
        showResult('Please enter some text to analyze', 'error');
        return;
      }
  
      try {
        setLoadingState(true);
        // Update the fetch URL to match your Docker environment
        const response = await fetch('https://spammaildetector-y89t.onrender.com/predict', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text: emailText })
        });
  
        if (!response.ok) throw new Error('Server error');
  
        const data = await response.json();
        showResult(
          data.prediction === 1 ? '🚩 Spam Detected!' : '✅ Legitimate Email',
          data.prediction === 1 ? 'spam' : 'ham'
        );
      } catch (error) {
        console.error('Detection error:', error);
        showResult('⚠️ Error processing request', 'error');
      } finally {
        setLoadingState(false);
      }
    });
  
    function setLoadingState(isLoading) {
      submitBtn.disabled = isLoading;
      submitBtn.classList.toggle('loading', isLoading);
    }
  
    function showResult(message, type) {
      resultDiv.textContent = message;
      resultDiv.className = 'result';
      
      if (type === 'spam') {
        resultDiv.classList.add('spam');
      } else if (type === 'ham') {
        resultDiv.classList.remove('spam');
      } else {
        resultDiv.style.color = '#ffa502';
      }
      
      resultDiv.style.display = 'block';
    }
  });