// script.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const weatherInfo = document.querySelector('.weather-info');
    const errorMessage = document.querySelector('.text-danger');

    form.addEventListener('submit', function(event) {
        weatherInfo.style.opacity = '0';
        setTimeout(function() {
            weatherInfo.style.opacity = '1';
        }, 500);
    });

    if (errorMessage) {
        form.classList.add('shake');
    }
});
