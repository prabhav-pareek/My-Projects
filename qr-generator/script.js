document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("qrForm");
    const input = document.getElementById("qrInput");
    const canvas = document.getElementById("qrCanvas");
    const downloadBtn = document.getElementById("downloadBtn");
    const qrResult = document.getElementById("qrResult");
    const themeToggle = document.getElementById("themeToggle");
    const modeText = document.getElementById("modeText");
  
    const ctx = canvas.getContext("2d");
  
    // Handle Form Submission
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const text = input.value;
  
      // Generate QR Code
      fetch(`/generate_qr`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      })
        .then((res) => res.blob())
        .then((blob) => {
          const url = URL.createObjectURL(blob);
          const img = new Image();
          img.src = url;
  
          img.onload = () => {
            canvas.width = img.width;
            canvas.height = img.height;
            ctx.drawImage(img, 0, 0);
  
            qrResult.style.display = "block";
          };
        });
    });
  
    // Handle Download
    downloadBtn.addEventListener("click", () => {
      const link = document.createElement("a");
      link.download = "qr-code.png";
      link.href = canvas.toDataURL();
      link.click();
    });
  
    // Theme Toggle
    themeToggle.addEventListener("change", () => {
      document.body.classList.toggle("dark");
      modeText.textContent = themeToggle.checked ? "Dark Mode" : "Light Mode";
    });
  });
  