
const examples = [
    "Send every new website lead to my CRM and Slack.",
    "Create an invoice when a Stripe payment succeeds.",
    "Summarise new emails and add tasks to Notion.",
    "Send booking reminders to clients automatically."
];

let textIndex = 0;
let charIndex = 0;
let isDeleting = false;

const typingText = document.getElementById("typing-text");

function typeEffect() {
    const currentText = examples[textIndex];

    if (isDeleting) {
        typingText.textContent = currentText.substring(0, charIndex--);
    } else {
        typingText.textContent = currentText.substring(0, charIndex++);
    }

    let speed = isDeleting ? 40 : 80;

    if (!isDeleting && charIndex === currentText.length + 1) {
        speed = 1500;
        isDeleting = true;
    }

    if (isDeleting && charIndex === 0) {
        isDeleting = false;
        textIndex = (textIndex + 1) % examples.length;
        speed = 500;
    }

    setTimeout(typeEffect, speed);
}

typeEffect();
