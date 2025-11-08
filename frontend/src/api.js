// src/api.js
import axios from "axios";

const API_URL = "http://127.0.0.1:5000/api"; // Flask backend của bạn

// Hàm lấy danh sách điện thoại
export const getPhones = async () => {
  try {
    const res = await axios.get(`${API_URL}/phones`);
    return res.data;
  } catch (error) {
    console.error("Error fetching phones:", error);
    return [];
  }
};
