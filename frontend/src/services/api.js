const BASE_URL = "https://financial-health-assessment-7ayd.onrender.com";

export async function analyze() {
  const response = await fetch(`${BASE_URL}/finance/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      revenue: 100000,
      expenses: 60000,
    }),
  });

  if (!response.ok) {
    throw new Error("API call failed");
  }

  return response.json();
}

export async function uploadFile(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${BASE_URL}/upload/`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("File upload failed");
  }

  return response.json();
}
