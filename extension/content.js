// This script runs on every page to collect content
// It can be used to highlight potential deepfake content or collect data

// Function to get selected text from the page
function getSelectedText() {
  return window.getSelection().toString();
}

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getSelectedText") {
    const selectedText = getSelectedText();
    sendResponse({ text: selectedText });
  }
  return true;
});
