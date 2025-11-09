# Public_372

# Quy định chung

## Khái quát

1.1.1 Khả năng của AIS      AIS có khả năng cung cấp cho các tàu và bờ thông tin của một tàu, một cách tự động với   độ chính xác và tần suất theo yêu cầu, nhằm mục đích để theo dõi chính xác đường đi của   tàu.
1.1.2 Kiểm định chất lượng   Các nhà sản xuất được yêu cầu có hệ thống kiểm soát chất lượng được kiểm định để đảm   bảo việc thoả mãn điều kiện được ban hành. Cơ quan quản lý sẽ đánh giá sản phẩm sau khi   được đơn vị uỷ quyền đánh giá đảm bảo chất lượng trước khi lắp đặt trên tàu.

## Chế độ vận hành

Hệ thống phải có khả năng hoạt động theo các chế độ sau:
1.2.1 Chế độ “tự động và liên tục”   Chế độ “tự động và liên tục” có thể hoạt động liên tục ở mọi khu vực biển: ngoài khơi,
trong khu vực cảng, trong luồng hẹp.
1.2.2 Chế độ “chỉ định”   Chế độ “chỉ định” hoạt động tại một vùng cụ thể, tuỳ thuộc vào bộ phận điều khiển giao   thông tại đây, theo đó khoảng thời gian truyền dữ liệu và/hoặc các khe thời gian có thể   được thiết lập từ xa bởi bộ phận điểu khiển giao thông.
1.2.3 Chế độ “kiểm soát vòng”      Chế độ "kiểm soát vòng” khi tàu cần truyền dữ liệu để trả lời truy vấn của tàu khác hoặc   của trạm điều khiển giao thông.

# Quy định kỹ thuật

## Khái quát

Các quy định trong phần này liên quan từ lớp 1 đến lớp 4 (Lớp vật lý, Lớp kết nối, Lớp   mạng, Lớp vận tải) trong mô hình OSI.
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Lớp ứng d ụng</th>
<th>Col2</th>
<th>Col3</th>
</tr>
</thead>
<tbody>
<tr>
<td>Lớp trình diễn</td>
<td>Lớp trình diễn</td>
<td>Lớp trình diễn</td>
</tr>
<tr>
<td>Lớp phiên</td>
<td>Lớp phiên</td>
<td>Lớp phiên</td>
</tr>
<tr>
<td>Lớp vận tải</td>
<td>Lớp vận tải</td>
<td>Lớp vận tải</td>
</tr>
<tr>
<td>Lớp mạng<br>Kênh 1                               Kênh 2</td>
<td>Lớp mạng<br>Kênh 1                               Kênh 2</td>
<td>Lớp mạng<br>Kênh 1                               Kênh 2</td>
</tr>
<tr>
<td>Lớp liên kết<br>LME</td>
<td></td>
<td>Lớp liên kết<br>LME</td>
</tr>
<tr>
<td>Lớp liên kết DLS</td>
<td>Lớp liên kết DLS</td>
<td>Lớp liên kết DLS</td>
</tr>
</tbody>
</table>
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Lớp liên kế t<br>MAC</th>
<th>Col2</th>
<th>Lớp liên kế t<br>MAC</th>
</tr>
</thead>
<tbody>
<tr>
<td>Lớp vật lý</td>
<td>Lớp vật lý</td>
<td>Lớp vật lý</td>
</tr>
<tr>
<td>Rx1</td>
<td>Tx 1/2</td>
<td>Rx2</td>
</tr>
</tbody>
</table>
|---|---|---| |Lớp trình diễn|Lớp trình diễn|Lớp trình diễn| |Lớp phiên|Lớp phiên|Lớp phiên| |Lớp vận tải|Lớp vận tải|Lớp vận tải| |Lớp mạng<br>Kênh 1                               Kênh 2|Lớp mạng<br>Kênh 1                               Kênh 2|Lớp mạng<br>Kênh 1                               Kênh 2| |Lớp liên kết<br>LME||Lớp liên kết<br>LME| |Lớp liên kết DLS|Lớp liên kết DLS|Lớp liên kết DLS|           |---|---|---| |Lớp vật lý|Lớp vật lý|Lớp vật lý| |Rx1|Tx 1/2|Rx2|

