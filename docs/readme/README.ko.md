# Cookbook by Pengusto

프로젝트: **Cookbook by Pengusto** · GitHub 저장소: [`pengusto/cookbook`](https://github.com/pengusto/cookbook).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme/cookbook-banner-storybook-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="../../assets/readme/cookbook-banner-storybook-v3.png">
  <img alt="AI 생성 일러스트: 펼친 요리책에서 솟아난 크림색과 와인색 주방에서 워크플로 카드 옆에서 요리하는 Cookbook 펭귄." src="../../assets/readme/cookbook-banner-storybook-v3.png">
</picture>

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

**코딩 대화의 다음 단계를 위한 레시피.**

Cookbook은 Codex 또는 Claude Code를 사용하는 개발자에게 19개의 집중된 워크플로를 제공합니다. 프로젝트 계획, 진행 상황 점검, 휴식 후 맥락 복구, 공유 전 검토, 유용한 인계 정리에 활용하세요. 필요할 때 레시피를 선택하면 호스트와 모델이 작업을 수행합니다.

**쉬운 질문** 또는 **요리 이름**을 선택하세요. 두 스타일은 같은 관리 지침에서 생성되며, 호스트마다 하나의 이름 체계를 설치합니다.

**실험적 공개 베타 · 0.7.2.** [레시피 둘러보기](https://pengusto.github.io/cookbook/cookbook.html) · [Plain](https://pengusto.github.io/cookbook/cookbook-plain.html)

## 빠른 시작: 이름 체계 선택

먼저 Codex 및/또는 Claude Code를 설치하고 로그인하세요. 예제는 Kitchen을 설치합니다. Codex에서 Plain을 사용하려면 `--ref plain`을 지정하세요. 두 스타일은 플러그인 ID를 공유하므로 한 번에 하나만 설치합니다. 패키지 빌드는 기존 호스트 설치를 변경하지 않습니다.

Codex — 로컬 빌드 불필요:

```sh
codex plugin marketplace add pengusto/cookbook --ref kitchen
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

설치 후 새 Codex 세션을 열고 다음을 입력하세요:

```text
$show-me-the-kitchen Cookbook을 설명하고 오랜 휴식 후 프로젝트에 복귀할 때 사용할 워크플로를 추천해 주세요.
```

가이드는 설명하고 추천하며 추천한 워크플로를 실행하지 않습니다. Plain은 설치 시 `--ref plain`, 대화에서는 `$explain-the-cookbook`을 사용하세요.

Claude Code — 먼저 아래의 빌드 및 검증 명령을 실행하세요:

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

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 38 individual ZIPs + `SHA256SUMS`.

## 빌드 및 검증

Git과 Python 3.10+가 필요하며 추가 Python 패키지는 필요하지 않습니다. Codex 또는 Claude Code는 별도로 설치하고 로그인하세요. 저장소 루트에서 명령을 실행합니다.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## 레시피 메뉴

| Plain | Kitchen |
|---|---|
| Explain the Cookbook | Show Me the Kitchen |
| Find Our Work | Find the Recipe |
| Where Does This Chat Belong? | Find the Kitchen |
| Catch Me Up | Back to the Kitchen |
| Where Were We? | What Was I Cooking? |
| How Do I Start? | Prep the Kitchen |
| Finish My Prompt | Finish My Order |
| Which Name Wins? | Name That Dish |
| You Got This | You’re the Chef |
| Am I Making Progress? | Are We Cooking? |
| Why Is It Broken? | Find the Bad Ingredient |
| Can We Simplify? | Trim the Recipe |
| Review My Changes | Taste Before Serving |
| Did I Leak? | Keep the Recipe Secret |
| Will They Sue Me? | Can I Serve This? |
| Am I Ready to Share? | Ready to Serve |
| What Did We Change? | What’s New on the Menu? |
| Can We Finish? | Close the Kitchen |
| Here We Go Again | Why Did It Burn? |

추가 모드: `$prep-the-kitchen explain <flow>`는 기존 코드를 설명하고 `$prep-the-kitchen choose <decision>`은 대안을 비교합니다. `$ready-to-serve verify-live <target>`은 실제 배포를 확인하고 `$close-the-kitchen handoff <destination>`은 인계를 준비합니다. Plain은 같은 인수로 `$how-do-i-start`, `$am-i-ready-to-share`, `$can-we-finish`를 사용합니다. 이 요청만으로 변경이 허용되지 않으며 인계 준비가 전송 완료를 뜻하지 않습니다.

상황에 맞는 [선택 안내](../choosing-workflow.md). 현재 오류에는 `$find-the-bad-ingredient`(Kitchen) 또는 `$why-is-it-broken`(Plain)을 사용합니다. 실제 사용 흐름은 `$youre-the-chef usertest <flow>` 또는 `$you-got-this usertest <flow>`로 확인합니다. 자동 수정 없이 결과를 보고하며 실제 참가자 대상 연구가 아닙니다.

## 업데이트

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

업데이트 전에 변경 사항을 커밋하거나 별도로 백업하세요. 다시 빌드하면 로컬 패키지만 갱신되며 설치된 캐시는 갱신되지 않습니다. 패키지를 백업한 후 기본 제거/재설치 명령을 사용하세요. Mac 안내를 참고하세요. [Mac setup](../../docs/mac-setup.md).

## 웹사이트

독일어/영어 페이지는 시스템의 라이트/다크 설정을 따릅니다. 언어와 이름 체계는 각각 바꿀 수 있지만 스킬 지침은 번역되지 않습니다. 로컬 미리보기를 시작하고 출력된 URL을 여세요. 공개 Beta 웹사이트는 GitHub Pages에서 제공됩니다. 스토어 심사는 별도입니다.

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](../../docs/landing-page.md).

## 제한 및 상태

패키지, 해시, 링크 및 이식 가능한 재빌드 검사는 자동화되어 있습니다. 관리자는 0.4.0에서 열두 스킬의 Desktop 선택기와 종료 가이드를 확인했습니다. 0.5.0의 새 소개 가이드는 새 네이티브 Codex 호출로 별도 테스트되었습니다. 이는 해당 버전의 검사 기록이며 0.6.0 전체의 시각적 승인이나 스토어 승인이 아닙니다. 시각적 Cookbook은 12개 UI 언어와 시스템/밝은/어두운 테마를 제공합니다. UI 언어는 워크플로 지침을 번역하지 않습니다. 선택적인 로컬 MCP 사이드바는 별도 패키지입니다.

보안 및 법률 검토 레시피는 검사를 안내하지만 보장하지 않습니다. 저장소 및 웹사이트 공개는 스토어 제출과 별개입니다. 승인된 과거 연락처 페이지를 포함한 가져온 Git 기록과 출처는 보존됩니다. 대체된 네 개의 GitHub 저장소는 관리자의 승인으로 삭제되었습니다. [0.5.0 acceptance](../../docs/acceptance-0.5.0.md) · [Release review](../../docs/public-release-review.md).

## 기여 및 라이선스

issue 또는 범위가 명확한 pull request를 보내주세요. 공통 스킬 소스만 수정하고 여덟 README를 함께 유지하세요. 자체 코드와 스킬은 MIT이며 외부 아이콘은 MIT/ISC 고지를 유지합니다. 일러스트는 AI로 생성했습니다.

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).

기존 Cookbook 로고 사용: Cormorant Garamond 글꼴 윤곽은 SIL OFL을 따릅니다. 레시피 그림은 AI로 생성되었으며 스크린샷이나 호스트 승인 증거가 아닙니다. [에셋 출처 및 라이선스](../../THIRD_PARTY_NOTICES.md) · [로고 안내](../../assets/brand/GUIDE.md).

## 개발 지원

Cookbook이 유용하다면 [제 오픈 소스 활동을 후원](https://github.com/sponsors/pengusto)하실 수 있습니다.
