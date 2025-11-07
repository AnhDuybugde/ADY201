library(ggplot2)
library(plotly)
library(scales)

# (Giả sử bạn đã có data frame tên là Test)

# BƯỚC 1: Tạo biểu đồ boxplot bằng ggplot
# x = as.factor(Ram): Phân nhóm theo RAM
# y = Price: Giá trị để vẽ boxplot
# fill = as.factor(Ram): Tô màu khác nhau cho mỗi nhóm RAM

p_box <- ggplot(data = Test, aes(x = as.factor(Ram), y = Price, fill = as.factor(Ram))) +
  geom_boxplot() + # Sử dụng geom_boxplot()
  labs(
    title = "Phân bổ Giá điện thoại theo RAM",
    x = "Dung lượng RAM (GB)",
    y = "Giá (VNĐ)",
    fill = "RAM (GB)"
  ) +
  theme_minimal() +
  scale_y_continuous(labels = scales::label_number(big.mark = ".")) # Định dạng trục Y

# BƯỚC 2: Biến nó thành tương tác
ggplotly(p_box)