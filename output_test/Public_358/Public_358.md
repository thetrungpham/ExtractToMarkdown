# Public_358

# Giới thiệu

Các lỗi sinh ra bởi một số nguyên nhân sau:
* Do can thiệp của con người;
* Nhiễu nhiệt;
* Các điện áp cảm ứng trong thiết bị và cáp do sét, chớp, sóng vô tuyến và các hiệu   ứng điện từ trường khác;
* Mất đồng bộ sau khi bị trượt không điều khiển được;
* Các điểm tiếp xúc và kết nối.
Nguyên nhân chính gây ra lỗi là các điện áp cảm ứng và các lỗi này thường xảy ra   với mật độ lớn do các hiện tượng đặc biệt nào đó xuất hiện. Sự phát triển của công   nghệ không những giúp con người có sự hiểu biết sâu sắc hơn về các hiệu ứng điện   từ trường mà còn có phương hướng lâu dài trong việc giảm các tỷ lệ về lỗi.
Các nghiên cứu của ITU-T đã chứng minh rằng tỷ lệ lỗi đối với đường truyền ít   phụ thuộc vào khoảng cách.

# Các tài liệu tham khảo

Khuyến nghị G.826 của ITU-T về giới hạn lỗi đối với đường truyền chuẩn lý thuyết   là 27 500 km. Để có thể áp dụng các số liệu này cho kênh thuê riêng thì cần phải   định nghĩa các đường truyền chuẩn để đại diện cho các kênh thuê riêng được đề   cập tới trong Quy chuẩn này. Đường truyền chuẩn trên mặt đất và đường truyền   chuẩn qua vệ tinh được định nghĩa trong C.2.1 và C.2.2 dựa trên cơ sở Khuyến   nghị G.826 của ITU-T.

## Đường truyền trên mặt đất

Hình C.1 mô tả đường truyền chuẩn trên mặt đất qua việc tính toán giới hạn lỗi   như đã chỉ ra trong Quy chuẩn này.
1

### Hình C.1 - Đường truyền chuẩn cho kênh thuê riêng trên mặt đất tốc độ

### 2 048 kbit/s.

Đường truyền chuẩn trong Hình C.1 gồm có 2 nước tại 2 đầu cuối và một nước   trung gian. Tại nước có điểm đầu cuối thì khoảng cách tính từ điểm NTP đến cổng   đi quốc tế tối đa là 1 000 km. Đối với nước trung gian thì khoảng cách tối đa là 3   500 km nếu chỉ có một cổng quốc tế. Khoảng cách trên được tính bằng 1,5 lần   khoảng cách theo đường thẳng trừ trường hợp nếu là cáp ngầm dưới biển thì   khoảng cách sẽ là khoảng cách thực tế.
CHÚ THÍCH: mô hình này cho phép khoảng cách tổng cộng lên đến 5500 km.
Mặc dù đường truyền chuẩn này biểu diễn các phần của các quốc gia riêng biệt,
nhưng trong Quy chuẩn này không tách lỗi riêng tại từng quốc gia và các lỗi có thể   được phân tách theo cách khác.

## Đường truyền qua vệ tinh

### Hình C.2 - Đường truyền chuẩn cho kênh thuê riêng qua vệ tinh tốc độ

### 2 048 kbit/s

2    |<image_1>|   |<image_2>|      Đường truyền chuẩn trong Hình C.2 gồm có đường truyền vệ tinh kết nối hai quốc   gia có điểm đầu cuối. Đối với mỗi nước có điểm đầu cuối thì khoảng cách là   khoảng 1 000 km.

# Tiêu chí với lỗi

Trong Bảng C.1 và C.2 thể hiện phân bố theo tỷ lệ phần trăm về lỗi tổng cộng   trong Khuyến nghị G.826 của ITU-T đối với các phần khác nhau của kênh thuê   riêng dựa theo đường truyền chuẩn (đường truyền mặt đất và đường truyền vệ tinh)
như định nghĩa trong C.2. Các bảng dưới đây bao gồm phân bố cố định và phân bố   theo khoảng cách với 1% cho chiều dài 500 km.

