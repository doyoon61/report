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
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NEXT TECH ACADEMY - 미래 IT 실무 양성 전문 기관</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Pretendard', sans-serif; }
            body { background-color: #0b0f19; color: #f8fafc; line-height: 1.6; }
            header { background: linear-gradient(to bottom, #0f172a, #0b0f19); padding: 60px 20px; text-align: center; border-bottom: 1px solid #1e293b; }
            header h1 { font-size: 38px; font-weight: 800; margin-bottom: 15px; color: #fff; }
            header p { color: #94a3b8; font-size: 16px; max-width: 600px; margin: 0 auto; }
            .container { max-width: 1100px; margin: 40px auto; padding: 0 20px; }
            .section-title { text-align: center; font-size: 26px; font-weight: 700; margin-bottom: 30px; color: #fff; }
            .course-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px; }
            .course-card { background: #111827; border: 1px solid #1f2937; border-radius: 16px; padding: 30px; transition: transform 0.2s; }
            .course-card:hover { transform: translateY(-5px); border-color: #3b82f6; }
            .tag { display: inline-block; background: #1e3a8a; color: #60a5fa; font-size: 12px; font-weight: bold; padding: 4px 10px; border-radius: 6px; margin-bottom: 15px; }
            .course-card h3 { font-size: 20px; margin-bottom: 12px; color: #fff; }
            .course-card p { font-size: 14px; color: #9ca3af; margin-bottom: 20px; }
            .course-info { font-size: 13px; color: #d1d5db; border-top: 1px solid #1f2937; padding-top: 15px; }
            footer { text-align: center; padding: 40px 0; color: #6b7280; font-size: 13px; border-top: 1px solid #1f2937; margin-top: 60px; }
        </style>
    </head>
    <body>

        <header>
            <h1>내일을 바꾸는 IT 실무 역량<br>최고의 전문 교육 기관에서 시작하세요</h1>
            <p>비전공자도 6개월 만에 네카라쿠배형 개발자로! 현업 최상위 개발자의 1:1 밀착 코칭을 제공합니다.</p>
        </header>

        <div class="container">
            <h2 class="section-title">🚀 기업이 지금 당장 탐내는 핵심 IT 교육 과정</h2>
            <div class="course-grid">

                <!-- 과정 1 -->
                <div class="course-card">
                    <span class="tag">국비지원 100%</span>
                    <h3>풀스택 웹 개발자 커리어 Track</h3>
                    <p>JavaScript/TypeScript 중심의 프론트엔드부터 백엔드, 클라우드 배포까지 다루는 웹 개발 완전 정복 프로젝트.</p>
                    <div class="course-info">
                        ⏱ <strong>교육 기간:</strong> 6개월 (총 960시간)<br>
                        👥 <strong>정원:</strong> 기수별 25명 정원제
                    </div>
                </div>

                <!-- 과정 2 -->
                <div class="course-card">
                    <span class="tag">AI / 빅데이터</span>
                    <h3>AI & 데이터 엔지니어링 전문가 과정</h3>
                    <p>Python 기반 머신러닝, 딥러닝 알고리즘 구현과 대용량 데이터 파이프라인 구축을 학습하는 최신 AI 인재 양성 과정.</p>
                    <div class="course-info">
                        ⏱ <strong>교육 기간:</strong> 6개월 (총 920시간)<br>
                        👥 <strong>정원:</strong> 기수별 20명 소수정예
                    </div>
                </div>

                <!-- 과정 3 -->
                <div class="course-card">
                    <span class="tag">클라우드 / 보안</span>
                    <h3>클라우드 DevOps & 보안 전문가 과정</h3>
                    <p>AWS 클라우드 인프라 자동화, CI/CD 파이프라인 구축 및 데브옵스 환경에서의 보안(DevSecOps) 실무 전수.</p>
                    <div class="course-info">
                        ⏱ <strong>교육 기간:</strong> 5개월 (총 800시간)<br>
                        👥 <strong>정원:</strong> 기수별 20명 정원제
                    </div>
                </div>

            </div>
        </div>

        <footer>
            <p>&copy; 2026 NEXT TECH ACADEMY. All rights reserved.</p>
        </footer>

    </body>
    </html>
    """