document.addEventListener("DOMContentLoaded", function () {
  const analyzeBtn = document.getElementById("analyzeBtn");
  const resultDiv = document.getElementById("result");

  analyzeBtn.addEventListener("click", async () => {
    try {
      // Get the current active tab
      const [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true,
      });

      // Execute content script to get page content
      const results = await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        function: getPageContent,
      });

      const pageContent = results[0].result;

      // Send content to backend for analysis
      const response = await fetch("http://localhost:5000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          url: tab.url,
          content: pageContent,
        }),
      });

      const data = await response.json();

      // Display results
      if (data.is_deepfake) {
        resultDiv.className = "danger";
        resultDiv.textContent = "⚠️ Warning: This content might be manipulated";
      } else {
        resultDiv.className = "safe";
        resultDiv.textContent = "✅ Content appears to be authentic";
      }
    } catch (error) {
      resultDiv.className = "warning";
      resultDiv.textContent = "❌ Error analyzing content. Please try again.";
      console.error("Error:", error);
    }
  });
});

// Function to get page content
function getPageContent() {
  return {
    title: document.title,
    text: document.body.innerText,
    images: Array.from(document.getElementsByTagName("img")).map(
      (img) => img.src
    ),
  };
}
