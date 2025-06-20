// script.js

// Handle tab switching
function showForm(formId) {
    const forms = document.querySelectorAll('.form');
    const buttons = document.querySelectorAll('.tab-button');

    // Hide all forms and remove active class from all buttons
    forms.forEach(form => form.classList.remove('active-form'));
    buttons.forEach(button => button.classList.remove('active'));

    // Show the selected form and activate the corresponding button
    document.getElementById(formId).classList.add('active-form');
    document.querySelector(`[onclick="showForm('${formId}')"]`).classList.add('active');
}
