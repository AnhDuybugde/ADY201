import React, { useState, useEffect } from "react";
import SearchBar from "../components/searchbar";
import PhoneCard from "../components/phonecard";
import api from "../utils/api";

const Home = () => {
  const [phones, setPhones] = useState([]);

  const fetchPhones = async (query = "") => {
    try {
      const res = await api.get("/phones", {
        params: { q: query },
      });
      setPhones(res.data);
      // console.log(res.data)
    } catch (err) {
      console.error("Lỗi tải danh sách điện thoại:", err);
    }
  };

  useEffect(() => {
    fetchPhones();
  }, []);

  return (
    <div>
      <SearchBar onSearch={fetchPhones} />
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {phones.map((phone, i) => (
          <PhoneCard key={i} phone={phone} />
        ))}
      </div>
    </div>
  );
};

export default Home;
