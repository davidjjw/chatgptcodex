# chatgptcodex

이 저장소는 Flask 기반 노트 애플리케이션을 단계적으로 개발하기 위한 예제입니다. `docs/PROJECT_PLAN.md` 문서에서 전반적인 구조와 개발 로드맵을 확인할 수 있습니다.

## 실행 방법
1. 의존성 설치
   ```bash
   python -m pip install -r requirements.txt
   ```
2. 개발 서버 실행
   ```bash
   python run.py
   ```

첫 실행 시 `app.db` 파일이 생성되며 `/auth/register` 페이지에서
새 계정을 만들어 로그인할 수 있습니다.

로그인 후 `/notebooks` 페이지에서 노트북을 추가하고 관리할 수 있습니다.
각 노트북의 `/sections` 페이지에서 하위 섹션을 생성하고 편집할 수 있습니다.