### Bảng C.1 - Phân bố nguyên nhân lỗi theo Khuyến nghị G.826 - Đường

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>truyền mặt đất và đường truyền</th>
<th>vệ tinh</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Phần đường truyền**</td>
<td>**Phân bố lỗi**</td>
</tr>
<tr>
<td>**Đường truyền mặt đất**</td>
<td>**Đường truyền mặt đất**</td>
</tr>
<tr>
<td>Quốc gia 1 (phân bố cố định)</td>
<td>17,5%</td>
</tr>
<tr>
<td>Quốc gia 1 (tối đa 1 000 km)</td>
<td>2,0%</td>
</tr>
<tr>
<td>Điểm quá giang quốc tế</td>
<td>1,0%</td>
</tr>
<tr>
<td>Quá giang quốc tế (phân bố cố định)</td>
<td>2,0%</td>
</tr>
<tr>
<td>Quá giang quốc tế (tối đa 3 500 km)</td>
<td>7,0%</td>
</tr>
<tr>
<td>Điểm quá giang quốc tế</td>
<td>1,0%</td>
</tr>
<tr>
<td>Quốc gia 2 (tối đa 1 000 km)</td>
<td>2,0%</td>
</tr>
<tr>
<td>Quốc gia 2 (phân bố cố định)</td>
<td>17,5%</td>
</tr>
<tr>
<td>Tổng cộng</td>
<td>50,0%</td>
</tr>
<tr>
<td>**Đường truyền vệ tinh**</td>
<td>**Đường truyền vệ tinh**</td>
</tr>
<tr>
<td>Quốc gia 1 (phân bố cố định)</td>
<td>17,5%</td>
</tr>
</tbody>
</table>
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Quố c gi a 1 (tối đ a 1 000 k m)</th>
<th>2 0%<br>,</th>
</tr>
</thead>
<tbody>
<tr>
<td>Điểm kết nối quốc tế</td>
<td>2,0%</td>
</tr>
<tr>
<td>Đường truyền vệ tinh</td>
<td>35,0%</td>
</tr>
<tr>
<td>Điểm kết nối quốc tế</td>
<td>2,0%</td>
</tr>
<tr>
<td>Quốc gia 2 (tối đa 1 000 km)</td>
<td>2,0%</td>
</tr>
<tr>
<td>Quốc gia 2 (phân bố cố định)</td>
<td>17,5%</td>
</tr>
<tr>
<td>**Tổng cộng**</td>
<td>78,0%</td>
</tr>
</tbody>
</table>
|---|---| |**Phần đường truyền**|**Phân bố lỗi**| |**Đường truyền mặt đất**|**Đường truyền mặt đất**| |Quốc gia 1 (phân bố cố định)|17,5%| |Quốc gia 1 (tối đa 1 000 km)|2,0%| |Điểm quá giang quốc tế|1,0%| |Quá giang quốc tế (phân bố cố định)|2,0%| |Quá giang quốc tế (tối đa 3 500 km)|7,0%| |Điểm quá giang quốc tế|1,0%| |Quốc gia 2 (tối đa 1 000 km)|2,0%| |Quốc gia 2 (phân bố cố định)|17,5%| |Tổng cộng|50,0%| |**Đường truyền vệ tinh**|**Đường truyền vệ tinh**| |Quốc gia 1 (phân bố cố định)|17,5%|    3       |---|---| |Điểm kết nối quốc tế|2,0%| |Đường truyền vệ tinh|35,0%| |Điểm kết nối quốc tế|2,0%| |Quốc gia 2 (tối đa 1 000 km)|2,0%| |Quốc gia 2 (phân bố cố định)|17,5%| |**Tổng cộng**|78,0%|   CHÚ THÍCH: Nếu có thêm các quốc gia quá giang vào đường truyền mặt đất thì   sẽ phải bổ sung thêm tỷ lệ phân bố cố định (2%), điểm kết cuối quá giang (1%) và   khoảng cách đường truyền (1% cho 500 km). Thông tin thêm về vấn đề này có   trong Khuyến nghị G.826 của ITU-T.
Khuyến nghị G.826 của ITU-T định nghĩa về các lỗi theo các cụm từ giây bị lỗi   ES, giây bị lỗi nghiêm trọng SES và lỗi khối nền BBE cho đường truyền chuẩn lý   thuyết có chiều dài 27 500 km, các tỷ lệ này cho trong cột 2 của Bảng C.3.
Việc áp dụng các tỷ lệ trong Bảng C.1 và C.2 vào vấn đề lỗi trong Khuyến nghị   G.826 của ITU-T đưa ra các tỷ lệ về lỗi đối với kênh thuê riêng cấu trúc số 2 048   kbit/s như trong cột 3 và 4 của Bảng C.3 tương ứng với đường truyền mặt đất và   đường truyền vệ tinh.

