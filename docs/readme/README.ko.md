# Cookbook by Pengusto

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

하나의 공통 소스에서 관리하는 일곱 가지 에이전트 워크플로입니다. **쉬운 질문** 또는 **요리 이름**을 선택하고 호스트마다 한 가지 이름 체계만 설치하세요.

**실험적 공개 Beta.** [pengusto/cookbook](https://github.com/pengusto/cookbook)

| Plain | Kitchen |
|---|---|
| How Do I Start? | Prep the Kitchen |
| Am I Making Progress? | Are We Cooking? |
| Did I Leak? | Keep the Recipe Secret |
| Will They Sue Me? | Can I Serve This? |
| Am I Ready to Share? | Ready to Serve |
| What Did We Change? | What’s New on the Menu? |
| Can We Finish? | Close the Kitchen |

## 빌드 및 검증

Git과 Python 3.10+가 필요하며 추가 Python 패키지는 필요하지 않습니다. Codex 또는 Claude Code는 별도로 설치하고 로그인하세요. 저장소 루트에서 명령을 실행합니다.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## 이름 체계 하나 설치

plain 또는 kitchen을 선택하세요. 두 방식은 같은 플러그인 식별자를 사용합니다. 예시는 Kitchen을 설치합니다. 설치 후 새 세션을 시작하세요. 빌드는 기존 설치를 변경하지 않습니다.

Codex:

```sh
codex plugin marketplace add ./dist/kitchen/codex
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Claude Code:

```sh
claude plugin marketplace add ./dist/kitchen/claude --scope user
claude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user
```

이름 체계를 바꾸기 전에 설치된 패키지를 백업하고 호스트의 기본 명령으로 Cookbook 플러그인만 제거한 뒤 해당 marketplace 등록을 해제하고 다른 체계를 등록하세요. 개별 복사본이나 기존 vibe-coding-cookbook을 함께 설치하지 마세요.

스킬 개별 설치도 지원합니다. 대상 위치에 같은 워크플로가 없어야 합니다. 예시는 close-the-kitchen을 만들며 plain은 can-we-finish를 만듭니다.

```sh
python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /empty/local/skills
```

Codex: `$close-the-kitchen` · Claude Code: `/cookbook-by-pengusto:close-the-kitchen`

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 14 individual ZIPs + `SHA256SUMS`.

## 업데이트

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

업데이트 전에 변경 사항을 커밋하거나 별도로 백업하세요. 다시 빌드하면 로컬 패키지만 갱신되며 설치된 캐시는 갱신되지 않습니다. 패키지를 백업한 후 기본 제거/재설치 명령을 사용하세요. Mac 안내를 참고하세요. [Mac setup](../../docs/mac-setup.md).

## 웹사이트

독일어/영어 페이지는 시스템의 라이트/다크 설정을 따릅니다. 언어와 이름 체계는 각각 바꿀 수 있지만 스킬 지침은 번역되지 않습니다. 로컬 미리보기를 시작하고 출력된 URL을 여세요. 이 Beta에는 공개 웹사이트 배포나 스토어 등록이 포함되지 않습니다.

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](../../docs/landing-page.md).

## 제한 및 상태

패키지, 해시, 링크 및 이동 가능한 재빌드를 자동으로 확인합니다. 스킬 로딩은 로컬에서 테스트했지만 전체 데스크톱 시각적 인수 확인과 스토어 승인은 아직 남아 있습니다. 보안 및 법률 검토 스킬은 지침이며 보증이 아닙니다. 보존된 기록에는 관리자가 공개를 승인한 과거 연락처 페이지가 포함됩니다. 원래 저장소는 보관됩니다. [Release review](../../docs/public-release-review.md).

## 기여 및 라이선스

issue 또는 범위가 명확한 pull request를 보내주세요. 공통 스킬 소스만 수정하고 여덟 README를 함께 유지하세요. 자체 코드와 스킬은 MIT이며 외부 아이콘은 MIT/ISC 고지를 유지합니다. 일러스트는 AI로 생성했습니다.

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).
