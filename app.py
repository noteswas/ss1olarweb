from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>ss1olarr</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        * { cursor: url('https://r2.guns.lol/02474717-e633-4558-8434-7b27cf998e3b.png'), auto !important; }

        body, html {
            margin: 0; padding: 0; width: 100%; height: 100%;
            background: #000; color: white; font-family: 'Roboto', sans-serif;
            overflow: hidden;
        }

        #bgvideo {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            object-fit: cover; z-index: 1;
            filter: brightness(0.6);
            background: #000;
        }

        #intro {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(40px);
            display: flex; justify-content: center; align-items: center;
            z-index: 100; transition: all 1.5s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
        }

        #intro.hide { opacity: 0; pointer-events: none; backdrop-filter: blur(0px); }

        .enter-text {
            font-size: 16px; letter-spacing: 6px; opacity: 0.4;
            text-transform: uppercase;
            animation: pulse 2s infinite ease-in-out;
        }

        @keyframes pulse { 0%, 100% { opacity: 0.3; } 50% { opacity: 0.8; } }

        .overlay {
            position: relative; width: 100%; height: 100%;
            display: flex; flex-direction: column; justify-content: center;
            align-items: center; z-index: 2;
            text-align: center;
            pointer-events: none; /* Чтобы не мешать клику по интро изначально */
        }
        
        .show.overlay { pointer-events: auto; }

        .fade-item {
            opacity: 0; transform: translateY(25px); filter: blur(15px);
            transition: all 1.2s ease-out;
        }

        .show .fade-item { opacity: 1; transform: translateY(0); filter: blur(0px); }

        .delay-1 { transition-delay: 0.4s; }
        .delay-2 { transition-delay: 0.8s; }
        .delay-3 { transition-delay: 1.2s; }

        .avatar {
            width: 125px; height: 125px; border-radius: 50%;
            border: 2px solid #fff; margin: 25px 0; object-fit: cover;
        }

        .button-container { 
            display: flex; justify-content: center; gap: 15px; margin-top: 30px; 
        }

        .social-link {
            opacity: 0; transform: scale(0.5);
            transition: all 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .show .social-link { opacity: 1; transform: scale(1); }

        .show .social-link:nth-child(1) { transition-delay: 1.6s; }
        .show .social-link:nth-child(2) { transition-delay: 1.7s; }
        .show .social-link:nth-child(3) { transition-delay: 1.8s; }
        .show .social-link:nth-child(4) { transition-delay: 1.9s; }
        .show .social-link:nth-child(5) { transition-delay: 2.0s; }

        .button-container a {
            display: flex; align-items: center; justify-content: center;
            width: 54px; height: 54px;
            background: rgba(255, 255, 255, 0.1); 
            backdrop-filter: blur(10px);
            border-radius: 14px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            transition: all 0.4s ease;
        }

        .button-container img, .button-container svg {
            width: 26px; height: 26px;
            filter: brightness(0) invert(1) drop-shadow(0 0 5px rgba(255, 255, 255, 0.7));
        }

        .button-container a:hover { 
            transform: translateY(-8px);
            background: rgba(255, 255, 255, 0.2);
            box-shadow: 0 5px 20px rgba(255, 255, 255, 0.2);
        }

        footer { position: absolute; bottom: 20px; width: 100%; font-size: 11px; color: #444; letter-spacing: 1px; }
    </style>
</head>
<body>

    <video id="bgvideo" loop muted playsinline>
        <source src="https://cdn.pixabay.com/video/2026/02/22/335998.mp4" type="video/mp4">
    </video>

    <div id="intro" onclick="startExperience()">
        <div class="enter-text">click to enter</div>
    </div>

    <div class="overlay" id="main-content">
        <h1 class="fade-item delay-1" style="font-size: 50px; margin: 0; font-weight: 700;">ss1olarr</h1>
        <img class="avatar fade-item delay-2" src="https://r2.guns.lol/bf9fd2a6-7e37-454d-986f-681c52836bec.webp">
        <p class="fade-item delay-3" style="max-width: 500px; margin: 0 25px; font-size: 18px; opacity: 0.7; line-height: 1.6;">
            yo! im ssolar, a dev of many games in roblox made by ehoriliaOOO!
        </p>

        <div class="button-container">
            <div class="social-link"><a href="https://discord.gg/Up9d2kwEWR" target="_blank">
                <svg viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028 14.09 14.09 0 0 0 1.226-1.994.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.23 10.23 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.196.373.291a.077.077 0 0 1-.006.127 12.29 12.29 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
            </a></div>
            <div class="social-link"><a href="https://t.me/RobStudio1" target="_blank">
                <svg viewBox="0 0 24 24"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0zm4.962 8.224c.127.01.127.01.127.01l-1.907 9.013c-.145.64-.52 1.144-1.092 1.144-.572 0-.858-.415-1.282-.843l-2.073-1.638-1.002-.914c-.167-.146-.333-.292-.49-.44l.024-.03L15.3 9.4c.057-.053.057-.107-.057-.107-.114 0-.17.054-.227.107L7.433 14.54l-2.413-.76c-.52-.164-.52-.516.113-.76l9.642-3.714c.45-.164.886-.067 1.17.266.284.333.284.714.053 1.05z"/></svg>
            </a></div>
            <div class="social-link"><a href="https://guns.lol/ss1olarr" target="_blank">
                <img src="https://assets.guns.lol/favicon/apple-touch-icon.png">
            </a></div>
            <div class="social-link"><a href="https://www.youtube.com/@ss1olar" target="_blank">
                <svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
            </a></div>
            <div class="social-link"><a href="https://www.tiktok.com/@ss1olar" target="_blank">
                <svg viewBox="0 0 24 24"><path d="M12.525.02c1.31-.032 2.61-.019 3.91-.019 0 1.22.015 2.445-.005 3.664.54.02 1.1.192 1.63.339.31.083.61.18.9.313a5.552 5.552 0 0 0 2.485 1.1c.01 1.33.01 2.66-.01 3.99-.88-.059-1.75-.414-2.485-.884-.32-.204-.62-.437-.902-.693v7.013c.01 2.89-.92 5.842-3.53 7.323a7.35 7.35 0 0 1-5.23.43c-2.6-.58-4.75-2.74-5.33-5.33a7.33 7.33 0 0 1 1.43-6.53c1.41-1.63 3.73-2.58 5.84-2.31v4.03a3.39 3.39 0 0 0-2.11 1.48c-.85 1.34-.35 3.33 1.1 4.14 1.25.7 3.09.24 3.77-1.04.21-.41.31-.87.3-1.33V0l.015.02z"/></svg>
            </a></div>
        </div>
        <footer>tiny site made by ssolar</footer>
    </div>

    <script>
        function startExperience() {
            document.getElementById('intro').classList.add('hide');
            document.getElementById('main-content').classList.add('show');
            const video = document.getElementById('bgvideo');
            if (video) {
                video.play().catch(error => {
                    console.log("Видео не смогло запуститься автоматически:", error);
                });
            }
        }
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
