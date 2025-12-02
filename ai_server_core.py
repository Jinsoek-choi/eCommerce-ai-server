# OpenAI API 호출을 위한 라이브러리
from openai import OpenAI

# .env 파일에서 환경변수를 자동으로 불러오기 위한 라이브러리
from dotenv import load_dotenv

# 환경변수 접근을 위한 os 라이브러리
import os

# .env 파일 내용 로드 (OPENAI_API_KEY 사용 가능해짐)
load_dotenv()

# OpenAI 클라이언트 생성
# api_key=os.getenv("OPENAI_API_KEY")
# → OS 환경변수 또는 .env에서 OPENAI_API_KEY를 읽어서 사용
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------------------------------------
# 상품 정보를 받아서 OpenAI에게 "상품 상세 설명"을 생성 요청하는 함수
# FastAPI 서버(server.py)나 테스트 코드(main.py)에서 이 함수를 호출함
# -----------------------------------------------------------
def generate_product_description(product: dict) -> str:
    # OpenAI에 전달할 프롬프트(지시문)
    # 모델이 어떤 스타일로 글을 쓸지, 어떤 정보를 참고할지 설명함
    prompt = f"""
너는 남녀 공용 캐주얼 의류 쇼핑몰의 상품 상세 페이지를 작성하는 카피라이터야.
아래 정보를 참고해서 한국어로 300~500자 정도의 상세 설명을 써줘.

[상품 정보]
- 상품명: {product["name"]}
- 가격: {product["price"]}원
- 옵션: {product["options"]}
- 카테고리: {product["category_path"]}
(이미지도 함께 참고해서 실루엣, 디테일, 분위기를 잘 설명해줘.)
"""

    # OpenAI GPT 모델 호출
    # messages → 프롬프트와 이미지 URL을 전달
    resp = client.chat.completions.create(
        model="gpt-4.1-mini",  # 이미지 인식 가능한 최신 경량 모델
        messages=[
            {
                "role": "user",
                "content": [
                    # 텍스트 지시문(prompt)
                    {"type": "text", "text": prompt},
                    
                     # 이미지 URL 전달 (모델이 실제 이미지를 보고 설명 가능)
                    {
                        "type": "image_url",
                        "image_url": {"url": product["image_url"]},
                    },
                ],
            }
        ],
    )

    # OpenAI 응답에서 생성된 텍스트만 추출하여 반환
    return resp.choices[0].message.content
