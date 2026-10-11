'use strict';
for (const button of document.querySelectorAll('[data-copy]')) {
  button.addEventListener('click', async () => {
    const status = document.getElementById('copy-status');
    const source = document.getElementById(button.dataset.copy);
    try {
      await navigator.clipboard.writeText(source.textContent);
      status.textContent = 'Copied. Paste it into your terminal or agent session.';
    } catch {
      status.textContent = 'Clipboard unavailable. Select and copy the text above manually.';
    }
  });
}
