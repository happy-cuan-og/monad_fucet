function executeRecaptcha() {
    grecaptcha.execute('6LdOf-EqAAAAAAKJ2QB6IqnJfsOl13El4XZwRD8c', {action: 'drip_request'}).then(function(token) {
        console.log("Token reCAPTCHA:", token);

        // Send recaptcha token with fetch
        fetch("http://127.0.0.1:5000/submit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                recaptcha_token: token
            })
        })
        .then(response => response.json())
        .then(data => console.log("Server response:", data))
        .catch(error => console.error("Error:", error));
    });
}

// Running excuteRecaptcha
setInterval(executeRecaptcha, 10000);