### Hình 2 - Mô tả mô hình các lớp trong một trạm AIS

## Lớp vật lý

Lớp Vật lý làm nhiệm vụ truyền các luồng bít từ đầu ra ban đầu trên kênh dữ liệu. Lớp Vật   lý tuân theo ITU-R M.1371-1, Phụ lục 2, Chương 2.
Bảng 1 bao gồm các thông số kỹ thuật sẽ áp dụng cho các bộ thu TDMA.

### Bảng 1 - Các yêu cầu đặc tính bộ thu

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Thông số máy thu</th>
<th>Kênh 25 kHz</th>
<th>Kênh 12 5 kHz<br>,</th>
</tr>
</thead>
<tbody>
<tr>
<td>Độ nhạy</td>
<td>20 % PER, –107 dBm</td>
<td>20 % PER, –98 dBm</td>
</tr>
<tr>
<td>Triệt nhiễu cùng kênh</td>
<td>–10 dB ÷ 0 dB</td>
<td>–18 dB ÷ 0 dB</td>
</tr>
<tr>
<td>Độ chọn lọc kênh lân cận</td>
<td>70 dB</td>
<td>50 dB</td>
</tr>
<tr>
<td>Triệt đáp ứng giả</td>
<td>70 dB</td>
<td>N/A</td>
</tr>
</tbody>
</table>
|---|---|---| |Độ nhạy|20 % PER, –107 dBm|20 % PER, –98 dBm| |Triệt nhiễu cùng kênh|–10 dB ÷ 0 dB|–18 dB ÷ 0 dB| |Độ chọn lọc kênh lân cận|70 dB|50 dB| |Triệt đáp ứng giả|70 dB|N/A|

## Lớp liên kết

Lớp liên kết chỉ định phương thức đóng gói gói tin nhằm thực hiện việc phát hiện và sửa   lỗi cho quá trình truyền dữ liệu. Lớp liên kết chia thành 3 lớp con.

### Lớp liên kết con 1: Điều khiển truy nhập môi trường (MAC)

Lớp con MAC chỉ định phương thức truy nhập tới môi trường truyền dữ liệu, tức là kênh   dữ liệu VHF. Lớp này dùng phương thức truy nhập TDMA dùng tham chiếu thời gian   thông thường.

### Lớp liên kết con 2: Dịch vụ kênh dữ liệu (DSL)

Lớp con DLS chỉ định phương thức:
a. Khởi tạo và giải phóng kênh dữ liệu.
b. Truyền dữ liệu.
c. Giám sát và phát hiện lỗi.

### Lớp liên kết con 3: Thành phần quản lý kênh (LME)

LME điều khiển hoạt động của DLS, MAC và lớp vật lý.

## Lớp mạng

Lớp mạng dùng để:
a. Thiết lập và duy trì các kết nối kênh;
b. Quản lý các phép gán ưu tiên cho bản tin;
c. Phân phối các gói tin truyền vào các kênh.
Lớp mạng có cấu trúc tuân thủ Khuyến nghị ITU-R M.1371-1-1, Phụ lục 2, Chương 4.
Mọi thiết lập được khai thác vùng được lưu đều được gán thẻ ngày/giờ và các thông tin   đầu vào mà thiết lập được khai thác vùng thu được (TDMA Msg 22, tín hiệu mã DSC, đầu   vào nhập qua bàn phím, đầu vào chuỗi ACA nhập qua giao diện trình diễn).
AIS sẽ liên tục kiểm tra, nếu biên gần nhất của vùng được khai thác của mọi thiết lập cách   tàu đang đo trên 804,5 km, hoặc nếu mọi thiết lập được khai thác vùng đã dùng trên 5 tuần.

## Lớp vận tải

Lớp vận tải dùng để:
a. Chuyển đổi dữ liệu thành các gói tin với kích thước phù hợp để phát đi   b. Kiểm soát thứ tự các gói tin   c. Làm giao thức cầu nối với các lớp cao hơn.
Lớp vận tải có cấu trúc tuân thủ Khuyến nghị ITU-RM.1371-1-1, Phụ lục 2, Chương 5.

