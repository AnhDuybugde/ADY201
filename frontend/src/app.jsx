import React, { useEffect, useState } from "react";
import { getPhones } from "./api";
import PhoneCard from "./components/phonecard";

function App() {
  const [phones, setPhones] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await getPhones();
      setPhones(data);
    };
    fetchData();
  }, []);

  return (
    <div className="p-6 grid grid-cols-3 gap-4">
      {phones.length > 0 ? (
        phones.map((phone, idx) => <PhoneCard key={idx} phone={phone} />)
      ) : (
        <p>Đang tải dữ liệu...</p>
      )}
    </div>
  );
}

export default App;
