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
            
            background-color: black;
      }
    </style>
</head>
<body>
    <!-- Services Section -->
    <div id="services-section" class="container mx-auto px-4 py-16">
        <h1 class="text-3xl font-bold text-center text-primary mb-8">𝐻𝐸𝑁𝑅𝑌 𝐗 𝑆𝐴𝑀𝐴𝑅 2.</h1>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            
                    <img src="https://i.imgur.com/BqCpF7N.jpeg" alt="SINGLE CONVO">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">SINGLE CONVO</h3>
                <p>Ultimate Facebook Message Sender Tool.</p>
                <a href="https://ishu-server.onrender.com/" class="color-blue mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
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
