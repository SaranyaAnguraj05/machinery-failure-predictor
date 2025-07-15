// frontend/script.js
document.getElementById("form").addEventListener("submit", async function (e) {
  e.preventDefault();
  const temperature = parseFloat(document.getElementById("temperature").value);
  const pressure = parseFloat(document.getElementById("pressure").value);
  const vibration = parseFloat(document.getElementById("vibration").value);
  const humidity = parseFloat(document.getElementById("humidity").value);

  const response = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ temperature, pressure, vibration, humidity })
  });

  const result = await response.json();
  document.getElementById("result").innerText = `Prediction: ${result.prediction}`;
});
