from ai_server_core import generate_product_description

# 테스트용 main

def main():
    product = {
        "name": "Angel Star Patch 자수 원턱 스트링 와이드 스웨트 팬츠 AP903 (블랙)",
        "price": 30320,
        "options": "색상: 화이트/블랙/멜란지그레이, 사이즈: M/L/XL",
        "category_path": "바지 > 트레이닝/조거 팬츠(엠블러)",
        "image_url": "https://image.msscdn.net/thumbnails/images/goods_img/20250819/5338392/5338392_17564331759079_big.jpg?w=1200",
    }

    text = generate_product_description(product)
    print("===== 생성된 상품 상세 설명 =====")
    print(text)
    print("================================")

if __name__ == "__main__":
    main()
    
# 실행 시 python main.py
