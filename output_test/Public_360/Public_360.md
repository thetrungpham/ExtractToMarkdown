# Public_360

# Điều kiện môi trường

Các yêu cầu kỹ thuật trong quy chuẩn này áp dụng trong điều kiện môi trường hoạt động của thiết bị và phải được công bố bởi nhà sản xuất. Thiết bị phải tuân thủ mọi yêu cầu kỹ thuật của quy chuẩn này khi hoạt động trong các giới hạn biên của điều kiện môi trường hoạt động đã công bố.

# Yêu cầu kỹ thuật

## Công suất ra cực đại của máy phát

### Định nghĩa

Các loại công suất của UE sau đây xác định công suất ra cực đại đối với băng thông truyền dẫn bất kỳ thuộc băng thông kênh NB.
Đối với khoảng cách sóng mang con 3,75 kHz, công suất đầu ra cực đại được xác định là công suất trung bình trong khoảng thời gian ít nhất một khe (2 ms) không bao gồm khoảng cách 2 304 Ts khi UE không truyền.
Đối với khoảng cách sóng mang con 15 kHz, công suất đầu ra cực đại được xác định là công suất trung bình của trong thời gian ít nhất một khung con (1 ms).

### Giới hạn

Công suất ra cực đại của UE không được vượt các giá trị tại Bảng 1.

### Bảng 1 - Các loại công suất UE

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
<th>Băng tầ n<br>NB</th>
<th>Loại 3<br>(dBm)</th>
<th>Dung sai (dB)</th>
<th>Loại 5<br>(dBm)</th>
<th>Dung sai (dB)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>23</td>
<td>± 2,7</td>
<td>20</td>
<td>± 2,7</td>
</tr>
<tr>
<td>3</td>
<td>23</td>
<td>± 2,7</td>
<td>20</td>
<td>± 2,7</td>
</tr>
<tr>
<td>5</td>
<td>23</td>
<td>± 2,7</td>
<td>20</td>
<td>± 2,7</td>
</tr>
<tr>
<td>8</td>
<td>23</td>
<td>± 2,7</td>
<td>20</td>
<td>± 2,7</td>
</tr>
<tr>
<td>28</td>
<td>23</td>
<td>± 2,7</td>
<td>20</td>
<td>± 2,7</td>
</tr>
</tbody>
</table>
|---|---|---|---|---| |1|23|± 2,7|20|± 2,7| |3|23|± 2,7|20|± 2,7| |5|23|± 2,7|20|± 2,7| |8|23|± 2,7|20|± 2,7| |28|23|± 2,7|20|± 2,7|

## Mặt nạ phổ phát xạ của máy phát

### Định nghĩa

Mặt nạ phổ phát xạ của UE áp dụng đối với các tần số Δf OOB bắt đầu từ ± biên băng thông kênh NB được cấp phát.
1

### Giới hạn

Công suất phát xạ của UE bất kỳ phải tuân thủ theo các yêu cầu tại Bảng 2.

### Bảng 2 - Mặt nạ phổ phát xạ UE NB

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Δf OOB(kHz)</th>
<th>Giới hạn phổ phát xạ (dBm)</th>
<th>Băng thông đo</th>
</tr>
</thead>
<tbody>
<tr>
<td>± 0</td>
<td>24,5</td>
<td>30 kHz</td>
</tr>
<tr>
<td>± 100</td>
<td>-3,5</td>
<td>30 kHz</td>
</tr>
<tr>
<td>± 150</td>
<td>-6,5</td>
<td>30 kHz</td>
</tr>
<tr>
<td>± 300</td>
<td>-27,5</td>
<td>30 kHz</td>
</tr>
<tr>
<td>± 500 – 1 700</td>
<td>-33,5</td>
<td>30 kHz</td>
</tr>
</tbody>
</table>
|---|---|---| |± 0|24,5|30 kHz| |± 100|-3,5|30 kHz| |± 150|-6,5|30 kHz| |± 300|-27,5|30 kHz| |± 500 – 1 700|-33,5|30 kHz|

## Phát xạ giả của máy phát

### Định nghĩa

Phát xạ giả của máy phát là các phát xạ được tạo ra bởi các hiệu ứng không mong muốn của máy phát như: các phát xạ hài, phát xạ ký sinh, các thành phần xuyên điều chế và các thành phần đổi tần nhưng không bao gồm các phát xạ ngoài băng.
Các giới hạn phát xạ giả được quy định tại các điều khoản yêu cầu chung phù hợp với khuyến nghị ITU-R SM.329-12 và yêu cầu băng tần hoạt động NB của UE.
Để nâng cao độ chính xác, độ nhạy và hiệu quả của phép đo, băng thông phân giải có thể nhỏ hơn băng thông đo. Khi băng thông phân giải nhỏ hơn băng thông đo,
kết quả đo phải được lấy tích phân trên băng thông đo để thu được băng thông tạp  âm tương đương của băng thông đo.

### Giới hạn

Trừ ranh giới giữa ngoài băng NB và miền giả f OOB = 1,7 MHz, khi UE được cấu hình cho truyền dẫn đường lên NB các giới hạn sau đây được áp dụng:
Các giới hạn phát xạ giả trong Bảng 4 áp dụng đối với các dải tần số lớn hơn  f OOB  (MHz) tại Bảng 3 tính từ biên của băng thông kênh.
Công suất trung bình của phát xạ giả đo được đối với yêu cầu chung không được  vượt quá các giá trị tại Bảng 4.

### Bảng 3 - Ranh giới Δf** **OOB** **giữa kênh NB và miền phát xạ giả

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
<th>Băng thông kênh</th>
<th>5 MHz</th>
<th>10 MHz</th>
<th>15 MHz</th>
<th>20 MHz</th>
</tr>
</thead>
<tbody>
<tr>
<td>ΔfOOB (MHz)</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
</tr>
</tbody>
</table>
|---|---|---|---|---| |ΔfOOB (MHz)|10|15|20|25|    2       CHÚ THÍCH 1: Đối với điều kiện đo tại biên của mỗi dải tần số, tần số thấp nhất của điểm đo trong mỗi dải tần số được đặt tại ranh giới thấp nhất của dải tần số cộng với MBW/2. Tần số cao nhất của điểm đo trong mỗi dải tần số nên được đặt tại ranh giới cao nhất của dải tần số trừ MBW/2. MBW là ký hiệu cho băng thông đo xác định cho băng bảo vệ.

### Bảng 4 - Giới hạn phát xạ giả

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Dải tầ n số</th>
<th>Mức tối đa</th>
<th>Băng thông đo</th>
</tr>
</thead>
<tbody>
<tr>
<td>9 kHz ≤ f < 150 kHz</td>
<td>-36 dBm</td>
<td>1 kHz</td>
</tr>
<tr>
<td>150 kHz ≤ f < 30 MHz</td>
<td>-36 dBm</td>
<td>10 kHz</td>
</tr>
<tr>
<td>30 MHz ≤ f < 1 GHz</td>
<td>-36 dBm</td>
<td>100 kHz</td>
</tr>
<tr>
<td>1 GHz ≤ f < 12,75 GHz</td>
<td>-30 dBm</td>
<td>1 MHz</td>
</tr>
</tbody>
</table>
|---|---|---| |9 kHz ≤ f < 150 kHz|-36 dBm|1 kHz| |150 kHz ≤ f < 30 MHz|-36 dBm|10 kHz| |30 MHz ≤ f < 1 GHz|-36 dBm|100 kHz| |1 GHz ≤ f < 12,75 GHz|-30 dBm|1 MHz|

