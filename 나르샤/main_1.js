// 안정화된 toggle 코드: 강제 리플로우 + 리스너 등록 타이밍 개선
const toggleBtn = document.getElementById("toggleBtn");
const searchBox = document.getElementById("searchBox");
const up_arrow = document.getElementById("arrow");

if (!toggleBtn || !searchBox) {
  console.warn("toggleBtn 또는 searchBox를 찾을 수 없습니다.");
} else {
  const ANIM_DURATION = 600; // ms
  const EASING = "0, 0.55, 0.45, 1";
  const TRANS = `max-height ${ANIM_DURATION}ms ${EASING}, padding ${ANIM_DURATION}ms ${EASING}`;

  // CSS에서 collapsed로 정의한 값과 같게 맞추세요
  const COLLAPSED_HEIGHT = "50px";

  toggleBtn.addEventListener("click", () => {
    const isExpanded = searchBox.classList.contains("expanded");

    if (isExpanded) {
      // === 닫기 흐름 ===
      // 1) 시작 높이 고정
      const curH = searchBox.scrollHeight;
      searchBox.style.maxHeight = curH + "px";

      // 2) (중요) 강제 리플로우 — 브라우저가 시작 상태를 확정하도록 함
      //    그냥 읽기만 해도 리플로우 발생
      void searchBox.offsetHeight;

      // 3) transitionend 리스너 미리 등록 (놓치는 것 방지)
      const onCloseEnd = (e) => {
        if (e.propertyName === "max-height") {
          searchBox.classList.remove("expanded");
          searchBox.style.transition = "";
          searchBox.style.maxHeight = ""; // CSS의 collapsed 규칙으로 돌아감
          searchBox.removeEventListener("transitionend", onCloseEnd);
        }
      };
      searchBox.addEventListener("transitionend", onCloseEnd);

      // 4) 다음 프레임에서 transition 설정하고 목표 높이로 변경 -> 애니메이션 시작
      requestAnimationFrame(() => {
        searchBox.style.transition = TRANS;
        searchBox.style.maxHeight = COLLAPSED_HEIGHT;
      });

      toggleBtn.toggleAttribute("data-rotated");
    } else {
      // === 열기 흐름 ===
      searchBox.classList.add("expanded");

      // 1) full height 측정 (클래스 추가 후)
      const fullH = searchBox.scrollHeight;

      // 2) 강제 리플로우: collapsed 상태로 세팅 후 퍼포먼스 안정화
      searchBox.style.maxHeight = COLLAPSED_HEIGHT;
      void searchBox.offsetHeight;

      // 3) transitionend 리스너 등록
      const onOpenEnd = (e) => {
        if (e.propertyName === "max-height") {
          searchBox.style.transition = "";
          searchBox.style.maxHeight = "none"; // 내용 가변 허용
          searchBox.removeEventListener("transitionend", onOpenEnd);
        }
      };
      searchBox.addEventListener("transitionend", onOpenEnd);

      // 4) 애니메이션 트리거
      requestAnimationFrame(() => {
        searchBox.style.transition = TRANS;
        searchBox.style.maxHeight = fullH + "px";
      });

      toggleBtn.toggleAttribute("data-rotated");
    }
  });
}
