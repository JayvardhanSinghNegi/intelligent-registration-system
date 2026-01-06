const form = document.getElementById("registrationForm");
const submitBtn = document.getElementById("submitBtn");
const formMessage = document.getElementById("formMessage");

const countrySelect = document.getElementById("country");
const stateSelect = document.getElementById("state");
const citySelect = document.getElementById("city");

const passwordInput = document.getElementById("password");
const confirmPasswordInput = document.getElementById("confirmPassword");
const strengthText = document.getElementById("strength");

const disposableDomains = ["tempmail.com", "10minutemail.com"];

const locationData = {
    India: {
        Uttarakhand: ["Haldwani", "Dehradun"],
        Maharashtra: ["Mumbai", "Pune"]
    },
    USA: {
        California: ["Los Angeles", "San Diego"],
        Texas: ["Dallas", "Austin"]
    }
};

/* ---------------- Dropdown Logic ---------------- */

countrySelect.addEventListener("change", function () {
    stateSelect.innerHTML = "";
    citySelect.innerHTML = "";
    
    const selectedCountry = this.value;
    if (!selectedCountry) return;

    const states = Object.keys(locationData[selectedCountry]);
    stateSelect.innerHTML = `<option value="">Select State</option>`;
    
    states.forEach(state => {
        const option = document.createElement("option");
        option.value = state;
        option.textContent = state;
        stateSelect.appendChild(option);
    });
});

stateSelect.addEventListener("change", function () {
    citySelect.innerHTML = "";
    const country = countrySelect.value;
    const state = this.value;

    if (!country || !state) return;

    const cities = locationData[country][state];
    citySelect.innerHTML = `<option value="">Select City</option>`;

    cities.forEach(city => {
        const option = document.createElement("option");
        option.value = city;
        option.textContent = city;
        citySelect.appendChild(option);
    });
});

/* ---------------- Password Strength ---------------- */

passwordInput.addEventListener("input", function () {
    const value = this.value;

    if (value.length < 6) {
        strengthText.textContent = "Weak";
        strengthText.style.color = "red";
    } else if (/[A-Za-z]/.test(value) && /[0-9]/.test(value)) {
        strengthText.textContent = "Medium";
        strengthText.style.color = "orange";
    } else if (/[A-Za-z]/.test(value) && /[0-9]/.test(value) && /[^A-Za-z0-9]/.test(value)) {
        strengthText.textContent = "Strong";
        strengthText.style.color = "green";
    }
});

/* ---------------- Validation Functions ---------------- */

function showError(input, message) {
    const error = input.nextElementSibling;
    error.textContent = message;
    input.classList.add("error-border");
}

function clearError(input) {
    const error = input.nextElementSibling;
    error.textContent = "";
    input.classList.remove("error-border");
}

function validateEmail(email) {
    if (!email.includes("@")) return false;

    for (let domain of disposableDomains) {
        if (email.endsWith(domain)) {
            return false;
        }
    }
    return true;
}

/* ---------------- Main Validation ---------------- */

form.addEventListener("input", function () {
    let valid = true;

    const firstName = document.getElementById("firstName");
    const lastName = document.getElementById("lastName");
    const email = document.getElementById("email");
    const phone = document.getElementById("phone");
    const gender = document.querySelectorAll("input[name='gender']:checked");
    const terms = document.getElementById("terms");

    if (firstName.value.trim().length < 2) {
        showError(firstName, "Enter valid first name");
        valid = false;
    } else {
        clearError(firstName);
    }

    if (lastName.value.trim().length < 2) {
        showError(lastName, "Enter valid last name");
        valid = false;
    } else {
        clearError(lastName);
    }

    if (!validateEmail(email.value)) {
        showError(email, "Invalid email address");
        valid = false;
    } else {
        clearError(email);
    }

    if (!/^[0-9+]{10,13}$/.test(phone.value)) {
        showError(phone, "Enter valid phone number");
        valid = false;
    } else {
        clearError(phone);
    }

    if (gender.length === 0) {
        valid = false;
    }

    if (passwordInput.value !== confirmPasswordInput.value || passwordInput.value === "") {
        showError(confirmPasswordInput, "Passwords do not match");
        valid = false;
    } else {
        clearError(confirmPasswordInput);
    }

    if (!terms.checked) {
        valid = false;
    }

    submitBtn.disabled = !valid;
});

/* ---------------- Submit ---------------- */

form.addEventListener("submit", function (e) {
    e.preventDefault();

    formMessage.textContent = "Registration Successful! Your profile has been submitted successfully.";
    formMessage.className = "success";

    form.reset();
    submitBtn.disabled = true;
    strengthText.textContent = "";
});
