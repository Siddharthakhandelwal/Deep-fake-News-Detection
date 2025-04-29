// This script runs on every page to collect content
// It can be used to highlight potential deepfake content or collect data

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getContent") {
    const content = {
      title: document.title,
      text: document.body.innerText,
      images: Array.from(document.getElementsByTagName("img")).map(
        (img) => img.src
      ),
    };
    sendResponse(content);
  }
  return true;
});