# Yêu cầu về nguồn điện và đảm bảo an toàn

## Độ bền với các điều kiện khác nhau của môi trường

### Bảng 2 - Độ bền với các điều kiện khác nhau của môi trường

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Điề kiện<br>u</th>
<th>Xách tay</th>
<th>Được<br>che chắ n</th>
<th>Ngoài trời</th>
<th>Ngập nước</th>
</tr>
</thead>
<tbody>
<tr>
<td>Khô nóng</td>
<td>+55 °C<br>(bảo quản +70<br>°C)</td>
<td>+55 °C</td>
<td>+55 °C<br>(bảo quản +70<br>°C)</td>
<td>(bảo quản +70<br>°C)</td>
</tr>
<tr>
<td>Nóng ẩm</td>
<td>+40 °C 93 %</td>
<td>+40 °C 93 %</td>
<td>+40 °C 93 %</td>
<td>x</td>
</tr>
<tr>
<td>Nhiệt độ thấp</td>
<td>–20 °C<br>(bảo quản<br>–30 °C)</td>
<td>–15 °C</td>
<td>–25 °C</td>
<td>x</td>
</tr>
<tr>
<td>Sốc nhiệt</td>
<td>45 K trong<br>nước</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>Rơi xuống mặt<br>phẳng cứng</td>
<td>6 lần từ độ cao<br>1 m</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>Rơi xuống<br>nước</td>
<td>3 lần từ độ cao<br>20 m</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
</tbody>
</table>
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Điề kiện<br>u</th>
<th>Xách tay</th>
<th>Được<br>che chắ n</th>
<th>Col4</th>
<th>Ngoài trời</th>
<th>Ngập nước</th>
</tr>
</thead>
<tbody>
<tr>
<td>Rung lắc</td>
<td>Rung  tại tần số 2 Hz – 13,2 Hz độ dịch chuyển ± 1 mm, tại 13,2 Hz –<br>100 Hz độ dịch chuyển 7 m/s2 và trong 2 h với mỗi lần cộng hưởng,<br>nói cách khác 2h quét tại 30 Hz theo cả 3 trục</td>
<td>Rung  tại tần số 2 Hz – 13,2 Hz độ dịch chuyển ± 1 mm, tại 13,2 Hz –<br>100 Hz độ dịch chuyển 7 m/s2 và trong 2 h với mỗi lần cộng hưởng,<br>nói cách khác 2h quét tại 30 Hz theo cả 3 trục</td>
<td>Rung  tại tần số 2 Hz – 13,2 Hz độ dịch chuyển ± 1 mm, tại 13,2 Hz –<br>100 Hz độ dịch chuyển 7 m/s2 và trong 2 h với mỗi lần cộng hưởng,<br>nói cách khác 2h quét tại 30 Hz theo cả 3 trục</td>
<td>Rung  tại tần số 2 Hz – 13,2 Hz độ dịch chuyển ± 1 mm, tại 13,2 Hz –<br>100 Hz độ dịch chuyển 7 m/s2 và trong 2 h với mỗi lần cộng hưởng,<br>nói cách khác 2h quét tại 30 Hz theo cả 3 trục</td>
<td>Rung  tại tần số 2 Hz – 13,2 Hz độ dịch chuyển ± 1 mm, tại 13,2 Hz –<br>100 Hz độ dịch chuyển 7 m/s2 và trong 2 h với mỗi lần cộng hưởng,<br>nói cách khác 2h quét tại 30 Hz theo cả 3 trục</td>
</tr>
<tr>
<td>Mưa và bụi<br>nước</td>
<td>x</td>
<td>x</td>
<td>Vòi 12,5 mm , lưu<br>lượng 100 lít/phút<br>và khoảng cách 3<br>m</td>
<td>Vòi 12,5 mm , lưu<br>lượng 100 lít/phút<br>và khoảng cách 3<br>m</td>
<td>X</td>
</tr>
<tr>
<td>Nhúng<br>vào<br>nước</td>
<td>100 kPa (1 bar)<br>trong 5 phút<br>10 kPa (0,1 bar)<br>với<br>VHF<br>2 <br>chiều</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>600 kPa (6 bar)<br>trong 12 h</td>
</tr>
<tr>
<td>Bức xạ mặt trời</td>
<td>1120 W/m2<br>80 h</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
<tr>
<td>Chống dầu bám</td>
<td>ISO Oil No. 1<br>24 h, 19 °C</td>
<td>x</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
</tbody>
</table>
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Điề kiện<br>u</th>
<th>Xách tay</th>
<th>Được<br>che chắ n</th>
<th>Ngoài trời</th>
<th>Ngập nước</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ăn mòn</td>
<td>Bốn chu kỳ, mỗi chu kỳ trong vòng 7 ngày tại 40 °C, độ ẩm tương đối<br>90 % – 95 % sau 2h phun nước muối</td>
<td>Bốn chu kỳ, mỗi chu kỳ trong vòng 7 ngày tại 40 °C, độ ẩm tương đối<br>90 % – 95 % sau 2h phun nước muối</td>
<td>Bốn chu kỳ, mỗi chu kỳ trong vòng 7 ngày tại 40 °C, độ ẩm tương đối<br>90 % – 95 % sau 2h phun nước muối</td>
<td>Bốn chu kỳ, mỗi chu kỳ trong vòng 7 ngày tại 40 °C, độ ẩm tương đối<br>90 % – 95 % sau 2h phun nước muối</td>
</tr>
<tr>
<td>CHÚ THÍCH: “x” – Không quy định</td>
<td>CHÚ THÍCH: “x” – Không quy định</td>
<td>CHÚ THÍCH: “x” – Không quy định</td>
<td>CHÚ THÍCH: “x” – Không quy định</td>
<td>CHÚ THÍCH: “x” – Không quy định</td>
</tr>
</tbody>
</table>
|---|---|---|---|---| |Khô nóng|+55 °C<br>(bảo quản +70<br>°C)|+55 °C|+55 °C<br>(bảo quản +70<br>°C)|(bảo quản +70<br>°C)| |Nóng ẩm|+40 °C 93 %|+40 °C 93 %|+40 °C 93 %|x| |Nhiệt độ thấp|–20 °C<br>(bảo quản<br>–30 °C)|–15 °C|–25 °C|x| |Sốc nhiệt|45 K trong<br>nước|x|x|x| |Rơi xuống mặt<br>phẳng cứng|6 lần từ độ cao<br>1 m|x|x|x| |Rơi xuống<br>nước|3 lần từ độ cao<br>20 m|x|x|x|                      |---|---|---|---|---|---| |Rung lắc|Rung  tại tần số 2 Hz – 13,2 Hz độ dịch chuyển ± 1 mm, tại 13,2 Hz –<br>100 Hz độ dịch chuyển 7 m/s2 và trong 2 h với mỗi lần cộng hưởng,<br>nói cách khác 2h quét tại 30 Hz theo cả 3 trục|Rung  tại tần số 2 Hz – 13,2 Hz độ dịch chuyển ± 1 mm, tại 13,2 Hz –<br>100 Hz độ dịch chuyển 7 m/s2 và trong 2 h với mỗi lần cộng hưởng,<br>nói cách khác 2h quét tại 30 Hz theo cả 3 trục|Rung  tại tần số 2 Hz – 13,2 Hz độ dịch chuyển ± 1 mm, tại 13,2 Hz –<br>100 Hz độ dịch chuyển 7 m/s2 và trong 2 h với mỗi lần cộng hưởng,<br>nói cách khác 2h quét tại 30 Hz theo cả 3 trục|Rung  tại tần số 2 Hz – 13,2 Hz độ dịch chuyển ± 1 mm, tại 13,2 Hz –<br>100 Hz độ dịch chuyển 7 m/s2 và trong 2 h với mỗi lần cộng hưởng,<br>nói cách khác 2h quét tại 30 Hz theo cả 3 trục|Rung  tại tần số 2 Hz – 13,2 Hz độ dịch chuyển ± 1 mm, tại 13,2 Hz –<br>100 Hz độ dịch chuyển 7 m/s2 và trong 2 h với mỗi lần cộng hưởng,<br>nói cách khác 2h quét tại 30 Hz theo cả 3 trục| |Mưa và bụi<br>nước|x|x|Vòi 12,5 mm , lưu<br>lượng 100 lít/phút<br>và khoảng cách 3<br>m|Vòi 12,5 mm , lưu<br>lượng 100 lít/phút<br>và khoảng cách 3<br>m|X| |Nhúng<br>vào<br>nước|100 kPa (1 bar)<br>trong 5 phút<br>10 kPa (0,1 bar)<br>với<br>VHF<br>2 <br>chiều|x|x|x|600 kPa (6 bar)<br>trong 12 h| |Bức xạ mặt trời|1120 W/m2<br>80 h|x|x|x|x| |Chống dầu bám|ISO Oil No. 1<br>24 h, 19 °C|x|x|x|x|               |---|---|---|---|---| |Ăn mòn|Bốn chu kỳ, mỗi chu kỳ trong vòng 7 ngày tại 40 °C, độ ẩm tương đối<br>90 % – 95 % sau 2h phun nước muối|Bốn chu kỳ, mỗi chu kỳ trong vòng 7 ngày tại 40 °C, độ ẩm tương đối<br>90 % – 95 % sau 2h phun nước muối|Bốn chu kỳ, mỗi chu kỳ trong vòng 7 ngày tại 40 °C, độ ẩm tương đối<br>90 % – 95 % sau 2h phun nước muối|Bốn chu kỳ, mỗi chu kỳ trong vòng 7 ngày tại 40 °C, độ ẩm tương đối<br>90 % – 95 % sau 2h phun nước muối| |CHÚ THÍCH: “x” – Không quy định|CHÚ THÍCH: “x” – Không quy định|CHÚ THÍCH: “x” – Không quy định|CHÚ THÍCH: “x” – Không quy định|CHÚ THÍCH: “x” – Không quy định|

