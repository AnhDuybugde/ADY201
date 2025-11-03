# Tải các thư viện cần thiết
library(ggplot2)
library(plotly)
library(scales) # <-- Thêm thư viện này

# (Giả sử bạn đã có data frame tên là Test)

p_phone <- ggplot(data = Test, aes(x = Ram, y = Price, color = as.factor(Ram))) +
  geom_point(size = 3) +
  geom_smooth(method = "lm", se = FALSE, color = "darkblue", linetype = "dashed") +
  labs(
    title = "Mối quan hệ giữa RAM và Giá điện thoại",
    x = "Dung lượng RAM (GB)",
    y = "Giá (VNĐ)",
    color = "RAM (GB)"
  ) +
  theme_minimal() +
  
  # ----- DÒNG MỚI ĐƯỢC THÊM VÀO ĐÂY -----
scale_y_continuous(labels = scales::label_number(big.mark = "."))

# Chạy lệnh plotly như cũ
ggplotly(p_phone)