document.addEventListener("DOMContentLoaded", function () {
  const analyzeBtn = document.getElementById("analyzeBtn");
  const resultDiv = document.getElementById("result");
  const loadingDiv = document.getElementById("loading");
  const resultTitle = document.getElementById("resultTitle");
  const resultMessage = document.getElementById("resultMessage");
  const confidenceLevel = document.getElementById("confidenceLevel");

  analyzeBtn.addEventListener("click", async () => {
    try {
      // Show loading state
      analyzeBtn.disabled = true;
      loadingDiv.classList.add("show");
      resultDiv.classList.remove("show");

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

      // Hide loading state
      loadingDiv.classList.remove("show");
      analyzeBtn.disabled = false;

      // Display results
      resultDiv.classList.add("show");
      if (data.is_deepfake) {
        resultDiv.className = "result-container show danger";
        resultTitle.textContent = "⚠️ Potential DeepFake Detected";
        resultMessage.textContent = "This content might be manipulated";
        confidenceLevel.style.width = `${data.confidence * 100}%`;
        confidenceLevel.style.backgroundColor = "var(--danger-color)";
      } else {
        resultDiv.className = "result-container show safe";
        resultTitle.textContent = "✅ Content Authentic";
        resultMessage.textContent = "No signs of manipulation detected";
        confidenceLevel.style.width = `${(1 - data.confidence) * 100}%`;
        confidenceLevel.style.backgroundColor = "var(--safe-color)";
      }
    } catch (error) {
      // Hide loading state
      loadingDiv.classList.remove("show");
      analyzeBtn.disabled = false;

      // Show error
      resultDiv.className = "result-container show warning";
      resultTitle.textContent = "❌ Error";
      resultMessage.textContent =
        "Failed to analyze content. Please try again.";
      confidenceLevel.style.width = "0%";
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
