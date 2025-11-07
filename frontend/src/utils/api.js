import axios from "axios";

const API_BASE = "http://127.0.0.1:5000/api";

export const getPhones = async () => {
  try {
    const res = await axios.get(`${API_BASE}/phones`);
    return res.data;
  } catch (err) {
    console.error("❌ Lỗi khi gọi API:", err);
    return [];
  }
};