## Nguồn điện

### Nguồn điện

Quy trình đo đầu vào và ra của nguồn điện tuân theo các quy định IEC 61162-1 hoặc IEC   61162-2 về điện áp và dòng lớn nhất và nhỏ nhất trên các kết cuối đầu vào.

### Yêu cầu kết quả

Các giao diện đáp ứng đầy đủ theo 2 tiêu chuẩn trên (IEC 61162-1 hoặc IEC 61162-2).

# Các điều kiện thử nghiệm

## Khái quát

Khi một yêu cầu trong tiêu chuẩn này khác với trong IEC 60945, yêu cầu trong tiêu chuẩn   này sẽ được áp dụng.

## Điều kiện thử nghiệm thông thường và tới hạn

### Điều kiện thử nghiệm thông thường

#### Nhiệt độ và độ ẩm

Nhiệt độ và độ ẩm phải nằm trong dải:
Nhiệt độ từ +15 °C đến +35 °C.
Độ ẩm từ 20 % đến 75 %.

#### Nguồn cấp

Nguồn cấp trong điều kiện thử nghiệm thông thường sẽ có dung sai tương đối trong   khoảng là ±3% so với điện áp danh nghĩa của nguồn điện trên tàu đã được thiết kế để   cung cấp cho thiết bị.

#### Điều kiện thử nghiệm tới hạn

Điều kiện thử nghiệm tới hạn được chỉ rõ trong IEC 60945. Khi được yêu cầu, phép thử   trong điều kiện tới hạn được thực hiện trong môi trường khô ráo và có điện áp cao hơn giới   hạn điện áp cấp cùng lúc đó, có nhiệt độ thấp và thấp hơn giới hạn điện áp cấp cùng lúc.

### Môi trường đo chuẩn

EUT được đo trong môi trường sử dụng thiết bị đo để mô phỏng và lưu các bản tin VDL.
Môi trường chuẩn gồm ít nhất 5 mục tiêu mô phỏng. Mức tín hiệu đầu vào ở cổng RF input   của EUT với mỗi mục tiêu ít nhất là -100 dBm. Các đầu vào thu được bằng cảm biến của   EUT, được mô phỏng bằng hệ thống đo kiểm hoặc các phương pháp khác. Được khai thác   và kiểm tra trên các kênh trong băng tần di động hàng hải.
Các kênh đang dùng sẽ được lựa chọn bằng tay thông qua các đầu vào hoặc các bản tin đã   gán kênh trước khi bắt đầu đo.