## Công suất ra cực tiểu của máy phát

### Định nghĩa

Đối với UE NB, công suất đầu ra cực tiểu truyền đơn âm và đa âm trên băng thông  kênh là -40 dBm.
Đối với khoảng cách sóng mang con 3,75 kHz, công suất đầu ra cực tiểu được xác định là công suất trung bình trong khoảng thời gian ít nhất một khe (2 ms) không bao gồm khoảng cách 2 304 Ts khi UE không truyền. Đối với khoảng cách sóng mang con 15 kHz, công suất đầu ra cực tiểu được xác định là công suất trung bình  trên một khung con (1 ms).

### Giới hạn

Công suất đầu ra cực tiểu không vượt quá giá trị -40 dBm cho tất cả các băng thông  kênh NB.

## Độ chọn lọc kênh lân cận của máy thu

### Định nghĩa

Độ chọn lọc kênh lân cận của máy thu là tham số đánh giá khả năng nhận tín hiệu tại kênh tần số được cấp phát của máy thu khi có sự hiện diện của tín hiệu kênh lân cận tại tần số lệch cho trước so với tần số trung tâm của kênh được cấp phát.
ACS là tỉ số giữa mức suy hao của bộ lọc máy thu trên tần số kênh được cấp phát  với mức suy hao của bộ lọc máy thu trên (các) kênh lân cận.
3

### Giới hạn

UE phải đáp ứng yêu cầu tối thiểu quy định trong Bảng 5 đối với tất cả các giá trị của nhiễu kênh lân cận lên đến -25 dBm. Tuy nhiên, không thể đo trực tiếp ACS,
thay vào đó, dải thông số đo kiểm dưới và trên được chọn trong Bảng 5 có thông lượng phải ≥ 95 % thông lượng tối đa của kênh đo tham chiếu xác định tại A.3.2  của ETSI TS 136 521-1.
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Bảng 5 - Tham số đo cho độ chọn lọc kênh lân cận</th>
<th>Col2</th>
<th>Col3</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Tham số đo ACS1**</td>
<td>**Tham số đo ACS1**</td>
<td>**Tham số đo ACS1**</td>
</tr>
<tr>
<td>Nhiễu</td>
<td>**GSM (GMSK)**</td>
<td>**E-UTRA**</td>
</tr>
<tr>
<td>Công suất tín hiệu NB<br>(Pwanted) / dBm</td>
<td>REFSENS + 14 dB</td>
<td>REFSENS + 14 dB</td>
</tr>
<tr>
<td>Công suất tín hiệu nhiễu<br>(PInterferer) / dBm</td>
<td>REFSENS + 42 dB</td>
<td>REFSENS + 47 dB</td>
</tr>
<tr>
<td>Băng thông nhiễu</td>
<td>200 kHz</td>
<td>5 MHz</td>
</tr>
<tr>
<td>Độ lệch nhiễu từ biên kênh NB</td>
<td>±200 kHz</td>
<td>±2,5 MHz</td>
</tr>
<tr>
<td>**Tham số đo ACS2**</td>
<td>**Tham số đo ACS2**</td>
<td>**Tham số đo ACS2**</td>
</tr>
<tr>
<td>Nhiễu</td>
<td>**GSM (GMSK)**</td>
<td>**E-UTRA**</td>
</tr>
<tr>
<td>Công suất tín hiệu NB<br>(Pwanted) / dBm</td>
<td>-53 dBm</td>
<td>-58 dBm</td>
</tr>
<tr>
<td>Công suất tín hiệu nhiễu<br>(PInterferer) / dBm</td>
<td>-25 dBm</td>
<td>-25 dBm</td>
</tr>
<tr>
<td>Băng thông nhiễu</td>
<td>200 kHz</td>
<td>5 MHz</td>
</tr>
<tr>
<td>Độ lệch nhiễu từ biên kênh NB</td>
<td>±200 kHz</td>
<td>±2,5 MHz</td>
</tr>
</tbody>
</table>
|---|---|---| |**Tham số đo ACS1**|**Tham số đo ACS1**|**Tham số đo ACS1**| |Nhiễu|**GSM (GMSK)**|**E-UTRA**| |Công suất tín hiệu NB<br>(Pwanted) / dBm|REFSENS + 14 dB|REFSENS + 14 dB| |Công suất tín hiệu nhiễu<br>(PInterferer) / dBm|REFSENS + 42 dB|REFSENS + 47 dB| |Băng thông nhiễu|200 kHz|5 MHz| |Độ lệch nhiễu từ biên kênh NB|±200 kHz|±2,5 MHz| |**Tham số đo ACS2**|**Tham số đo ACS2**|**Tham số đo ACS2**| |Nhiễu|**GSM (GMSK)**|**E-UTRA**| |Công suất tín hiệu NB<br>(Pwanted) / dBm|-53 dBm|-58 dBm| |Công suất tín hiệu nhiễu<br>(PInterferer) / dBm|-25 dBm|-25 dBm| |Băng thông nhiễu|200 kHz|5 MHz| |Độ lệch nhiễu từ biên kênh NB|±200 kHz|±2,5 MHz|

## Đặc tính chặn của máy thu

### Định nghĩa

Đặc tính chặn là một tham số đánh giá khả năng của máy thu thu được tín hiệu mong muốn tại tần số kênh được cấp phát khi có sự hiện diện của nhiễu không mong muốn trên các tần số khác với các tần số đáp ứng giả này hoặc các tần số kênh lân cận, mà không có tín hiệu vào không mong muốn này gây ra sự suy giảm   4       chỉ tiêu của máy thu vượt quá giới hạn quy định. Chỉ tiêu chặn áp dụng đối với tất cả các tần số ngoại trừ các tần số xảy ra đáp ứng giả.

### Giới hạn

Với các tham số xác định tại Bảng 6, thông lượng phải ≥ 95 % thông lượng tối đa của các kênh đo kiểm tham chiếu theo quy định tại A.2.2, A.2.3 và A.3.2, tài liệu ETSI TS 136 521-1 (với một mặt động OCNG Pattern OP.1 FDD/TDD đối với tín  hiệu DL như mô tả tại A.5.1.1/A.5.2.1, tài liệu ETSI TS 136 521-1).
Với các tham số xác định tại Bảng 7, thông lượng phải ≥ 95 % thông lượng tối đa của các kênh đo kiểm tham chiếu theo quy định tại A.2.2, A.2.3 và A.3.2, tài liệu ETSI TS 136 521-1 (với một mặt động OCNG Pattern OP.1 FDD/TDD đối với tín  hiệu DL như mô tả tại A.5.1.1/A.5.2.1, tài liệu ETSI TS 136 521-1), ngoại trừ các tần số đáp ứng giả.
Đối với Bảng 7 trong các dải tần số 1, 2 và 3 tới max (24,6[N RB /6]) các ngoại lệ được phép đối với các tần số đáp ứng giả trong mỗi kênh tần số được cấp phát khi đo sử dụng kích thước bước 1 MHz, với N RB là số lượng khối tài nguyên trong cấu hình băng thông truyền dẫn đường xuống. Đối với các ngoại lệ, các yêu cầu quy  định tại 2.7 được áp dụng.