### Bảng C.2 - Tỷ lệ lỗi dài hạn áp dụng cho kênh thuê riêng cấu trúc số

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Col1</th>
<th>Col2</th>
<th>2 048 kbit/s</th>
<th>Col4</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tham số</td>
<td>G.826</td>
<td>Đường truyền mặt<br>đất</td>
<td>Đường truyền vệ<br>tinh</td>
</tr>
<tr>
<td>Tỷ lệ ES<br>Tỷ lệ SES</td>
<td>4,00%<br>0,20%</td>
<td>2,000 %<br>0,100%</td>
<td>3,120%<br>0,156%</td>
</tr>
</tbody>
</table>
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Tỷ lệ BBE</th>
<th>0 03%<br>,</th>
<th>0 015%<br>,</th>
<th>0 023%<br>,</th>
</tr>
</thead>
<tbody>
<tr>
<td>CHÚ THÍCH: các số liệu trong bảng này đã được làm tròn, các số liệu chính xác<br>được sử dụng để tính toán các giới hạn trong các mục tiếp theo.</td>
<td>CHÚ THÍCH: các số liệu trong bảng này đã được làm tròn, các số liệu chính xác<br>được sử dụng để tính toán các giới hạn trong các mục tiếp theo.</td>
<td>CHÚ THÍCH: các số liệu trong bảng này đã được làm tròn, các số liệu chính xác<br>được sử dụng để tính toán các giới hạn trong các mục tiếp theo.</td>
<td>CHÚ THÍCH: các số liệu trong bảng này đã được làm tròn, các số liệu chính xác<br>được sử dụng để tính toán các giới hạn trong các mục tiếp theo.</td>
</tr>
</tbody>
</table>
|---|---|---|---| |Tham số|G.826|Đường truyền mặt<br>đất|Đường truyền vệ<br>tinh| |Tỷ lệ ES<br>Tỷ lệ SES|4,00%<br>0,20%|2,000 %<br>0,100%|3,120%<br>0,156%|    4       |---|---|---|---| |CHÚ THÍCH: các số liệu trong bảng này đã được làm tròn, các số liệu chính xác<br>được sử dụng để tính toán các giới hạn trong các mục tiếp theo.|CHÚ THÍCH: các số liệu trong bảng này đã được làm tròn, các số liệu chính xác<br>được sử dụng để tính toán các giới hạn trong các mục tiếp theo.|CHÚ THÍCH: các số liệu trong bảng này đã được làm tròn, các số liệu chính xác<br>được sử dụng để tính toán các giới hạn trong các mục tiếp theo.|CHÚ THÍCH: các số liệu trong bảng này đã được làm tròn, các số liệu chính xác<br>được sử dụng để tính toán các giới hạn trong các mục tiếp theo.|

# Lỗi dài hạn

Các tỷ lệ lỗi trong C.3 áp dụng cho đường truyền chuẩn có thể sử dụng để tính toán   các yêu cầu đối với lỗi dài hạn, biểu diễn bằng một số tuyệt đối trong khoảng thời   gian 24 giờ; các con số này được cho trong hàng 1 của Bảng C.4 và C.5 tương ứng   với đường truyền mặt đất và đường truyền vệ tinh.
Tuy nhiên các yêu cầu về lỗi đã được chỉ ra là các số liệu thống kê dựa trên việc   đo kiểm dài hạn (hơn một tháng), không sử dụng số liệu thống kê trong vòng 24   giờ. Do đó, Khuyến nghị M.2100 của ITU-T đưa ra một phương pháp đo có thể   giảm thời gian đo xuống là 24 giờ với các giá trị giới hạn S1 và S2. S1 là giới hạn   mà thấp hơn mức này đường truyền hoạt động tốt đáp ứng yêu cầu, S2 là giới hạn   mà trên mức này đường truyền không còn đáp ứng được yêu cầu. Các giá trị nằm   trong khoảng S1 và S2 là không xác định được trạng thái hoạt động của đường   truyền. Do đó để có thể kết luận là đường truyền hoạt động tốt đáp ứng yêu cầu   dài hạn thì kết quả đo trong khoảng thời gian 24 giờ phải tốt hơn giá trị giới hạn   S1.
S1 và S2 được tính như sau:
𝑆1 = (𝑌ê𝑢 𝑐ầ𝑢) −2 × √(𝑌ê𝑢 𝑐ầ𝑢)
𝑆2 = (𝑌ê𝑢 𝑐ầ𝑢) + 2 × √(𝑌ê𝑢 𝑐ầ𝑢)

### Bảng C.3 - Các giá trị giới hạn đối với độ dài khối là 2 048 bit - Đường

### truyền mặt đất

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Thông số</th>
<th>ES</th>
<th>SES</th>
<th>BBE</th>
</tr>
</thead>
<tbody>
<tr>
<td>Lỗi dài hạn</td>
<td>1 728 / 24h</td>
<td>86/ 24h</td>
<td>12 960/ 24h</td>
</tr>
</tbody>
</table>
|---|---|---|---| |Lỗi dài hạn|1 728 / 24h|86/ 24h|12 960/ 24h|    5

### Bảng C.4 - Các giá trị giới hạn đối với độ dài khối là 2 048 bit - Đường

### truyền  vệ tinh

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Thông số</th>
<th>ES</th>
<th>SES</th>
<th>BBE</th>
</tr>
</thead>
<tbody>
<tr>
<td>Lỗi dài hạn</td>
<td>2 696 / 24h</td>
<td>135 / 24h</td>
<td>20 218 / 24h</td>
</tr>
<tr>
<td>**Thời gian đo 24 giờ**<br>Giá trị giới hạn S1<br>Giá trị giới hạn S2</td>
<td>2 592 / 24h<br>2 800 / 24h</td>
<td>112 / 24h<br>158 / 24h</td>
<td>19 933 / 24h<br>20 502 / 24h</td>
</tr>
</tbody>
</table>
|---|---|---|---| |Lỗi dài hạn|2 696 / 24h|135 / 24h|20 218 / 24h| |**Thời gian đo 24 giờ**<br>Giá trị giới hạn S1<br>Giá trị giới hạn S2|2 592 / 24h<br>2 800 / 24h|112 / 24h<br>158 / 24h|19 933 / 24h<br>20 502 / 24h|    6