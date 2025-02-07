html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Rose Day, My Love!</title>
    <style>
        body {
            background-color: #ffcccc;
            text-align: center;
            font-family: Arial, sans-serif;
            overflow: hidden;
        }
        h1 {
            color: #d63384;
            font-size: 50px;
            margin-top: 20px;
        }
        p {
            color: #b30000;
            font-size: 20px;
            font-weight: bold;
        }
        .heart, .rose {
            position: absolute;
            width: 50px;
            height: 50px;
            animation: float 5s infinite;
        }
        @keyframes float {
            0% { transform: translateY(100vh) scale(0.5); opacity: 1; }
            100% { transform: translateY(-10vh) scale(1); opacity: 0; }
        }
    </style>
</head>
<body>
    <h1>Happy Rose Day, My Love! 🌹❤️</h1>
    <p>You are the rose that fills my life with love and happiness! I love you forever! 💖</p>

    <script>
        function createElement(type, src) {
            let elem = document.createElement("img");
            elem.src = src;
            elem.className = type;
            elem.style.left = Math.random() * window.innerWidth + "px";
            elem.style.animationDuration = Math.random() * 2 + 3 + "s";
            document.body.appendChild(elem);
            setTimeout(() => { elem.remove(); }, 5000);
        }

        setInterval(() => createElement('heart', 'https://cdn-icons-png.flaticon.com/512/833/833472.png'), 500);
        setInterval(() => createElement('rose', 'https://cdn-icons-png.flaticon.com/512/4151/4151695.png'), 1000);
    </script>
</body>
</html>
"""

with open("rose_day.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML file 'rose_day.html' created successfully! Open it in a browser.")