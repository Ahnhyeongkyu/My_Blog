# 🔖My Blog
My_Blog은 Flask 웹 애플리케이션을 활용하여 구축된 개인 블로그 플랫폼입니다.

https://ans-tech-blog.onrender.com/

## 1. 개발 목적

Flask 웹 프레임워크를 활용하여 가벼우면서도 다양한 기능을 갖춘 블로그 서비스 구현이 목표입니다. 사용자는 손쉽게 블로그를 운영하고 다양한 글을 작성할 수 있습니다.

## 2. 사용기술

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


## 3. 핵심 기능

"My Blog"의 핵심 기능은 먼저, 간편한 회원가입과 로그인을 통해 블로그에 접근 할 수 있습니다.

사용자는 직관적이고 편리한 CKEditor를 활용하여 블로그에 글을 작성하며, 다른 사용자와 소통할 수 있는 댓글 기능이 제공됩니다. 

또한, 글이 많아져도 효과적인 글 탐색을 위해 페이지네이션을 지원하여 사용자 경험을 향상시켰습니다.

<details>
  <summary>핵심 기능 설명 펼치기</summary>
  
  ### 3-1. 사용자 회원가입 및 로그인

- 회원가입: 🔖[코드확인](https://github.com/Ahnhyeongkyu/My_Blog/blob/main/main.py#L99)

  - 사용자는 웹 애플리케이션에 접속하여 이메일, 비밀번호, 사용자명 등의 정보를 입력하여 회원가입을 진행합니다.
  - 입력한 정보는 서버에서 유효성 검사를 거치고, 유효한 경우 데이터베이스에 저장됩니다.
  - 비밀번호는 해시 함수를 사용하여 안전하게 저장됩니다.

- 로그인: 🔖[코드확인](https://github.com/Ahnhyeongkyu/My_Blog/blob/main/main.py#L130)

  -  회원가입한 사용자는 이메일과 비밀번호를 입력하여 로그인할 수 있습니다.
  -  서버는 입력받은 이메일과 비밀번호를 검증하고, 일치하는 경우 로그인 세션을 생성합니다.
  -  로그인 상태를 유지하기 위해 Flask-Login을 사용하여 세션 관리를 합니다.

  ### 3-2. 게시물 작성, 수정, 삭제 기능

- 게시물 작성: 🔖[코드확인](https://github.com/Ahnhyeongkyu/My_Blog/blob/main/main.py#L197)

  - 관리자는 웹 페이지에서 새로운 글을 작성할 수 있습니다.
  - 제목, 소제목, 내용 등을 작성하고 "글 작성" 버튼을 클릭하면 해당 글이 데이터베이스에 저장됩니다.

- 게시물 수정: 🔖[코드확인](https://github.com/Ahnhyeongkyu/My_Blog/blob/main/main.py#L217)

  - 관리자는 작성된 글을 수정할 수 있습니다.
  - 글 수정 페이지에서 기존 내용을 수정하고 "수정 완료" 버튼을 클릭하면 데이터베이스가 업데이트됩니다.

- 게시물 삭제: 🔖[코드확인](https://github.com/Ahnhyeongkyu/My_Blog/blob/main/main.py#L238)

  - 관리자는 작성된 글을 삭제할 수 있습니다.
  - 삭제 버튼 클릭 시 해당 글 및 관련된 댓글들이 데이터베이스에서 삭제됩니다.

  ### 3-3. 댓글 작성 및 삭제 기능

- 댓글 작성: 🔖[코드확인](https://github.com/Ahnhyeongkyu/My_Blog/blob/main/main.py#L160)

  - 글을 읽는 사용자는 해당 글 하단에서 댓글을 작성할 수 있습니다.
  - 댓글 작성란에 텍스트를 입력하고 "댓글 작성" 버튼을 클릭하면 댓글이 데이터베이스에 저장됩니다.

- 댓글 삭제: 🔖[코드확인](https://github.com/Ahnhyeongkyu/My_Blog/blob/main/main.py#L249)

  - 관리자는 작성된 댓글을 삭제할 수 있습니다.
  - 삭제 버튼 클릭 시 해당 댓글이 데이터베이스에서 삭제됩니다.

  ### 3-4. 관리자 권한 기능

- 관리자 권한 부여: 🔖[코드확인](https://github.com/Ahnhyeongkyu/My_Blog/blob/main/main.py#L66)

  - 웹 애플리케이션은 관리자 권한을 가진 특정 사용자에게 추가 기능 및 권한을 부여합니다.
  - 예를 들어, 글 삭제, 사용자 관리 등의 작업은 관리자만 가능합니다.
  - 이러한 핵심 기능들을 통해 사용자는 쉽고 편리하게 블로그를 운영하고, 다른 사용자들과 소통할 수 있는 풍부한 경험을 얻을 수 있습니다.
</details>

## 4. 핵심 트러블 슈팅

### 4-1 페이지네이션 구현

- 내용:
  - 게시물이 많아질 경우 과거에 게시한 게시물을 찾기 위해서는 스크롤을 많이 내려야 되는 현상이 발생하여 사용자 편의를 해치게 됩니다.

- 해결책:
  - SQLAlchemy의 paginate 메서드를 사용하여 페이지네이션을 구현하였습니다. 또한 Jinja2 템플릿 엔진을 사용하여 페이지네이션 버튼을 동적으로 생성하여 사용자 편의성을 높였습니다.

- 🔖[코드확인](https://github.com/Ahnhyeongkyu/My_Blog/blob/main/main.py#L85)

### 4-2 댓글 삭제 시 외래 키 제약 조건

- 내용:
  - 게시물 삭제 시 해당 게시물과 관련된 댓글도 함께 삭제해야 했으나 외래 키 제약 조건으로 인해 발생한 문제가 있었습니다.

- 해결책:
  - SQLAlchemy에서 cascade 속성을 사용하여 외래 키 제약 조건을 해결하였습니다. 댓글을 삭제할 때 해당 게시물의 외래 키 조건도 함께 삭제되도록 설정하였습니다.

- 🔖[코드확인](https://github.com/Ahnhyeongkyu/My_Blog/blob/main/main.py#L53)


## 5. 그 외 트러블 슈팅

- 환경 변수 로드 오류

  - 내용:
    - env 파일에서 환경 변수를 로드하는 과정에서 오류가 발생했습니다.

  - 해결책:
    - python-dotenv 라이브러리를 사용하여 .env 파일에서 환경 변수를 로드하도록 구현했습니다.

- SQLAlchemy 연결 문제

  - 내용:
    -  SQLAlchemy를 사용하여 데이터베이스에 연결하는 과정에서 연결 오류가 발생했습니다.

  - 해결책:
    - 데이터베이스 URI를 .env 파일에서 동적으로 읽어오도록 설정했습니다.
   
- 배포 후 서버 슬립 문제

  - 내용:
    - render.com에 프로젝트 배포 후 일정시간 서버를 사용하지 않으면 서버가 '슬립모드'에 들어가는 문제가 있습니다.

  - 해결책:
    - 현재 사용하고 있는 Free 요금이 아니라 유료 요금제를 사용하거나, AWS 학습을 통해 클라우드 환경에서의 서버 운영 및 관리 능력을 키우고, render.com에서 발생하는 특정 문제를 피할 수 있습니다.

## 6. 회고/느낀점

프로젝트 개발 회고 글: https://ans-tech-blog.onrender.com/post/16


       
