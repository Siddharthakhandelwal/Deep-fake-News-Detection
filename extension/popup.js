document.addEventListener("DOMContentLoaded", function () {
  const analyzeBtn = document.getElementById("analyzeBtn");
  const newsText = document.getElementById("newsText");
  const resultDiv = document.getElementById("result");
  const loadingDiv = document.getElementById("loading");
  const predictionSpan = document.getElementById("prediction");
  const confidenceSpan = document.getElementById("confidence");

  // API URL - Update this with your Render URL after deployment
  const API_URL = "https://deepfake-news-detector.onrender.com/analyze";

  analyzeBtn.addEventListener("click", async function () {
    const text = newsText.value.trim();
    if (!text) {
      alert("Please enter some text to analyze");
      return;
    }

    // Show loading
    loadingDiv.style.display = "block";
    resultDiv.style.display = "none";

    try {
      // Make API call to your backend
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: text }),
      });

      const data = await response.json();

      if (data.status === "success") {
        // Update UI with results
        predictionSpan.textContent = data.prediction;
        confidenceSpan.textContent = `${(data.confidence * 100).toFixed(2)}%`;

        // Set result box class based on prediction
        resultDiv.className = `result ${data.prediction.toLowerCase()}`;
        resultDiv.style.display = "block";
      } else {
        alert("Error: " + data.message);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Error analyzing the text. Please try again.");
    } finally {
      loadingDiv.style.display = "none";
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