### Bảng 6 - Các tham số chặn trong băng

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Tham số đo IBB1</th>
<th>Col2</th>
</tr>
</thead>
<tbody>
<tr>
<td>Công suất tín hiệu NB<br>(Pwanted) / dBm</td>
<td>REFSENS + 6 dB</td>
</tr>
<tr>
<td>Nhiễu</td>
<td>E-UTRA</td>
</tr>
<tr>
<td>Công suất tín hiệu nhiễu<br>(PInterferer) / dBm</td>
<td>- 56 dBm</td>
</tr>
<tr>
<td>Băng thông nhiễu</td>
<td>5 MHz</td>
</tr>
<tr>
<td>Độ lệch nhiễu từ biên kênh NB</td>
<td>+7,5 MHz + 0,005 MHz<br>và<br>-7,5 MHz - 0,005 MHz</td>
</tr>
<tr>
<td>**Tham số đo IBB2**</td>
<td>**Tham số đo IBB2**</td>
</tr>
<tr>
<td>Công suất tín hiệu NB<br>(Pwanted) / dBm</td>
<td>REFSENS + 6 dB</td>
</tr>
<tr>
<td>Nhiễu</td>
<td>E-UTRA</td>
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
<th>Công suấ t tín hiệu nhiễ u<br>(P Interferer) / dBm</th>
<th>44 dBm<br>-</th>
</tr>
</thead>
<tbody>
<tr>
<td>Băng thông nhiễu</td>
<td>5 MHz</td>
</tr>
<tr>
<td>Độ lệch nhiễu từ biên kênh NB</td>
<td>từ +12,5 MHz đến FDL_high+ 15 MHz và<br>từ -12,5 MHz đến FDL_low - 15 MHz</td>
</tr>
</tbody>
</table>
|---|---| |Công suất tín hiệu NB<br>(Pwanted) / dBm|REFSENS + 6 dB| |Nhiễu|E-UTRA| |Công suất tín hiệu nhiễu<br>(PInterferer) / dBm|- 56 dBm| |Băng thông nhiễu|5 MHz| |Độ lệch nhiễu từ biên kênh NB|+7,5 MHz + 0,005 MHz<br>và<br>-7,5 MHz - 0,005 MHz| |**Tham số đo IBB2**|**Tham số đo IBB2**| |Công suất tín hiệu NB<br>(Pwanted) / dBm|REFSENS + 6 dB| |Nhiễu|E-UTRA|    5           |---|---| |Băng thông nhiễu|5 MHz| |Độ lệch nhiễu từ biên kênh NB|từ +12,5 MHz đến FDL_high+ 15 MHz và<br>từ -12,5 MHz đến FDL_low - 15 MHz|

