# BƯỚC 1: Tạo biểu đồ cột bằng ggplot
# x = as.factor(Ram): Mỗi cột là một mức RAM
# fill = as.factor(Ram): Tô màu các cột
# (Lưu ý: Chúng ta không cần y, vì geom_bar() sẽ tự động đếm số hàng)

p_bar <- ggplot(data = Test, aes(x = as.factor(Ram), fill = as.factor(Ram))) +
  geom_bar() + # Sử dụng geom_bar()
  labs(
    title = "Số lượng điện thoại theo dung lượng RAM",
    x = "Dung lượng RAM (GB)",
    y = "Số lượng", # Trục Y bây giờ là số đếm (count)
    fill = "RAM (GB)"
  ) +
  theme_minimal()

# BƯỚC 2: Biến nó thành tương tác
ggplotly(p_bar)