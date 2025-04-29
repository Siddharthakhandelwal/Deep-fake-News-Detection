document.addEventListener("DOMContentLoaded", function () {
  const analyzeBtn = document.getElementById("analyzeBtn");
  const newsText = document.getElementById("newsText");
  const resultDiv = document.getElementById("result");
  const loadingDiv = document.getElementById("loading");
  const predictionSpan = document.getElementById("prediction");
  const confidenceSpan = document.getElementById("confidence");
  const errorDiv = document.getElementById("error");
  const errorMessage = document.getElementById("errorMessage");

  // API URL - Update this with your Render URL after deployment
  const API_URL = "http://localhost:5000/analyze"; // Change this to your Render URL after deployment

  // Add loading spinner style
  const style = document.createElement("style");
  style.textContent = `
      .spinner {
          border: 4px solid rgba(0, 0, 0, 0.1);
          border-radius: 50%;
          border-top: 4px solid #4CAF50;
          width: 30px;
          height: 30px;
          animation: spin 1s linear infinite;
          margin: 0 auto;
      }
      @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
      }
  `;
  document.head.appendChild(style);

  function showError(message) {
    errorMessage.textContent = message;
    errorDiv.style.display = "block";
    resultDiv.style.display = "none";
    loadingDiv.style.display = "none";
  }

  function hideError() {
    errorDiv.style.display = "none";
  }

  function showLoading() {
    loadingDiv.style.display = "block";
    resultDiv.style.display = "none";
    hideError();
  }

  function showResult(prediction, confidence) {
    loadingDiv.style.display = "none";
    resultDiv.style.display = "block";
    hideError();

    predictionSpan.textContent = prediction;
    confidenceSpan.textContent = `${(confidence * 100).toFixed(2)}%`;

    if (prediction === "Fake") {
      resultDiv.className = "result fake";
    } else {
      resultDiv.className = "result real";
    }
  }

  analyzeBtn.addEventListener("click", async function () {
    const text = newsText.value.trim();

    if (!text) {
      showError("Please enter some text to analyze");
      return;
    }

    try {
      showLoading();
      analyzeBtn.disabled = true;

      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: text }),
      });

      if (!response.ok) {
        throw new Error(`Server returned ${response.status}`);
      }

      const data = await response.json();
      showResult(data.prediction, data.confidence);
    } catch (error) {
      showError(`Error analyzing text: ${error.message}`);
      console.error("Error:", error);
    } finally {
      analyzeBtn.disabled = false;
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