### Bảng 7 - Các tham số chặn ngoài băng

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
<th>Tham số</th>
<th>Đơn vị</th>
<th>Tầ số<br>n</th>
<th>Col4</th>
<th>Col5</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Tham số**</td>
<td>**Đơn vị**</td>
<td>**Dải 1**</td>
<td>**Dải 2**</td>
<td>**Dải 3**</td>
</tr>
<tr>
<td>Pwanted</td>
<td>dBm</td>
<td>REFSENS + 6 dB</td>
<td>REFSENS + 6 dB</td>
<td>REFSENS + 6 dB</td>
</tr>
<tr>
<td>Pinterferer<br>(CW)</td>
<td>dBm</td>
<td>-44</td>
<td>-30</td>
<td>-15</td>
</tr>
<tr>
<td>Dải Finterferer</td>
<td>MHz</td>
<td>FDL_low - 15 đến<br>FDL_low - 60</td>
<td>FDL_low - 60 đến<br>FDL_low - 85</td>
<td>FDL_low - 85 đến 1<br>MHz</td>
</tr>
<tr>
<td>Dải Finterferer</td>
<td>MHz</td>
<td>FDL_high + 15 đến<br>FDL_high + 60</td>
<td>FDL_high + 60 đến<br>FDL_high + 85</td>
<td>FDL_high + 85 đến 12<br>750 MHz</td>
</tr>
<tr>
<td>CHÚ THÍCH 1: Đối với dải tần số đường xuống 729 MHz < f < 1 GHz trong băng tần<br>hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải điều<br>chỉnh tới -18 dBm tại dải tần số bị giới hạn bởi FDL_low - 150 MHz của<br>băng tần nhỏ nhất UE hỗ trợ trong dải tần số 729 MHz < f < 1 GHz và<br>FDL_high + 150 MHz của băng tần lớn nhất UE hỗ trợ trong dải tần số<br>729 MHz < f < 1 GHz.<br>CHÚ THÍCH 2: Đối với dải tần số đường xuống 1 805 MHz < f < 2 200 MHz trong<br>băng tần hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải<br>điều chỉnh tới -20 dBm tại dải tần số bị giới hạn bởi FDL_low - 200 MHz<br>của băng tần nhỏ nhất UE hỗ trợ trong dải tần số 1 805 MHz < f < 2 200<br>MHz and FDL_high + 200 MHz của băng tần lớn nhất UE hỗ trợ trong<br>dải tần số 1 805 MHz < f < 2 200 MHz.</td>
<td>CHÚ THÍCH 1: Đối với dải tần số đường xuống 729 MHz < f < 1 GHz trong băng tần<br>hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải điều<br>chỉnh tới -18 dBm tại dải tần số bị giới hạn bởi FDL_low - 150 MHz của<br>băng tần nhỏ nhất UE hỗ trợ trong dải tần số 729 MHz < f < 1 GHz và<br>FDL_high + 150 MHz của băng tần lớn nhất UE hỗ trợ trong dải tần số<br>729 MHz < f < 1 GHz.<br>CHÚ THÍCH 2: Đối với dải tần số đường xuống 1 805 MHz < f < 2 200 MHz trong<br>băng tần hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải<br>điều chỉnh tới -20 dBm tại dải tần số bị giới hạn bởi FDL_low - 200 MHz<br>của băng tần nhỏ nhất UE hỗ trợ trong dải tần số 1 805 MHz < f < 2 200<br>MHz and FDL_high + 200 MHz của băng tần lớn nhất UE hỗ trợ trong<br>dải tần số 1 805 MHz < f < 2 200 MHz.</td>
<td>CHÚ THÍCH 1: Đối với dải tần số đường xuống 729 MHz < f < 1 GHz trong băng tần<br>hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải điều<br>chỉnh tới -18 dBm tại dải tần số bị giới hạn bởi FDL_low - 150 MHz của<br>băng tần nhỏ nhất UE hỗ trợ trong dải tần số 729 MHz < f < 1 GHz và<br>FDL_high + 150 MHz của băng tần lớn nhất UE hỗ trợ trong dải tần số<br>729 MHz < f < 1 GHz.<br>CHÚ THÍCH 2: Đối với dải tần số đường xuống 1 805 MHz < f < 2 200 MHz trong<br>băng tần hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải<br>điều chỉnh tới -20 dBm tại dải tần số bị giới hạn bởi FDL_low - 200 MHz<br>của băng tần nhỏ nhất UE hỗ trợ trong dải tần số 1 805 MHz < f < 2 200<br>MHz and FDL_high + 200 MHz của băng tần lớn nhất UE hỗ trợ trong<br>dải tần số 1 805 MHz < f < 2 200 MHz.</td>
<td>CHÚ THÍCH 1: Đối với dải tần số đường xuống 729 MHz < f < 1 GHz trong băng tần<br>hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải điều<br>chỉnh tới -18 dBm tại dải tần số bị giới hạn bởi FDL_low - 150 MHz của<br>băng tần nhỏ nhất UE hỗ trợ trong dải tần số 729 MHz < f < 1 GHz và<br>FDL_high + 150 MHz của băng tần lớn nhất UE hỗ trợ trong dải tần số<br>729 MHz < f < 1 GHz.<br>CHÚ THÍCH 2: Đối với dải tần số đường xuống 1 805 MHz < f < 2 200 MHz trong<br>băng tần hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải<br>điều chỉnh tới -20 dBm tại dải tần số bị giới hạn bởi FDL_low - 200 MHz<br>của băng tần nhỏ nhất UE hỗ trợ trong dải tần số 1 805 MHz < f < 2 200<br>MHz and FDL_high + 200 MHz của băng tần lớn nhất UE hỗ trợ trong<br>dải tần số 1 805 MHz < f < 2 200 MHz.</td>
<td>CHÚ THÍCH 1: Đối với dải tần số đường xuống 729 MHz < f < 1 GHz trong băng tần<br>hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải điều<br>chỉnh tới -18 dBm tại dải tần số bị giới hạn bởi FDL_low - 150 MHz của<br>băng tần nhỏ nhất UE hỗ trợ trong dải tần số 729 MHz < f < 1 GHz và<br>FDL_high + 150 MHz của băng tần lớn nhất UE hỗ trợ trong dải tần số<br>729 MHz < f < 1 GHz.<br>CHÚ THÍCH 2: Đối với dải tần số đường xuống 1 805 MHz < f < 2 200 MHz trong<br>băng tần hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải<br>điều chỉnh tới -20 dBm tại dải tần số bị giới hạn bởi FDL_low - 200 MHz<br>của băng tần nhỏ nhất UE hỗ trợ trong dải tần số 1 805 MHz < f < 2 200<br>MHz and FDL_high + 200 MHz của băng tần lớn nhất UE hỗ trợ trong<br>dải tần số 1 805 MHz < f < 2 200 MHz.</td>
</tr>
</tbody>
</table>
|---|---|---|---|---| |**Tham số**|**Đơn vị**|**Dải 1**|**Dải 2**|**Dải 3**| |Pwanted|dBm|REFSENS + 6 dB|REFSENS + 6 dB|REFSENS + 6 dB| |Pinterferer<br>(CW)|dBm|-44|-30|-15| |Dải Finterferer|MHz|FDL_low - 15 đến<br>FDL_low - 60|FDL_low - 60 đến<br>FDL_low - 85|FDL_low - 85 đến 1<br>MHz| |Dải Finterferer|MHz|FDL_high + 15 đến<br>FDL_high + 60|FDL_high + 60 đến<br>FDL_high + 85|FDL_high + 85 đến 12<br>750 MHz| |CHÚ THÍCH 1: Đối với dải tần số đường xuống 729 MHz < f < 1 GHz trong băng tần<br>hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải điều<br>chỉnh tới -18 dBm tại dải tần số bị giới hạn bởi FDL_low - 150 MHz của<br>băng tần nhỏ nhất UE hỗ trợ trong dải tần số 729 MHz < f < 1 GHz và<br>FDL_high + 150 MHz của băng tần lớn nhất UE hỗ trợ trong dải tần số<br>729 MHz < f < 1 GHz.<br>CHÚ THÍCH 2: Đối với dải tần số đường xuống 1 805 MHz < f < 2 200 MHz trong<br>băng tần hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải<br>điều chỉnh tới -20 dBm tại dải tần số bị giới hạn bởi FDL_low - 200 MHz<br>của băng tần nhỏ nhất UE hỗ trợ trong dải tần số 1 805 MHz < f < 2 200<br>MHz and FDL_high + 200 MHz của băng tần lớn nhất UE hỗ trợ trong<br>dải tần số 1 805 MHz < f < 2 200 MHz.|CHÚ THÍCH 1: Đối với dải tần số đường xuống 729 MHz < f < 1 GHz trong băng tần<br>hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải điều<br>chỉnh tới -18 dBm tại dải tần số bị giới hạn bởi FDL_low - 150 MHz của<br>băng tần nhỏ nhất UE hỗ trợ trong dải tần số 729 MHz < f < 1 GHz và<br>FDL_high + 150 MHz của băng tần lớn nhất UE hỗ trợ trong dải tần số<br>729 MHz < f < 1 GHz.<br>CHÚ THÍCH 2: Đối với dải tần số đường xuống 1 805 MHz < f < 2 200 MHz trong<br>băng tần hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải<br>điều chỉnh tới -20 dBm tại dải tần số bị giới hạn bởi FDL_low - 200 MHz<br>của băng tần nhỏ nhất UE hỗ trợ trong dải tần số 1 805 MHz < f < 2 200<br>MHz and FDL_high + 200 MHz của băng tần lớn nhất UE hỗ trợ trong<br>dải tần số 1 805 MHz < f < 2 200 MHz.|CHÚ THÍCH 1: Đối với dải tần số đường xuống 729 MHz < f < 1 GHz trong băng tần<br>hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải điều<br>chỉnh tới -18 dBm tại dải tần số bị giới hạn bởi FDL_low - 150 MHz của<br>băng tần nhỏ nhất UE hỗ trợ trong dải tần số 729 MHz < f < 1 GHz và<br>FDL_high + 150 MHz của băng tần lớn nhất UE hỗ trợ trong dải tần số<br>729 MHz < f < 1 GHz.<br>CHÚ THÍCH 2: Đối với dải tần số đường xuống 1 805 MHz < f < 2 200 MHz trong<br>băng tần hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải<br>điều chỉnh tới -20 dBm tại dải tần số bị giới hạn bởi FDL_low - 200 MHz<br>của băng tần nhỏ nhất UE hỗ trợ trong dải tần số 1 805 MHz < f < 2 200<br>MHz and FDL_high + 200 MHz của băng tần lớn nhất UE hỗ trợ trong<br>dải tần số 1 805 MHz < f < 2 200 MHz.|CHÚ THÍCH 1: Đối với dải tần số đường xuống 729 MHz < f < 1 GHz trong băng tần<br>hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải điều<br>chỉnh tới -18 dBm tại dải tần số bị giới hạn bởi FDL_low - 150 MHz của<br>băng tần nhỏ nhất UE hỗ trợ trong dải tần số 729 MHz < f < 1 GHz và<br>FDL_high + 150 MHz của băng tần lớn nhất UE hỗ trợ trong dải tần số<br>729 MHz < f < 1 GHz.<br>CHÚ THÍCH 2: Đối với dải tần số đường xuống 1 805 MHz < f < 2 200 MHz trong<br>băng tần hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải<br>điều chỉnh tới -20 dBm tại dải tần số bị giới hạn bởi FDL_low - 200 MHz<br>của băng tần nhỏ nhất UE hỗ trợ trong dải tần số 1 805 MHz < f < 2 200<br>MHz and FDL_high + 200 MHz của băng tần lớn nhất UE hỗ trợ trong<br>dải tần số 1 805 MHz < f < 2 200 MHz.|CHÚ THÍCH 1: Đối với dải tần số đường xuống 729 MHz < f < 1 GHz trong băng tần<br>hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải điều<br>chỉnh tới -18 dBm tại dải tần số bị giới hạn bởi FDL_low - 150 MHz của<br>băng tần nhỏ nhất UE hỗ trợ trong dải tần số 729 MHz < f < 1 GHz và<br>FDL_high + 150 MHz của băng tần lớn nhất UE hỗ trợ trong dải tần số<br>729 MHz < f < 1 GHz.<br>CHÚ THÍCH 2: Đối với dải tần số đường xuống 1 805 MHz < f < 2 200 MHz trong<br>băng tần hoạt động, mức công suất nhiễu (PInterferer) đối với dải 3 sẽ phải<br>điều chỉnh tới -20 dBm tại dải tần số bị giới hạn bởi FDL_low - 200 MHz<br>của băng tần nhỏ nhất UE hỗ trợ trong dải tần số 1 805 MHz < f < 2 200<br>MHz and FDL_high + 200 MHz của băng tần lớn nhất UE hỗ trợ trong<br>dải tần số 1 805 MHz < f < 2 200 MHz.|

