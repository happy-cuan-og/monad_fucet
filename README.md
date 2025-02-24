# monad_fucet
Monad semi-auto claim Faucet


This project demonstrates how to claim faucet using a Flask server and a JavaScript client. The server-side script (`server.py`) handles the reCAPTCHA token verification and interacts with an external API, while the client-side script (`snippet.js`) generates and sends the reCAPTCHA token to the server.

## Features

- **reCAPTCHA Verification**: The client-side script generates a reCAPTCHA token and sends it to the server for verification.
- **EVM Account Creation**: The server creates a new EVM account for each request.
- **Proxy Support**: The server can be configured to use a proxy for outgoing requests.
- **Logging**: The server logs the private keys of the created EVM accounts to a file (`pk.txt`).

## Installation

### Prerequisites

- Python 3.x
- Browser with javascript support (for running the client-side script)
- Flask (`pip install flask`)
- `requests` library (`pip install requests`)
- `fake_useragent` library (`pip install fake-useragent`)
- `eth_account` library (`pip install eth_account`)
- `flask_cors` library (`pip install flask-cors`)

### Step-by-Step Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/happy-cuan-og/monad_fucet.git
   cd monad_fucet
   ```

2. **Set Up the Python Environment**

   Create a virtual environment and install the required Python packages.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure Proxy**

   If you need to use a proxy for outgoing requests, update the `proxies` dictionary in `server.py` with your proxy details.

   ```python
   proxies = {
       "http": "http://user:pass@ip:port",
       "https": "http://user:pass@ip:port"
   }
   ```

4. **Run the Flask Server**

   Start the Flask server by running the `server.py` script.

   ```bash
   python server.py
   ```

   The server will start on `http://127.0.0.1:5000`.


5. **Open Your browser**
    Goto https://testnet.monad.xyz/

    Open devtools

    Execute this script

    ```javascript
    function executeRecaptcha() {
    grecaptcha.execute('6Lf_xd8qAAAAANYpu_MCMXZA0A2_0F9wgB3pKs5j', {action: 'drip_request'}).then(function(token) {
        console.log("Token reCAPTCHA:", token);

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

    setInterval(executeRecaptcha, 10000);

## Usage

1. **Start the Server**: Ensure the Flask server is running.
2. **Run the Client Script**: Execute the `snippet.js` script in your browser.
3. **Monitor Logs**: Check the `pk.txt` file for logged Ethereum private keys and the console for server responses.

## Troubleshooting

- **reCAPTCHA Errors**: Ensure that the reCAPTCHA score is 0.9 check your score here [https://2captcha.com/demo/recaptcha-v3](https://2captcha.com/demo/recaptcha-v3).
- **Proxy Issues**: Verify that the proxy settings in `server.py` are correct and that the proxy server is accessible.
- **SSL Errors**: If you encounter SSL errors, ensure that the server has access to the necessary SSL certificates.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- reCAPTCHA: [https://www.google.com/recaptcha/](https://www.google.com/recaptcha/)