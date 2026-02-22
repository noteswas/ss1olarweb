from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<html>
<head>
    <title>ss1olarr</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- favicon -->
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            min-height: 100vh;
            font-family: 'Roboto', sans-serif;
            overflow: hidden;
            text-align: center;
            color: white;
        }

        #bgvideo {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            min-height: 100vh;
            object-fit: cover;
            z-index: -2;
        }

        #intro {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.4);
            backdrop-filter: blur(15px);
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            z-index: 2;
            transition: opacity 1s ease;
        }

        #intro.hide {
            opacity: 0;
            pointer-events: none;
        }

        #intro h1 {
            font-size: 48px;
            margin: 0;
            text-shadow: 2px 2px 8px #000;
        }

        #intro p {
            font-size: 24px;
            margin-top: 10px;
        }

        .overlay {
            position: relative;
            background-color: rgba(0,0,0,0.6);
            width: 100%;
            height: 100%;
            padding-top: 50px;
            box-sizing: border-box;
            opacity: 0;
            transition: opacity 1s ease;
        }

        .overlay.show {
            opacity: 1;
        }

        .avatar {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            border: 3px solid #fff;
            margin-bottom: 20px;
            object-fit: cover;
        }

        h1.site-title {
            font-size: 48px;
            margin-bottom: 20px;
            text-shadow: 2px 2px 8px #000;
        }

        p.site-desc {
            font-size: 18px;
            margin-bottom: 30px;
            padding: 0 10px;
        }

        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 20px;
        }

        .icon-only {
            width: 60px !important;
            height: 60px !important;
            cursor: pointer;
        }

        footer {
            margin-top: 50px;
            font-size: 14px;
            color: #aaa;
        }

        @media (max-width: 480px) {
            #intro h1 { font-size: 32px; }
            #intro p { font-size: 18px; }
            .avatar { width: 100px; height: 100px; }
            .site-title { font-size: 32px; }
            .site-desc { font-size: 16px; }
            .icon-only { width: 50px !important; height: 50px !important; }
            .button-container { gap: 15px; margin-top: 15px; }
        }
    </style>
</head>
<body>

<video autoplay loop muted id="bgvideo">
    <source src="https://r2.guns.lol/dfe3d4d8-50cb-457b-826c-332733670778.mp4" type="video/mp4">
</video>

<div id="intro">
    <h1>ss1olarr</h1>
    <p>click to enter</p>
</div>

<div class="overlay">
    <img class="avatar" src="https://r2.guns.lol/bf9fd2a6-7e37-454d-986f-681c52836bec.webp" alt="Avatar">
    <h1 class="site-title">ss1olarr</h1>
    <p class="site-desc">yo! im ssolar, a dev of many games in roblox made by ehoriliaOOO! (he doesnt pay me) yeah i dont know what else to add so bye</p>

    <div class="button-container">
        <!-- Discord -->
        <a href="https://discord.gg/Up9d2kwEWR" target="_blank">
            <img class="icon-only" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzBLaLqWJZBXlMzkbnTETwPP0W89GdLjt-CA&s">
        </a>

        <!-- Telegram -->
        <a href="https://t.me/RobStudio1" target="_blank">
            <img class="icon-only" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/1280px-Telegram_2019_Logo.svg.png">
        </a>

        <!-- Guns -->
        <a href="https://guns.lol/ss1olarr" target="_blank">
            <img class="icon-only" src="https://assets.guns.lol/guns_logo_no_background_cropped.png">
        </a>

        <!-- YouTube -->
        <a href="https://www.youtube.com/@ss1olar" target="_blank">
            <img class="icon-only" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/960px-YouTube_full-color_icon_%282017%29.svg.png">
        </a>

        <!-- TikTok (оставим как обычная иконка, можно сделать без фона, если нужно) -->
        <a href="https://www.tiktok.com/@ss1olar" target="_blank">
            <img class="icon-only" src="https://upload.wikimedia.org/wikipedia/en/a/a9/TikTok_logo.svg">
        </a>
    </div>

    <footer>
        tiny site made by ssolar
    </footer>
</div>

<script>
    function setVh() {
        document.documentElement.style.setProperty('--vh', window.innerHeight * 0.01 + 'px');
    }
    window.addEventListener('resize', setVh);
    setVh();

    const intro = document.getElementById('intro');
    const overlay = document.querySelector('.overlay');
    intro.addEventListener('click', () => {
        intro.classList.add('hide');
        overlay.classList.add('show');
    });
</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