## Đáp ứng giả của máy thu

### Định nghĩa

Đáp ứng giả là tham số đánh giá khả năng máy thu thu tín hiệu mong muốn tại tần số kênh được cấp phát của máy thu mà không vượt quá độ suy giảm cho trước do sự hiện diện của một tín hiệu gây nhiễu CW không mong muốn tại bất cứ tần số nào khác, mà tại đó có tồn tại đáp ứng, nghĩa là đối với các tần số đó giới hạn chặn  ngoài băng xác định tại 2.6.2 không được thoả mãn.
6

### Giới hạn

Thông lượng phải ≥ 95 % thông lượng tối đa của các kênh đo kiểm tham chiếu  theo quy định tại A.2.2, A.2.3 và A.3.2, tài liệu ETSI TS 136 521-1 (với một mặt động OCNG Pattern OP.1 FDD/TDD đối với tín hiệu DL như mô tả tại A.5.1.1/A.5.2.1, tài liệu ETSI TS 136 521-1) với các tham số tại Bảng 8.

### Bảng 8 - Đáp ứng giả

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Tham số</th>
<th>Đơn vị</th>
<th>Mức</th>
</tr>
</thead>
<tbody>
<tr>
<td>Psignal</td>
<td>dBm</td>
<td>REFSENS + 6</td>
</tr>
<tr>
<td>Pinterferer (CW)</td>
<td>dBm</td>
<td>-44</td>
</tr>
<tr>
<td>Finterferer</td>
<td>MHz</td>
<td>Các tần số đáp ứng giả</td>
</tr>
<tr>
<td>Số lượng các tần số đáp ứng giả</td>
<td></td>
<td>24 (trong OOB dải 1, 2, 3)</td>
</tr>
<tr>
<td>CHÚ THÍCH 1: Kênh đo tham chiếu xác định tại A.3.2, tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 2: REFSENS được xác định tại tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 3: OOB dải 1, 2, 3 quy định tại Bảng 7.</td>
<td>CHÚ THÍCH 1: Kênh đo tham chiếu xác định tại A.3.2, tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 2: REFSENS được xác định tại tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 3: OOB dải 1, 2, 3 quy định tại Bảng 7.</td>
<td>CHÚ THÍCH 1: Kênh đo tham chiếu xác định tại A.3.2, tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 2: REFSENS được xác định tại tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 3: OOB dải 1, 2, 3 quy định tại Bảng 7.</td>
</tr>
</tbody>
</table>
|---|---|---| |Psignal|dBm|REFSENS + 6| |Pinterferer (CW)|dBm|-44| |Finterferer|MHz|Các tần số đáp ứng giả| |Số lượng các tần số đáp ứng giả||24 (trong OOB dải 1, 2, 3)| |CHÚ THÍCH 1: Kênh đo tham chiếu xác định tại A.3.2, tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 2: REFSENS được xác định tại tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 3: OOB dải 1, 2, 3 quy định tại Bảng 7.|CHÚ THÍCH 1: Kênh đo tham chiếu xác định tại A.3.2, tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 2: REFSENS được xác định tại tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 3: OOB dải 1, 2, 3 quy định tại Bảng 7.|CHÚ THÍCH 1: Kênh đo tham chiếu xác định tại A.3.2, tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 2: REFSENS được xác định tại tài liệu ETSI TS 136 521-1.<br>CHÚ THÍCH 3: OOB dải 1, 2, 3 quy định tại Bảng 7.|

## Đặc tính xuyên điều chế của máy thu

### Định nghĩa

Loại bỏ đáp ứng xuyên điều chế là tham số đánh giá khả năng của máy thu thu một tín hiệu mong muốn tại tần số kênh được cấp phát khi có hai hoặc nhiều tín hiệu gây nhiễu có mối liên quan tần số đặc thù với tín hiệu mong muốn.

### Giới hạn

Thông lượng phải ≥ 95 % thông lượng tối đa của các kênh đo kiểm tham chiếu như  quy định tại A.2.2, A.2.3 và A.3.2, tài liệu ETSI TS 136 521-1 (với một mặt động OCNG Pattern OP.1 FDD/TDD đối với tín hiệu DL như mô tả tại A.5.1.1/A.5.2.1,
tài liệu ETSI TS 136 521-1) với các tham số xác định tại Bảng 9 đối với công suất trung bình tín hiệu mong muốn xác định khi có sự xuất hiện của hai tín hiệu nhiễu.

### Bảng 9 - Các tham số đo cho xuyên điều chế băng rộng

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Các tham số đo xuyên điề u chế băng rộng</th>
<th>Col2</th>
</tr>
</thead>
<tbody>
<tr>
<td>Công suất tín hiệu NB</td>
<td>REFSENS + 12 dB</td>
</tr>
<tr>
<td>Công suất tín hiệu nhiễu CW</td>
<td>-46 dBm</td>
</tr>
<tr>
<td>Công suất tín hiệu nhiễu E-UTRA 1,4 MHz</td>
<td>-46 dBm</td>
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
<th>Độ lệch nhiễ u CW</th>
<th>±2 2 MHz<br>,</th>
</tr>
</thead>
<tbody>
<tr>
<td>Độ lệch nhiễu E-UTRA 1,4 MHz</td>
<td>±4,4 MHz</td>
</tr>
</tbody>
</table>
|---|---| |Công suất tín hiệu NB|REFSENS + 12 dB| |Công suất tín hiệu nhiễu CW|-46 dBm| |Công suất tín hiệu nhiễu E-UTRA 1,4 MHz|-46 dBm|    7       |---|---| |Độ lệch nhiễu E-UTRA 1,4 MHz|±4,4 MHz|

