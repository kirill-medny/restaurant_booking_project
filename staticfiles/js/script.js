document.addEventListener('DOMContentLoaded', function() {
  // Example:  Disable past dates in the booking form
  const dateInput = document.querySelector('input[type="date"]');
  if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.setAttribute('min', today);
  }
});