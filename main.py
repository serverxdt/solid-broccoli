from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
 <!DOCTYPE html>
 <html lang="en">
 <head>
 	<meta charset="UTF-8">
 	<meta name="viewport" content="width=device-width, initial-scale=1.0">
 	<title> 𝗢𝗙𝗙𝗟𝗜𝗡𝗘 𝗦𝗘𝗥𝗩𝗘𝗥 BLACK SHADOW 𝗥𝗨𝗟𝗘𝗫 😈</title>
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"> 
     <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('https://i.imgur.com/uMwcqtB.jpeg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 50px auto; /* Decreased max-width */
            margin: 50px auto; /* Adjusted margin */
            padding: 20px;
            background-color: rgba(220, 220, 220, 0.5); /* Transparent white background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: white;
            border: 1.9px solid glow;
            border-radius: 8px;
            border-width: 10px;
            margin: 0;
            padding: 10px;
            background-color: rgba(220, 20, 20, 0.5); /* Transparent red background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
          }
        h2 {
            text-align: center;
            color: white;
            border: 1.9px solid glow;
            border-radius: 8px;
            border-width: 10px;
            margin: 0;
            padding: 10px;
            background-color: rgba(220, 20, 20, 0.5); /* Transparent red background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        label {
            font-weight: bold;
            color: auto;
            display: block;
            margin: 15px 0 5px;
        }
        .input {
            margin: 10px;
            background-color: rgba(220, 220, 220, 0.5) ;
            border: none;
            outline: none;
            max-width: 360px;
            padding: 20px 30px;
            font-size: 10px;
            border-radius: 9999px;
            box-shadow: inset 2px 5px 10px rgb(5, 5, 5);
            color: #fff;
        }
        input[type="text"], input[type="number"], input[type="file"] {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .submit-btn {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .submit-btn:hover {
            background-color: #b0b300;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: cyan;
        }
    </style>
</head>
<body>
  <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Services - Henry X Samar</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        :root {
            --background-image: url('https://i.imgur.com/mPu4nnK.jpeg');
        }
    </style>
    <link rel="stylesheet" href="/static/css/main.css">
    <script>
        // Initialize the login state
        let isLoggedIn = false;
        let isTrialActive = false;

        // Function to handle login
        function handleLogin(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            if (username === 'ISHU' && password === 'ISHU_99') {
                isLoggedIn = true;
                document.getElementById('login-section').style.display = 'none'; // Hide login
                document.getElementById('subscription-section').style.display = 'block';
            } else {
                alert('Invalid credentials! Please try again.');
            }
        }

        // Function to handle subscription selection
        function chooseSubscription(type) {
            if (type === 'Free Trial') {
                alert("You have selected the Free Trial! Enjoy your 7 days.");
                isTrialActive = true;
                showServices();
            } else if (type === 'Monthly Subscription') {
                alert("You will be redirected to payment.");
                window.location.href = "https://wa.me/+91923574160?text=Sir%2C%20I%20am%20paying%20your%20server%201k.%20Please%20send%20me%20your%20bank%20number.";
            }
        }

        // Function to show services
        function showServices() {
            if (isTrialActive) {
                document.getElementById('services-section').style.display = 'block'; // Show services
            }
        }

        // Function to handle page load
        window.onload = function() {
            document.getElementById('subscription-section').style.display = 'none'; // Hide subscription options
            document.getElementById('services-section').style.display = 'none'; // Hide services
        };
    </script>
</head>
<body>
    <nav class="navbar p-4 shadow-md">
        <div class="container mx-auto flex justify-between items-center">
            <h2 class="text-2xl font-bold">Henry X Samar</h2>
            <div class="lg:hidden">
                <span id="menu-btn" class="navbar-icon text-2xl">
                    <i class="fas fa-bars"></i>
                </span>
            </div>
        </div>
    </nav>

    <!-- Login Section -->
    <div id="login-section" class="container mx-auto px-4 py-16 text-center">
        <h2 class="text-3xl font-bold">Login</h2>
        <form onsubmit="handleLogin(event)" class="mt-4">
            <input type="text" id="username" placeholder="Username" required 
                   class="border rounded px-4 py-2 mb-4" />
            <input type="password" id="password" placeholder="Password" required 
                   class="border rounded px-4 py-2 mb-4" />
            <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">Login</button>
        </form>
    </div>

    <!-- Subscription Options Section -->
    <div id="subscription-section" class="container mx-auto px-4 py-16 text-center">
        <h2 class="text-3xl font-bold">Choose Your Subscription</h2>
        <div class="mt-6">
               <img src="https://i.imgur.com/1AKZp6Z.jpeg" style="width: 100%; height: auto; border-radius: 12px;">
            <button onclick="chooseSubscription('Free Trial')" class="bg-blue-500 text-white px-4 py-2 rounded mx-2">Free Trial (7 Days)</button>
            <button onclick="chooseSubscription('Monthly Subscription')" class="bg-red-500 text-white px-4 py-2 rounded mx-2">Monthly Subscription (500/month)</button>
        </div>
    </div>

    <!-- Services Section -->
    <div id="services-section" class="container mx-auto px-4 py-16">
        <h1 class="text-3xl font-bold text-center text-primary mb-8">𝐻𝐸𝑁𝑅𝑌 𝐗 𝑆𝐴𝑀𝐴𝑅 2.</h1>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="container">
                    <img src="https://i.imgur.com/BqCpF7N.jpeg" alt="SINGLE CONVO">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">SINGLE CONVO</h3>
                <p>Ultimate Facebook Message Sender Tool.</p>
                <a href="https://ishu-server.onrender.com/" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            </div>

            <div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
                <div class="card-img service mt-4 mb-4">
                    <img src="https://i.imgur.com/IdljQMA.jpeg" alt="Mᴜʟᴛʏ Cᴏɴᴠᴏ">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">Mᴜʟᴛʏ Cᴏɴᴠᴏ</h3>
                <p>Multi Convo By Multi Tokens.</p>
                <a href="https://ishu-server.onrender.com/" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            </div>

            <div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
                <div class="card-img service mt-4 mb-4">
                    <img src="https://imgur.com/J3EaW4o.jpeg" alt="Offline Sever">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">Post Server</h3>
                <p> Updated Postt Tool</p>
                <a href="https://web-production-d3ce.up.railway.app/" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            </div>

            <div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
                <div class="card-img service mt-4 mb-4">
                    <img src="https://imgur.com/VtZI9Yj.jpeg" alt="Tᴏᴋᴇɴ Cʜᴇᴄᴋᴇʀ">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">Tᴏᴋᴇɴ Cʜᴇᴄᴋᴇʀ</h3>
                <p>Get Token Checker.</p>
                <a href="https://ok-lnq6.vercel.app/" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            </div>

            <div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
                <div class="card-img service mt-4 mb-4">
                    <img src="https://imgur.com/p8p6rDL.jpeg" alt="Cᴏᴍᴍᴇɴᴛ ᴛᴏᴏʟ">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">Cᴏᴍᴍᴇɴᴛ Tᴏᴏʟ</h3>
                <p>Get Send Unlimited Comment By Cookie's Using Comment Tool</p>
                <a href="coming soon" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            </div>

            <div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
                <div class="card-img service mt-4 mb-4">
                    <img src="https://i.imgur.com/Z1ovbj0.jpeg" alt="Wʜᴀᴛsᴀᴘᴘ Lᴏᴅᴇʀ">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">Wʜᴀᴛsᴀᴘᴘ Lᴏᴅᴇʀ</h3>
                <p>Profile & Termux WhatsApp Loader</p>
                <a href="coming soon" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            </div>
        </div>
    </div>

    <footer class="footer py-6">
        <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
            <div class="mb-4 md:mb-0">
                <a href="/terms" class="hover:text-primary">Terms</a>
                <span class="mx-2">|</span>
                <a href="/privacy" class="hover:text-primary">Privacy</a>
            </div>

            <div class="flex space-x-4">
                <a href="https://www.facebook.com/profile.php?id=100021951578613" class="text-2xl hover:text-primary"><i class="fab fa-facebook"></i></a>
                <a href="https://wa.me/+919584720412" class="text-2xl hover:text-primary"><i class="fab fa-whatsapp"></i></a>
                <a href="https://github.com" class="text-2xl hover:text-primary"><i class="fab fa-github"></i></a>
            </div>

            <div class="mt-4 md:mt-0 text-center">
                <p>© 2024 MADE BY HENRY X SAMAR. All Rights Reserved.</p>
                <p>Owner ❤️ by <a href="https://www.facebook.com/profile.php?id=100021951578613">ISHU'W</a></p>
            </div>
        </div>
    </footer>

    <script src="/static/js/menu.js"></script>
</body>
</html>
 '''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
