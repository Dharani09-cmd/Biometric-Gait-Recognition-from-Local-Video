function analyzeVideo() {
  const fileInput = document.getElementById("videoInput");
  const resultCard = document.getElementById("resultCard");
  const resultsContainer = document.getElementById("resultsContainer");

  if (!fileInput.files.length) {
    alert("Please select a video file!");
    return;
  }

  const fileName = fileInput.files[0].name;
  resultCard.classList.remove("hidden");
  resultsContainer.innerHTML = `<p>Analyzing "${fileName}"...</p><p>🧠 Running gait recognition model...</p>`;

  setTimeout(() => {
    resultsContainer.innerHTML = `
      <h3>✅ Analysis Complete</h3>
      <p><strong>Video File:</strong> ${fileName}</p>
      <p><strong>Gait ID Match:</strong> User_07</p>
      <p><strong>Confidence:</strong> 94.7%</p>
      <p><strong>Stride Pattern:</strong> Consistent</p>
      <p><strong>Anomaly Detection:</strong> None</p>
      <p><strong>Processing Time:</strong> 2.4s</p>
    `;
  }, 2500);
}

function showInfo() {
  alert("This AI dashboard analyzes human gait patterns from local video files to verify identity and detect anomalies using pose estimation and machine learning models.");
}
