# 🔖My Blog
My_Blog"은 Flask 웹 애플리케이션을 활용하여 구축된 개인 블로그 플랫폼입니다.

https://ans-tech-blog.onrender.com/

## 1. 개발 목적

백엔드 개발자 학습 과정에서 습득한 지식과 각종 정보들 및 진행한 프로젝트들에서 배운점들을 일목요연하게 정리하여

지속적으로 학습하고 성장하기 위해서 시중에서 서비스 되는 블로그가 아닌 나만의 블로그를 개발하게 되었습니다.



## 2. 제작기간 & 참여인원

- 제작기간: 2023년 12월 ~ 2024년 1월
- 참여인원: 1인 (개인 프로젝트)



## 3. 사용기술

**Back-end**
- Python
- Flask
- flask ckeditor
- werkzeug security
- flask sqlalchemy
- flask login
- functools
- dotenv
- flask bootstrap

**Front-end**
- HTML
- CSS
- Bootstrap


## 4. 핵심 기능

"My Blog"의 핵심 기능은 먼저, 간편한 회원가입과 로그인을 통해 블로그에 접근 할 수 있습니다.

사용자는 직관적이고 편리한 CKEditor를 활용하여 블로그에 글을 작성하며, 다른 사용자와 소통할 수 있는 댓글 기능이 제공됩니다. 

또한, 글이 많아져도 효과적인 글 탐색을 위해 페이지네이션을 지원하여 사용자 경험을 향상시켰습니다.

<details>
  <summary>핵심 기능 설명 펼치기</summary>
  
  ### 4-1. 사용자 회원가입 및 로그인

  #### 회원가입: 🔖[코드확인](https://github.com/Ahnhyeongkyu/My_Blog/blob/main/main.py#L99)

- 사용자는 웹 애플리케이션에 접속하여 이메일, 비밀번호, 사용자명 등의 정보를 입력하여 회원가입을 진행합니다.
- 입력한 정보는 서버에서 유효성 검사를 거치고, 유효한 경우 데이터베이스에 저장됩니다.
- 비밀번호는 해시 함수를 사용하여 안전하게 저장됩니다.
</details>
