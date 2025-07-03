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
        <h2 class="text-3xl font-bold text-center text-primary mb-8">HENRY 2.0</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Service Cards -->
            <div class="bg-white rounded-lg shadow-lg p-15 text-center relative">
                <div class="card-img service img-center mt-4 mb-4">
                    <img src="https://i.imgur.com/o4BipKB.gif" alt="SINGLE CONVO">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">SINGLE CONVO</h3>
                <p>Sigle Convo Tool By Henry Click The View Botttom And Use.</p>
                <a href="https://singelnew-9mxs.onrender.com/"style="color: blue "mt-4 color-blue inline-block px-6 py-2 btn-primary rounded-lg">View</button>
            </div>


    
            <div class="bg-white rounded-lg shadow-lg p-15 text-center relative">
                <div class="card-img service img-center mt-4 mb-4">
                    <img src="https://i.ibb.co/WpdhRtsn/s-Fws-F2sh-YWPerb-KYPd.gif" alt="FREE CONVO">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">MULTY CONVO</h3>
                <p>Multy Convo Tool By Henry Click The View Botttom And Use.</p>
                <a href="https://evil-fay-zohan-21e195f3.koyeb.app/"style="color: blue "mt-4 color-blue inline-block px-6 py-2 btn-primary rounded-lg">View</button>
            </div>


     <div id="services-section" class="container mx-auto px-4 py-16">
        <h2 class="text-3xl font-bold text-center text-primary mb-8"> </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Service Cards -->
            <div class="bg-white rounded-lg shadow-lg p-15 text-center relative">
                <div class="card-img service img-center mt-4 mb-4">
                    <img src="https://i.ibb.co/nMm8ZsBj/h-PMG9pb-IRXdksa-YA4-D-2.gif" alt="uid + post uid extractor">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">Post uid + uid</h3>
                <p>Paid Tool By Henry Click The View Botttom And Use</p>
                <a href=""style="color: blue "mt-4 color-blue inline-block px-6 py-2 btn-primary rounded-lg">View</button>
            </div>


    <div id="services-section" class="container mx-auto px-4 py-16">
        <h2 class="text-3xl font-bold text-center text-primary mb-8"> </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Service Cards -->
            <div class="bg-white rounded-lg shadow-lg p-15 text-center relative">
                <div class="card-img service img-center mt-4 mb-4">
                    <img src="https://i.imgur.com/kNmsmiT.gif" alt="uid + post uid extractor">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">Post uid + uid</h3>
                <p>Post Commenter cookies By Henry Click The View Botttom And Use.</p>
                <a href="https://web-page-w0sz.onrender.com/"style="color: blue "mt-4 color-blue inline-block px-6 py-2 btn-primary rounded-lg">View</button>
            </div>

    <div id="services-section" class="container mx-auto px-4 py-16">
        <h2 class="text-3xl font-bold text-center text-primary mb-8"> </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Service Cards -->
            <div class="bg-white rounded-lg shadow-lg p-15 text-center relative">
                <div class="card-img service img-center mt-4 mb-4">
                    <img src="https://i.ibb.co/vCnBPGR0/Sxj-Rmxrh-Pg-DHujk1s-H-1.gif" alt="Token + Gc Uid Extractor">
                </div>
                <h3 class="text-2xl font-bold text-primary mb-4">Post uid + uid</h3>
                <p>Token + gc uid Chekcer By Henry Click The View Botttom And Use.</p>
                <a href="https://token1-x2va.onrender.com/"style="color: blue "mt-4 color-red inline-block px-6 py-2 btn-primary rounded-lg">View</button>
            </div>
    <footer class="footer py-6">
        <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
            <div class="mb-4 md:mb-0">
                <a href="/terms" class="hover:text-primary">Terms</a>
                <span class="mx-2">|</span>
                <a href="/privacy" class="hover:text-primary">Privacy</a>
            </div>

            <div class="flex space-x-4">
                <a href="https://www.facebook.com/Henry.inxide" class="text-2xl hover:text-primary">God Abhser + Haters Fuck3d By Owner Henry<i class="fab fa-facebook"></i></a>
                <a href="https://wa.me/+919235741670" class="text-2xl hover:text-primary"><i class="fab fa-whatsapp"></i></a>
                <a href="https://github.com" class="text-2xl hover:text-primary"><i class="fab fa-github"></i></a>
            </div>

            <div class="mt-4 md:mt-0 text-center">
                <p>© 2024 MADE BY HENRY. All Rights Reserved.</p>
                <p>Owner ❤️ by <a href="https://www.facebook.com/Henry.inxide">HENRY'W</a></p>
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