## Phát xạ giả của máy thu

### Định nghĩa

Công suất phát xạ giả là công suất của các phát xạ được tạo ra hoặc được khuếch đại trong máy thu xuất hiện tại đầu nối ăng ten của UE.

### Giới hạn

Công suất phát xạ giả không vượt quá giá trị mức tối đa quy định trong Bảng 11.

### Bảng 10 - Các yêu cầu chung cho phát xạ giả máy thu

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Tầ n số băng</th>
<th>Băng thông đo</th>
<th>Mức tối đa</th>
</tr>
</thead>
<tbody>
<tr>
<td>30 MHz ≤ f 1 GHz</td>
<td>100 kHz</td>
<td>-57 dBm</td>
</tr>
<tr>
<td>1 GHz ≤ f ≤ 12,75 GHz</td>
<td>1 MHz</td>
<td>-47 dBm</td>
</tr>
<tr>
<td>CHÚ THÍCH:<br>Các tài nguyên PDCCH không sử dụng được đệm với các nhóm<br>tài nguyên có mức công suất đưa ra bởi PDCCH_RA/RB như định nghĩa<br>tại C.3.1, tài liệu ETSITS 136 101.</td>
<td>CHÚ THÍCH:<br>Các tài nguyên PDCCH không sử dụng được đệm với các nhóm<br>tài nguyên có mức công suất đưa ra bởi PDCCH_RA/RB như định nghĩa<br>tại C.3.1, tài liệu ETSITS 136 101.</td>
<td>CHÚ THÍCH:<br>Các tài nguyên PDCCH không sử dụng được đệm với các nhóm<br>tài nguyên có mức công suất đưa ra bởi PDCCH_RA/RB như định nghĩa<br>tại C.3.1, tài liệu ETSITS 136 101.</td>
</tr>
</tbody>
</table>
|---|---|---| |30 MHz ≤ f 1 GHz|100 kHz|-57 dBm| |1 GHz ≤ f ≤ 12,75 GHz|1 MHz|-47 dBm| |CHÚ THÍCH:<br>Các tài nguyên PDCCH không sử dụng được đệm với các nhóm<br>tài nguyên có mức công suất đưa ra bởi PDCCH_RA/RB như định nghĩa<br>tại C.3.1, tài liệu ETSITS 136 101.|CHÚ THÍCH:<br>Các tài nguyên PDCCH không sử dụng được đệm với các nhóm<br>tài nguyên có mức công suất đưa ra bởi PDCCH_RA/RB như định nghĩa<br>tại C.3.1, tài liệu ETSITS 136 101.|CHÚ THÍCH:<br>Các tài nguyên PDCCH không sử dụng được đệm với các nhóm<br>tài nguyên có mức công suất đưa ra bởi PDCCH_RA/RB như định nghĩa<br>tại C.3.1, tài liệu ETSITS 136 101.|

## Tỉ số công suất rò kênh lân cận của máy phát

### Định nghĩa

Tỉ số công suất rò kênh lân cận (ACLR) là tỉ số giữa công suất trung bình đã lọc có tâm trên tần số kênh được cấp phát và công suất trung bình đã lọc có tâm trên tần số kênh lân cận.

### Giới hạn

Công suất kênh và công suất kênh lân cận NB được cấp phát đo được với các bộ  lọc và các băng thông đo theo quy định tại Bảng 11.
Nếu công suất kênh lân cận đo được lớn hơn -50 dBm thì GSM ACLR và W CDMA ACLR đo được phải lớn hơn các giới hạn tại Bảng 11 và đáp ứng việc bảo vệ các hệ thống GSM, W-CDMA và E-UTRA.

### Bảng 11 – Yêu cầu đo ACLR cho UE NB

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Col1</th>
<th>GSM<br>ACLR</th>
<th>W CDMA<br>- ACLR</th>
</tr>
</thead>
<tbody>
<tr>
<td>**ACLR**</td>
<td>19,2 dB</td>
<td>36,2 dB</td>
</tr>
<tr>
<td>**Độ lệch tần số trung tâm**<br>**kênh lân cận từ biên kênh**<br>**NB**</td>
<td>±200 kHz</td>
<td>±2,5 MHz</td>
</tr>
<tr>
<td>**Băng thông đo kênh lân**<br>**cận**</td>
<td>180 KHz</td>
<td>3,84 MHz</td>
</tr>
<tr>
<td>**Bộ lọc đo**</td>
<td>Chữ nhật</td>
<td>Bộ lọc RRC α = 0,22</td>
</tr>
<tr>
<td>**Băng thông đo kênh NB**</td>
<td>180 KHz</td>
<td>180 KHz</td>
</tr>
<tr>
<td>**Bộ lọc đo kênh NB**</td>
<td>Chữ nhật</td>
<td>Chữ nhật</td>
</tr>
</tbody>
</table>
8             |---|---|---| |**ACLR**|19,2 dB|36,2 dB| |**Độ lệch tần số trung tâm**<br>**kênh lân cận từ biên kênh**<br>**NB**|±200 kHz|±2,5 MHz| |**Băng thông đo kênh lân**<br>**cận**|180 KHz|3,84 MHz| |**Bộ lọc đo**|Chữ nhật|Bộ lọc RRC α = 0,22| |**Băng thông đo kênh NB**|180 KHz|180 KHz| |**Bộ lọc đo kênh NB**|Chữ nhật|Chữ nhật|

## Độ nhạy tham chiếu của máy thu

Trừ khi có quy định khác, các đặc tính của máy thu được xác định tại các đầu nối ăng ten của UE. Đối với (các) UE chỉ có một ăng ten liền duy nhất, một (nhiều)
ăng ten tham chiếu với độ tăng ích 0 dBi được giả định đối với mỗi cổng ăng ten.

### Định nghĩa

Độ nhạy tham chiếu đánh giá khả năng của UE để nhận dữ liệu với một thông lượng trung bình cho trước đối với kênh đo kiểm tham chiếu xác định, dưới các điều kiện về mức tín hiệu thấp, môi trường truyền sóng lý tưởng và không có tạp  âm.
Một UE không thể đáp ứng thông lượng theo các yêu cầu trên sẽ làm giảm hiệu  quả vùng phủ của một e-NodeB.

### Giới hạn

Thông lượng phải ≥ 95 % thông lượng tối đa của các kênh đo kiểm tham chiếu  theo xác định tại A.3.2.2, tài liệu ETSI TS 136 521-1 (với một mặt động OCNG Pattern OP.1 FDD/TDD đối với tín hiệu DL như mô tả tại A.5.1.1/A.5.2.1, tài liệu ETSI TS 136 521-1) với các tham số xác định trong Bảng 12.

### Bảng 12 – Độ nhạy tham chiếu

9

