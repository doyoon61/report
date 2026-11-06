from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>휴먼 IT 교육센터</title>
        <style>
            body { font-family: sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
            h1 { color: #333; }
            .box { background: white; padding: 20px; margin: 20px auto; width: 60%; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            ul { text-align: left; display: inline-block; }
        </style>
    </head>
    <body>
        <h1>휴먼 IT 교육센터에 오신 것을 환영합니다!</h1>
        <p>최신 IT 트렌드에 맞춘 실무 중심의 교육 과정을 만나보세요.</p>

        <div class="box">
            <h3>🔥 개설된 교육 과정</h3>
            <ul>
                <li><strong>AI 기반 지능형 서비스 개발자 양성과정</strong> (파이썬, AI, RAG 활용)</li>
                <li><strong>클라우드 기반 풀스택 Web Developer 과정</strong> (자바, 리액트, 웹개발)</li>
            </ul>
        </div>
    </body>
    </html>
"""