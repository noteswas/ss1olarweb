from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<html>
<head>
    <title>ss1olarr</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        /* --- КАСТОМНЫЙ КУРСОР --- */
        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            min-height: 100vh;
            font-family: 'Roboto', sans-serif;
            overflow: hidden;
            text-align: center;
            color: white;
            background: #000;
            /* Устанавливаем твой курсор для всего сайта */
            cursor: url('https://r2.guns.lol/02474717-e633-4558-8434-7b27cf998e3b.png'), auto;
        }

        /* Чтобы курсор не менялся на стандартный при наведении на ссылки и кнопки */
        a, button, .button-container img, #intro {
            cursor: url('https://r2.guns.lol/02474717-e633-4558-8434-7b27cf998e3b.png'), pointer !important;
        }

        #bgvideo {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
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
            justify(content): center;
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
            box-shadow: 0 0 15px rgba(255,255,255,0.3);
        }

        h1.site-title {
            font-size: 48px;
            margin-bottom: 10px;
            text-shadow: 2px 2px 8px #000;
        }

        p.site-desc {
            font-size: 18px;
            max-width: 500px;
            margin: 0 auto 30px;
            padding: 0 15px;
            line-height: 1.5;
            color: #ddd;
        }

        .button-container {
            display: flex;
            justify-content: center;
            gap: 25px;
            flex-wrap: wrap;
            margin-top: 20px;
        }

        .button-container a {
            text-decoration: none;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.5s ease;
        }

        .overlay.show .button-container a {
            opacity: 1;
            transform: translateY(0);
        }

        .button-container img {
            width: 42px;
            height: 42px;
            filter: brightness(0) invert(1) drop-shadow(0 0 5px rgba(255, 255, 255, 0.8));
            transition: all 0.3s ease;
        }

        .button-container img:hover {
            transform: scale(1.25);
            filter: brightness(0) invert(1) drop-shadow(0 0 15px rgba(255, 255, 255, 1));
        }

        /* Задержка появления иконок */
        .button-container a:nth-child(1) { transition-delay: 0.2s; }
        .button-container a:nth-child(2) { transition-delay: 0.3s; }
        .button-container a:nth-child(3) { transition-delay: 0.4s; }
        .button-container a:nth-child(4) { transition-delay: 0.5s; }
        .button-container a:nth-child(5) { transition-delay: 0.6s; }

        footer {
            position: absolute;
            bottom: 30px;
            width: 100%;
            font-size: 13px;
            color: #888;
            letter-spacing: 1px;
        }

        @media (max-width: 480px) {
            #intro h1 { font-size: 32px; }
            .avatar { width: 100px; height: 100px; }
            h1.site-title { font-size: 32px; }
            .button-container img { width: 35px; height: 35px; }
        }
    </style>
</head>
<body>

<video autoplay loop muted playsinline id="bgvideo">
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
        <a href="https://discord.gg/Up9d2kwEWR" target="_blank">
            <img src="https://www.svgrepo.com/show/353655/discord-icon.svg">
        </a>
        <a href="https://t.me/RobStudio1" target="_blank">
            <img src="https://www.svgrepo.com/show/349526/telegram.svg">
        </a>
        <a href="https://guns.lol/ss1olarr" target="_blank">
            <img src="https://assets.guns.lol/guns_logo_no_background_cropped.png">
        </a>
        <a href="https://www.youtube.com/@ss1olar" target="_blank">
            <img src="https://www.svgrepo.com/show/475692/youtube-color.svg">
        </a>
        <a href="https://www.tiktok.com/@ss1olar" target="_blank">
            <img src="https://www.svgrepo.com/show/342294/tiktok.svg">
        </a>
    </div>

    <footer>
        tiny site made by ssolar
    </footer>
</div>

<script>
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
