# BƯỚC 1 (Phụ): Cần tính toán % trước
# Chúng ta cần một bảng tóm tắt số lượng và % của mỗi nhóm RAM
library(dplyr)

Test_summary <- Test %>%
  count(Ram) %>% # Đếm số lượng cho mỗi nhóm Ram
  mutate(
    percentage = n / sum(n), # Tính %
    label = scales::percent(percentage) # Tạo nhãn % đẹp mắt
  )

# BƯỚC 2: Tạo biểu đồ "cột" cho %
# x = "" (trống): để tạo 1 cột duy nhất
# y = n: độ cao của các phần (dựa trên số lượng)
# fill = as.factor(Ram): màu sắc
p_pie_base <- ggplot(Test_summary, aes(x = "", y = n, fill = as.factor(Ram))) +
  geom_bar(stat = "identity", width = 1) +
  
  # BƯỚC 3: "Uốn cong" nó thành biểu đồ tròn
  coord_polar("y", start = 0) + 
  
  # Thêm nhãn % vào
  geom_text(aes(label = label), position = position_stack(vjust = 0.5)) +
  
  labs(
    title = "Tỷ lệ các mức RAM",
    fill = "RAM (GB)",
    x = NULL, # Bỏ nhãn trục X
    y = NULL  # Bỏ nhãn trục Y
  ) +
  theme_void() # Xóa toàn bộ nền, trục, chữ...

# BƯỚC 4: Biến nó thành tương tác
# Khi di chuột, bạn sẽ thấy số lượng (n) và % (label)
ggplotly(p_pie_base, tooltip = c("fill", "n", "label"))