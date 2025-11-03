document.getElementById("predictForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData.entries());

  // Convert numeric fields properly
  for (const key in data) {
    if (!isNaN(data[key])) data[key] = Number(data[key]);
  }

  document.getElementById("result").innerHTML = "⏳ Predicting...";

  try {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    if (result.status === "success") {
      document.getElementById("result").innerHTML = `
        ✅ <strong>Prediction:</strong> ${result.category}<br>
        <em>(Code: ${result.prediction_code})</em>
      `;
    } else {
      document.getElementById("result").innerHTML = `⚠️ Error: ${result.error}`;
    }
  } catch (error) {
    document.getElementById("result").innerHTML = `🚫 Failed: ${error}`;
  }
});
