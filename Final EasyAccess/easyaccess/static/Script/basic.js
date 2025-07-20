document.querySelectorAll('.dropdown-item').forEach(item => {
    item.addEventListener('click', function(event) {
      const language = this.textContent;
      const confirmRedirect = confirm(`You are about to be redirected to the best ${language} playlist on YouTube. Continue?`);
      if (!confirmRedirect) {
        event.preventDefault(); // Stop the redirect if the user cancels
      }
    });
  });