## Độ nhạy bức xạ tổng máy thu

Yêu cầu kỹ thuật này áp dụng đối với các UE có kích thước lớn hơn hoặc bằng 56 mm và nhỏ hơn hoặc bằng 72 mm.

### Định nghĩa

Độ nhạy bức xạ tổng được định nghĩa như sau:
4π TRS =  1 1 ∮[EIS θ (Ω;f) [+] EIS φ (Ω;f) ~~[]]~~ [ dΩ]  Trong đó, Độ nhạy đẳng hướng hiệu dụng (EIS) được định nghĩa công suất tại đầu ra ăng ten, ví dụ như ngưỡng độ nhạy đạt được tại mỗi phân cực. Ω là góc phương vị, 𝑓 là tần số. θ và φ là góc phân cực trực giao.
4 _π_ TRS ≈  𝑁−1 𝑀−1 1 1 _π_ ∑ 𝑛=0 ∑ 𝑚=0  [ _EIS θ_ (𝜃 𝑛 _,_ 𝜑 𝑚 _;f_ ) [+] _EIS φ_ (𝜃 𝑛 _,_ 𝜑 𝑚 _;f_ ) [] sin 𝜃] [𝑛]   Trong đó, N và M là số lượng các khoảng thời gian lấy mẫu tương ứng với θ và φ.
θ n và φ m là góc đo. Các khoảng thời gian lấy mẫu được quy định tại 4.4 của ETSI  TS 137 544.
TRS có thể được tính toán từ các phép đo môi trường đẳng hướng ba chiều phađinh Rayleigh trong phân bố phương vị và góc ngẩng đồng đều trung bình. Việc tính toán TRS trong trường hợp này dựa trên việc tìm kiếm công suất thấp nhất mà UE nhận được đối với một lượng hữu hạn các tổ hợp trường trong buồng đo tạo ra mức BER tốt hơn mức BER được quy định. Bằng phương pháp hiệu chỉnh hàm chuyển đổi công suất trung bình, có thể nhận được giá trị tuyệt đối của TRS. Công thức sau được sử dụng để tính TRS.
-1    TRS ≈ 2 _N_ [(][∑] Nn=1 ( _C n_ (1- _R n_ ) _P thres,n_ ))
∑ Nn=1 _P ref,n_    Trong đó, P ref,n là hàm chuyển đổi công suất tham chiếu cho ăng ten đo cố định n,
R n là hệ số phản xạ đối với ăng ten đo cố định n, C n là suy hao đường truyền trong cáp kết nối từ máy thu đo đến ăng ten đo cố định n. Các tham số này được tính toán từ phép đo hiệu chuẩn và được quy định tại B.2 của ETSI TS 137 544. P thres,n được tính toán sử dụng công thức sau:
10       ∑ Mm=1 1    M m=1 2    P = thres,n    _thres_  _S_ | _21,n,m_    _M_    _thres_  _21,n,m_ |    thres  Trong đó, S 21,n,m là giá trị thứ m của hàm chuyển đổi đối với ăng ten đo cố định n,
mà đưa ra ngưỡng BER. M là tổng giá trị công suất đo được tại ngưỡng BER đối với mỗi ăng ten đo kiểm cố định.

### Giới hạn

Giá trị trung bình độ nhạy bức xạ tổng đo được của các kênh thấp, trung bình và cao đối với UE cầm tay phải nhỏ hơn giá trị TRS trung bình quy định trong Bảng 13. Việc lấy giá trị trung bình phải được thực hiện theo thang tuyến tính đối với các kết quả TRS cho phía trái và phía phải đầu mô hình. Giới hạn TRS trung bình được thể hiện trong cột “Giá trị trung bình” của Bảng 13.
1 TRS average =10log / [ (10 _[P]_    1 1  [+ ] 10 _[P] [left_low]_ [/10] 10 _[P]_    1 1  [+ ] 10 _[P] [left_mid]_ [/10] 10 _[P]_     [+ ] 10 _[P] [left_high]_ [/10]    1 1  [+] 10 _[P] [right_low]_ [/10] 10 _[P]_    1    1 1  [+ ] 10 _[P] [right_mid]_ [/10] 10 _[P]_    10 _[P] [right_high]_ [/10] [)]]

### Bảng 13 – Giới hạn giá trị TRS tối thiểu

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Băng tầ n hoạt động</th>
<th>Đơn vị</th>
<th><REFI ><br>or</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Băng tần hoạt động**</td>
<td>**Đơn vị**</td>
<td>**Giá trị trung bình**</td>
</tr>
<tr>
<td>1</td>
<td>dBm/10 MHz</td>
<td>-86</td>
</tr>
<tr>
<td>3</td>
<td>dBm/10 MHz</td>
<td>-86</td>
</tr>
<tr>
<td>5</td>
<td>dBm/10 MHz</td>
<td>-86</td>
</tr>
<tr>
<td>8</td>
<td>dBm/10 MHz</td>
<td>-82,5</td>
</tr>
<tr>
<td>28</td>
<td>dBm/10 MHz</td>
<td>-82,5</td>
</tr>
<tr>
<td>CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.</td>
<td>CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.</td>
<td>CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.</td>
</tr>
</tbody>
</table>
|---|---|---| |**Băng tần hoạt động**|**Đơn vị**|**Giá trị trung bình**| |1|dBm/10 MHz|-86| |3|dBm/10 MHz|-86| |5|dBm/10 MHz|-86| |8|dBm/10 MHz|-82,5| |28|dBm/10 MHz|-82,5| |CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.|CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.|CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.|    CHÚ THÍCH: Yêu cầu tối thiểu TRS áp dụng cho thiết bị có kích thước lớn hơn hoặc bằng 56 mm và nhỏ hơn hoặc bằng 72 mm được định nghĩa  trong ETSI TR 125 914.
11

## Công suất bức xạ tổng

Yêu cầu kỹ thuật này áp dụng đối với các UE có kích thước lớn hơn hoặc bằng 56 mm và nhỏ hơn hoặc bằng 72 mm.

### Định nghĩa

