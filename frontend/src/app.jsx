import React, { useEffect, useState } from "react";
import { getPhones } from "./api";
import PhoneCard from "./components/phonecard";
import Home from "./pages/home";

function App() {
  return (
    // You should wrap your component in a top-level element, 
    // like a div or a React Fragment (<>...</>).
    <div>
      <Home />
    </div>
  );
//   const [phones, setPhones] = useState([]);

//   useEffect(() => {
//     const fetchData = async () => {
//       const data = await getPhones();
//       console.log(data)
//       setPhones(data);
//     };
//     fetchData();
//   }, []);

//   return (
//     <div className="p-6 grid grid-cols-3 gap-4">
//       {phones.length > 0 ? (
//         phones.map((phone, idx) => <PhoneCard key={idx} phone={phone} />)
//       ) : (
//         <p>Đang tải dữ liệu...</p>
//       )}
//     </div>
//   );
}

export default App;
