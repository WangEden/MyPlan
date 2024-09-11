import os
import re


fileList = os.listdir("./")
pattern = r"\.md$"
file_path = [file for file in fileList if re.search(pattern, file)][0]
print("find markdown file: ", file_path)

html_path = "output.html"
html_path = "index.html"
print("target html: ", html_path)

template = """
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="apple-mobile-web-app-capable" content="yes"/>
    <meta name="apple-touch-fullscreen" content="yes"/>
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"/>
    <link rel="manifest" href="./manifest.json"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2048x2732.png" media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2732x2048.png" media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1668x2388.png" media="(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2388x1668.png" media="(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1536x2048.png" media="(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2048x1536.png" media="(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1668x2224.png" media="(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2224x1668.png" media="(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1620x2160.png" media="(device-width: 810px) and (device-height: 1080px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2160x1620.png" media="(device-width: 810px) and (device-height: 1080px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1290x2796.png" media="(device-width: 430px) and (device-height: 932px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2796x1290.png" media="(device-width: 430px) and (device-height: 932px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1179x2556.png" media="(device-width: 393px) and (device-height: 852px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2556x1179.png" media="(device-width: 393px) and (device-height: 852px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1248x2778.png" media="(device-width: 428px) and (device-height: 926px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2778x1248.png" media="(device-width: 428px) and (device-height: 926px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1170x2532.png" media="(device-width: 390px) and (device-height: 844px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2532x1170.png" media="(device-width: 390px) and (device-height: 844px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1125x2436.png" media="(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2436x1125.png" media="(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1242x2688.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2688x1242.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-828x1792.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1792x828.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1242x2208.png" media="(device-width: 414px) and (device-height: 736px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-2208x1242.png" media="(device-width: 414px) and (device-height: 736px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-750x1334.png" media="(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1334x750.png" media="(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-640x1136.png" media="(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"/>
    <link rel="apple-touch-startup-image" href="/img/pwa/splash-1136x640.png" media="(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"/>
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <title>周任务清单</title>
    <link rel="stylesheet" href="./style/style.css" id="myStyle" >
</head>
<body>
    <div id="float-btn-in">
      <i class='bx bxs-zoom-in'></i>
    </div>
    <div id="float-btn-out">
      <i class='bx bxs-zoom-out'></i>
    </div>
    <div id="float-btn-style">
      <i id="styleIcon" class='bx bx-sun'></i>
      <!-- <i class='bx bx-moon' ></i> -->
    </div>
    <div class="container">
    </div>
    <script>
        window.onload = function() {
            var t = new Date().getHours();
            if (t >= 19 || t <= 6) {
                var obj = document.getElementById("myStyle");
                var styleIcon = document.getElementById("styleIcon");
                obj.setAttribute("href", "./style/style-dark.css");
                styleIcon.setAttribute("class", "bx bx-moon");
            }
        }
        const pTags = document.querySelectorAll('p');
        const btnIn = document.getElementById('float-btn-in');
        const btnOut = document.getElementById('float-btn-out');
        const btnStyle = document.getElementById('float-btn-style');

        function adjustFontSize(isIncreasing) {
          pTags.forEach(p => {
            // 获取当前字体大小
            const currentSize = parseFloat(window.getComputedStyle(p).fontSize);
            // 根据isIncreasing标志增大或减小字体大小
            p.style.fontSize = isIncreasing ? `${currentSize + 1}px` : `${currentSize - 1}px`;
          });
        }
        function adjustStyle() {
          var obj = document.getElementById("myStyle");
          var styleIcon = document.getElementById("styleIcon");
          var currentStyle = obj.getAttribute("href");
          if (currentStyle == "./style/style.css") {
            obj.setAttribute("href", "./style/style-dark.css");
            styleIcon.setAttribute("class", "bx bx-moon");
          } else {
            obj.setAttribute("href", "./style/style.css");
            styleIcon.setAttribute("class", "bx bx-sun");
          }
        }
        btnIn.addEventListener('click', () => adjustFontSize(true));
        btnOut.addEventListener('click', () => adjustFontSize(false));
        btnStyle.addEventListener('click', () => adjustStyle());
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</body>
</html>
"""


import markdown
from bs4 import BeautifulSoup


# 读取 Markdown
with open(file_path, 'r', encoding="utf-8") as file:
    md_text = file.read()

# 将内容转成简易的 HTML 节点
html = markdown.markdown(md_text)
# print(html)

# 利用 BeautifulSoup 修改
sourceSoup = BeautifulSoup(html, 'html.parser')
targetSoup = BeautifulSoup(template, 'html.parser')
containerNode = targetSoup.find(class_="container") # 找到容器

# --------------------------------------- test
containerNode.append(sourceSoup)
html = targetSoup.prettify()
with open(html_path, 'w', encoding='utf-8') as file:
    file.write(html)
    print("ok")
# ---------------------------------------
