# Python으로 REST API 서버 만들 때 가장 많이 사용
from fastapi import FastAPI

# 들어오는 JSON 데이터의 구조를 검증하고 타입을 맞춰주는 클래스
from pydantic import BaseModel

# OpenAI 호출 함수
# FastAPI는 단순히 이 함수를 HTTP API로 감싸주는 역할
from ai_server_core import generate_product_description

# Flask의 app = Flask(__name__) 같은 역할
# API 서버의 시작점
app = FastAPI()

# 클라이언트(예: Spring, Frontend)가 보내야 하는 JSON의 형식을 정의
# FastAPI는 JSON을 받아서 자동으로 이 클래스로 변환해줌
class ProductIn(BaseModel):
    name: str
    price: int | None = None  # | None 이 붙은 건 옵션값(없어도 되는 값)
    options: str | None = None
    category_path: str | None = None
    image_url: str | None = None

# API Response Body 정의
# API가 반환하는 JSON 형식을 정의
class DescriptionOut(BaseModel):
    description: str
    # 실제 반환 데이터는 이렇게 내려옴:
    # {
    #   "description": "여기 OpenAI가 생성한 설명..."
    # }

# API 엔드포인트 생성
    # POST /ai/description URL에 요청이 오면 이 함수 실행됨
    # body: ProductIn 덕분에 JSON이 자동으로 ProductIn 객체로 변환됨.
    # response_model=DescriptionOut
    # → FastAPI가 응답을 자동으로 이 구조에 맞게 바꿔서 반환함
@app.post("/ai/description", response_model=DescriptionOut)
async def ai_description(body: ProductIn):
    text = generate_product_description(body.model_dump())
    # JSON 형태로 응답 돌려주기
    # FastAPI가 자동으로 JSON 변환
    return DescriptionOut(description=text)
