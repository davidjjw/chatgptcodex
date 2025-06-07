# 다층 노트 앱 프로젝트 기획

이 문서는 Flask 기반 다층 구조 노트 앱 개발을 위한 기본 계획을 정리합니다.

## 1. 목표
- 사용자별 노트북, 섹션, 노트를 생성하고 관리할 수 있는 웹 애플리케이션 구축
- 섹션의 부모-자식 관계를 이용하여 원하는 깊이의 트리 구조 지원
- Tailwind CSS 를 활용해 간결하면서도 일관된 UI 제공

## 2. 주요 기술 스택
- **백엔드**: Python, Flask, SQLAlchemy
- **데이터베이스**: 초기에는 SQLite, 이후 확장 시 PostgreSQL 고려
- **프론트엔드**: Jinja2 템플릿, Tailwind CSS, 필요 시 JavaScript(Ajax)

## 3. 데이터 모델
1. **User**
   - id, username, password, email 등 기본 로그인 정보
2. **Notebook**
   - id, user_id(FK), title, created_at, updated_at
3. **Section**
   - id, notebook_id(FK), parent_id(동일 테이블 참조), title,
     created_at, updated_at
4. **Note**
   - id, section_id(FK), title, body, created_at, updated_at

## 4. 개발 단계
1. **프로젝트 세팅**
   - 가상환경 생성 및 Flask, SQLAlchemy 등 필수 패키지 설치
   - 기본 앱 구조와 설정 파일 준비
2. **사용자 인증 기능**
   - 회원가입, 로그인, 로그아웃 뷰 구현
   - 비밀번호 해시 처리와 세션 관리
3. **노트북 CRUD**
   - 노트북 생성, 수정, 삭제, 목록 조회
   - 사용자별 권한 확인
4. **섹션(폴더) 계층 구조 구현**
   - parent_id 를 이용해 섹션 트리 구성
   - 섹션 추가, 이동, 삭제 기능
5. **노트 CRUD**
   - 노트 작성, 편집, 삭제, 조회
   - 섹션 트리에서 노트 위치 관리
6. **UI 개선 및 추가 기능**
   - Tailwind CSS를 적용하여 레이아웃 정리
   - 태그, 검색, 버전 관리 등의 부가기능 구현 검토

## 5. 향후 과제
- RESTful API 또는 GraphQL API 제공 여부 결정
- 테스트 코드 작성 및 배포 환경 구성

본 계획을 기반으로 단계별로 기능을 완성하면서 점진적으로 애플리케이션을 발전시킬 수 있습니다.

## 진행 상황
- 사용자 인증 기능 구현 완료
- 노트북 CRUD 기능 기본 구현
- 섹션 계층 구조 기본 구현
- 노트 CRUD 기본 구현