Công suất bức xạ tổng (TRP) là phép đo mức công suất UE thực tế bức xạ ra. TRP được định nghĩa là tích phân của công suất được truyền theo các hướng khác nhau trên toàn bộ mặt cầu bức xạ:
TRP = _4П [1]_ [∮(] _[EIRP] [θ]_ [(][Ω;] _[f]_ [)][+] _[EIRP] [φ]_ [(][Ω;] _[f]_ [))][ dΩ ]  Trong đó: Ω là góc phương vị, f là tần số.
θ và φ là góc phân cực trực giao.
EIRP θ và EIRP φ là mức công suất thực được truyền theo các phân cực   tương ứng.
Do đó:
_N-1_    _M-1_    _Π_ TRP ≈ _2NM_ [∑∑[] _[EIRP] [θ]_ [(] _[θ] [n] [,φ] [m] [;f]_ [)] _[+ EIRP] [φ]_ [(] _[θ] [n] [,φ] [m] [;f]_ [)]] _[sin]_    _θ n_    _n=0_    _m=0_    Trong đó, N và M là số lượng các khoảng thời gian lấy mẫu tương ứng với θ và φ.
𝜃 𝑛 và 𝜑 𝑚 là góc đo. Các khoảng thời gian lấy mẫu được quy định tại 4.4 của ETSI  TS 137 544.
TRP có thể được tính toán từ các mẫu pha-đinh Rayleigh của công suất tổng phát ra từ UE. Phép đo công suất máy phát trong môi trường đẳng hướng pha-đinh Rayleigh dựa trên việc lấy mẫu công suất bức xạ của UE đối với một lượng hữu hạn tổ hợp trường trong buồng đo. Giá trị trung bình của các mẫu được thống kê phân bố tương ứng với TRP và bằng phương pháp hiệu chỉnh hàm chuyển đổi công suất trung bình, từ đó tính thu được giá trị tuyệt đối của TRP.
Do đó:
TRP ≈    ∑ _Nn_ =1 ~~(~~ _C n_ ( _P_ 1- _n R n_ ) [)]  ∑ _Nn_ =1 _P ref,n_    Trong đó, P ref,n là hàm chuyển đổi công suất tham chiếu cho ăng ten đo cố định n,
R n là hệ số phản xạ đối với ăng ten đo cố định n, C n là suy hao đường truyền trong cáp kết nối từ máy thu đo đến ăng ten đo cố định n. Các tham số này được tính toán từ phép đo hiệu chuẩn và được quy định tại B.2 của ETSI TS 137 544. P n là   12       giá trị công suất trung bình được đo bởi ăng ten cố định n và được tính toán bằng  công thức sau:
Pn =    2  ∑ _Mm_ =1 | _S 21,n,m_ |   _M_    Trong đó S 21,n,m là số mẫu thứ m của hàm chuyển đổi số phức được đo bởi ăng ten đo cố định n và M là tổng số mẫu đo cho mỗi ăng ten đo cố định.
CHÚ THÍCH: Tất cả các giá trị trung bình phải được thực hiện bằng cách sử dụng giá trị công suất tuyến tính (ví dụ: các phép đo tính bằng W).

### Giới hạn

Giá trị trung bình công suất bức xạ tổng đo được của các kênh thấp, trung bình và cao tại vị trí bên cạnh đầu phải lớn hơn giá trị quy định trong Bảng 14. Việc lấy giá trị trung bình phải được thực hiện theo thang tuyến tính đối với các kết quả TRP cho phía trái và phía phải đầu giả.
[10] _[P] [left_high]_ [/10] [+10] _[P] [right_low]_ [/10] [+10] _[P] [right_mid]_ [/10] [+10] _[P] [right_high]_ [/10] TRP average =10log 6 [ [10] _[P] [left_low]_ [/10] [+10] _[P] [left_mid]_ [/10] [+] ]

### Bảng 14 – Giới hạn giá trị TRP tối thiểu

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Băng tầ n hoạt<br>động</th>
<th>Đơn vị</th>
<th>Công suấ t loại 3</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Băng tần hoạt**<br>**động**</td>
<td>**Đơn vị**</td>
<td>**Công suất trung bình (dBm)**</td>
</tr>
<tr>
<td>1</td>
<td>dBm/10 MHz</td>
<td>10,9</td>
</tr>
<tr>
<td>3</td>
<td>dBm/10 MHz</td>
<td>10,9</td>
</tr>
<tr>
<td>5</td>
<td>dBm/10 MHz</td>
<td>10,9</td>
</tr>
<tr>
<td>8</td>
<td>dBm/10 MHz</td>
<td>7,6</td>
</tr>
<tr>
<td>28</td>
<td>dBm/10 MHz</td>
<td>7,6</td>
</tr>
<tr>
<td>CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.</td>
<td>CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.</td>
<td>CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.</td>
</tr>
</tbody>
</table>
|---|---|---| |**Băng tần hoạt**<br>**động**|**Đơn vị**|**Công suất trung bình (dBm)**| |1|dBm/10 MHz|10,9| |3|dBm/10 MHz|10,9| |5|dBm/10 MHz|10,9| |8|dBm/10 MHz|7,6| |28|dBm/10 MHz|7,6| |CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.|CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.|CHÚ THÍCH:<br>Không áp dụng cho sóng mang kết hợp.|   CHÚ THÍCH: Yêu cầu tối thiểu TRS được áp dụng đối với UE có kích thước lớn hơn hoặc bằng 56 mm và nhỏ hơn hoặc bằng 72 mm được định  nghĩa trong ETSI TR 125 914.
13

## Phát xạ bức xạ

### Định nghĩa

Chỉ tiêu này đánh giá khả năng hạn chế các phát xạ không mong muốn từ cổng vỏ của thiết bị thông tin vô tuyến và thiết bị phụ trợ.
Chỉ tiêu này áp dụng cho thiết bị thông tin vô tuyến và thiết bị phụ trợ.
Phép đo chỉ tiêu này phải được thực hiện trên thiết bị thông tin vô tuyến và/hoặc trên cấu hình tiêu biểu của thiết bị phụ trợ.

### Giới hạn

Biên tần số và các băng thông tham chiếu đối với những chuyển tiếp chi tiết của các giới hạn giữa các yêu cầu đối với các phát xạ ngoài băng và các yêu cầu đối với các phát xạ giả được dựa trên các khuyến nghị SM.329-12 và SM.1539-1 của  ITU-R.
Các yêu cầu trong Bảng 16 chỉ áp dụng đối với các tần số trong miền phát xạ giả.

### Bảng 15 - Các yêu cầu đối với phát xạ giả bức xạ

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Tầ số<br>n</th>
<th>Yê u cầ u tối thiể u đối với<br>(e r p)/băng thông tham<br>. .<br>chiế u ở chế độ rỗi</th>
<th>Yê u cầ u tối thiể u đối với<br>(e r p)/băng thông tham<br>. .<br>chiế u ở chế độ lưu lượng</th>
</tr>
</thead>
<tbody>
<tr>
<td>30 MHz ≤ f < 1 000 MHz</td>
<td>-57 dBm/100 kHz</td>
<td>-36 dBm/100 kHz</td>
</tr>
<tr>
<td>1 GHz ≤ f < 12,75 GHz</td>
<td>-47 dBm/1 MHz</td>
<td>-30 dBm/1 MHz</td>
</tr>
</tbody>
</table>
|---|---|---| |30 MHz ≤ f < 1 000 MHz|-57 dBm/100 kHz|-36 dBm/100 kHz| |1 GHz ≤ f < 12,75 GHz|-47 dBm/1 MHz|-30 dBm/1 MHz|

## Chức năng điều khiển và giám sát

### Định nghĩa

Yêu cầu này xác minh rằng các chức năng điều khiển và giám sát của UE ngăn UE  phát trong trường hợp không có mạng hợp lệ.
Chỉ tiêu này có thể áp dụng được cho thiết bị thông tin vô tuyến và thiết bị phụ trợ.
Phép đo chỉ tiêu này phải được thực hiện trên thiết bị thông tin vô tuyến và/hoặc trên cấu hình tiêu biểu của thiết bị phụ trợ.

### Giới hạn

Công suất cực đại đo được trong khoảng thời gian đo kiểm không được vượt quá  -30 dBm.
14