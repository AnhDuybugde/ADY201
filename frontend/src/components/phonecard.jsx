import React from "react";

const PhoneCard = ({ phone }) => {
  return (
    <div className="border rounded-xl p-4 shadow-sm bg-white hover:shadow-md transition duration-200">
      <h3 className="font-semibold text-lg mb-2 text-blue-600">
        {phone.model_name || "Không rõ tên"}
      </h3>

      <div className="space-y-1 text-sm text-gray-700">
        <p><strong>Hãng:</strong> {phone.manufacturer || "N/A"}</p>
        <p><strong>Giá:</strong> {phone.final_price ? `${phone.final_price}₫` : "Chưa rõ"}</p>
        <p><strong>ROM:</strong> {phone.rom_preprocessed || phone.rom || "N/A"}</p>
        <p><strong>RAM:</strong> {phone.memory_internal || "N/A"}</p>
        <p><strong>Pin:</strong> {phone.battery_capacity ? `${phone.battery_capacity} mAh` : "N/A"}</p>
        <p><strong>Màn hình:</strong> {phone.display_size || "N/A"}</p>
        <p><strong>Camera chính:</strong> {phone.camera_primary || "N/A"}</p>
        <p><strong>Camera phụ:</strong> {phone.camera_secondary || "N/A"}</p>
        <p><strong>Jack 3.5mm:</strong> {phone.jack_support || "N/A"}</p>
        <p><strong>NFC:</strong> {phone.nfc || "N/A"}</p>
        <p><strong>Sạc nhanh:</strong> {phone.watt ? `${phone.watt}W` : "N/A"}</p>
        <p><strong>Cảm biến:</strong> {phone.sensor || "N/A"}</p>
      </div>
    </div>
  );
};

export default PhoneCard;
