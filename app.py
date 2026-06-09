from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask 部署测试成功</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0;
                color: #fff;
            }
            .card {
                background: rgba(255,255,255,0.15);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 48px 64px;
                text-align: center;
                box-shadow: 0 8px 32px rgba(0,0,0,0.2);
            }
            h1 { margin-top: 0; font-size: 2.5em; }
            p { font-size: 1.2em; opacity: 0.9; }
            .badge {
                display: inline-block;
                background: #10b981;
                padding: 6px 16px;
                border-radius: 999px;
                font-weight: bold;
                margin-top: 16px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🎉 部署成功！</h1>
            <p>你的 Flask 网站已经跑起来了</p>
            <span class="badge">Flask + Render ✅</span>
            <p style="margin-top:24px; font-size:0.9em; opacity:0.7;">
                Python 版本: 3.x &nbsp;|&nbsp; 路由: /health
            </p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "ok", "service": "flask-test-app"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
