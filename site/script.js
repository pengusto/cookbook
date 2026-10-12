const copyButton = document.querySelector('#copy');
if (copyButton) {
  copyButton.addEventListener('click', async () => {
    const status = document.querySelector('#copy-status');
    try {
      await navigator.clipboard.writeText(document.querySelector('#prompt').textContent);
      status.textContent = 'Copied. Edit the market and business model to match your app.';
    } catch {
      status.textContent = 'Copy is unavailable here. Select and copy the prompt above.';
    }
  });
}
