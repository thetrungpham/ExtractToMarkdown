# Public_368

# Kích cỡ khối để thử luồng PDH

Kích cỡ khối để thử luồng PDH trong hệ thống đang khai thác được cho trong Bảng 6.

### Bảng 6 - Kích cỡ khối PDH

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Tố c độ bit của l uồ ng<br>PDH kbit/ s</th>
<th>Kích cỡ khối PDH bit</th>
<th>EDC/không có EDC</th>
</tr>
</thead>
<tbody>
<tr>
<td>2048<br>8448<br>34368<br>139264</td>
<td>2048<br>4224<br>4296<br>17408</td>
<td>CRC-4<br>Không có EDC<br>Không có EDC<br>Không có EDC</td>
</tr>
</tbody>
</table>
|---|---|---| |2048<br>8448<br>34368<br>139264|2048<br>4224<br>4296<br>17408|CRC-4<br>Không có EDC<br>Không có EDC<br>Không có EDC|

# Các bất bình thường (Anomatics)

Hai trạng thái bất bình thường trong hệ thống đang khai thác được sử dụng để xác định chỉ   tiêu lỗi bit của luồng PDH.
a 1 : Một tín hiệu đồng bộ khung bị lỗi (an errored frame alignment signal).
a 2 : Một khối bị lỗi (EB) được chỉ thị bằng mã phát hiện lỗi (EDC).

# Các sai hỏng

Ba trạng thái sai hỏng của tín hiệu lối vào trong hệ thống đang khai thác được sử dụng để   xác định chỉ tiêu lỗi bit của luồng PDH.
d 1 : Mất khung (Loss of frame).
d 2 : Tín hiệu chỉ thị cảnh báo (Alarm Indication Signal).
d 3 : Mất đồng bộ khung (Loss of frame alignment).

# Các kiểu luồng PDH

Tùy theo thiết bị thử ISM liên quan đối với luồng PDH sẽ có 4 loại cấu trúc luồng như sau:
  * Kiểu 1: Luồng được cấu trúc bởi khung và khối   Một tập hợp đầy đủ chỉ thị sai hỏng d 1, d 2, d 3 và các chỉ thị bất bình thường a 1, a 2 do   thiết bị kiểm tra cung cấp khi hệ thống đang khai thác (ISM).
    * Kiểu 2: Luồng được cấu trúc bởi khung   Một tập hợp đầy đủ chỉ thị sai hỏng d 1, d 2, d 3 và bất bình thường a 1 do thiết bị kiểm   tra cung cấp khi hệ thống đang khai thác.
    * Kiểu 3: Các luồng được cấu trúc khung khác   Một loạt các giới hạn của chỉ thị sai hỏng d 1, d 2 và bất bình thường a 1 do thiết bị kiểm   tra cung cấp khi hệ thống đang khai thác. Ngoài ra ISM còn chỉ thị cả số lượng chuỗi   tín hiệu đồng bộ khung bị lỗi trong mỗi giây.
    * Kiểu 4: Các luồng không định dạng khung   Một loạt các giới hạn của chỉ thị sai hỏng d 1, d 2 do thiết bị kiểm tra cung cấp khi hệ   thống đang khai thác.

# Các thông số và tiêu chuẩn đo luồng PDH

### Bảng 7 - Các thông số và tiêu chuẩn đo

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Kiể luồ<br>u ng</th>
<th>Các thông số</th>
<th>Tiê u chuẩ n đo</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>ESR</td>
<td>Một giây bị lỗi quan sát được khi trong một<br>giây ít nhất có một bất bình thường a1 hoặc a2<br>hoặc một sai hỏng d1 đến d3 xảy ra.</td>
</tr>
<tr>
<td>1</td>
<td>SESR</td>
<td>Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây ít nhất có ‘x’ bất bình thường a1<br>hoặc a2, hoặc một sai hỏng d1 đến d3 xảy ra.</td>
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
<th>Col1</th>
<th>BBER</th>
<th>Một lỗi khối cơ bản quan sát được khi : một bấ t<br>bình thường a1 h oặc a2 xảy ra trong một khối<br>nhưng không th uộc phầ n giây bị lỗi nghiêm<br>trọng<br>.</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>ESR</td>
<td>Một giây bị lỗi quan sát được khi trong một<br>giây ít nhất có một bất bình thường a1 hoặc một<br>sai hỏng d1 đến d3 xảy ra</td>
</tr>
<tr>
<td>2</td>
<td>SESR</td>
<td>Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây ít nhất có ‘x’ bất bình thường a1<br>hoặc một sai hỏng d1 hoặc d2 xảy ra.</td>
</tr>
<tr>
<td>3</td>
<td>ESR</td>
<td>Một giây bị lỗi quan sát được khi trong một<br>giây ít nhất có một bất bình thường a1 hoặc một<br>sai hỏng d1 hoặc d2 xảy ra.</td>
</tr>
<tr>
<td>3</td>
<td>SESR</td>
<td>Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây có ít nhất ‘x’ bất bình thường a1<br>hoặc một sai hỏng d1 hoặc d2 xảy ra</td>
</tr>
<tr>
<td>4</td>
<td>4</td>
<td>Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây ít nhất có một sai hỏng d1 hoặc<br>d2 xảy ra.</td>
</tr>
</tbody>
</table>
|---|---|---| |1|ESR|Một giây bị lỗi quan sát được khi trong một<br>giây ít nhất có một bất bình thường a1 hoặc a2<br>hoặc một sai hỏng d1 đến d3 xảy ra.| |1|SESR|Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây ít nhất có ‘x’ bất bình thường a1<br>hoặc a2, hoặc một sai hỏng d1 đến d3 xảy ra.|            |---|---|---| |2|ESR|Một giây bị lỗi quan sát được khi trong một<br>giây ít nhất có một bất bình thường a1 hoặc một<br>sai hỏng d1 đến d3 xảy ra| |2|SESR|Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây ít nhất có ‘x’ bất bình thường a1<br>hoặc một sai hỏng d1 hoặc d2 xảy ra.| |3|ESR|Một giây bị lỗi quan sát được khi trong một<br>giây ít nhất có một bất bình thường a1 hoặc một<br>sai hỏng d1 hoặc d2 xảy ra.| |3|SESR|Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây có ít nhất ‘x’ bất bình thường a1<br>hoặc một sai hỏng d1 hoặc d2 xảy ra| |4|4|Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây ít nhất có một sai hỏng d1 hoặc<br>d2 xảy ra.|

# Tiêu chuẩn cho việc phát hiện một giây bị lỗi nghiêm trọng trong luồng PDH

Bảng 8 liệt kê giá trị ‘x’ gây ra một giây bị lỗi nghiêm trọng (SES) trong khi kiểm tra hệ   thống đang khai thác.

### Bảng 8 - Tiêu chuẩn có SES trên các tuyến PDH

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Tố độ bit (kbit/ s)<br>c</th>
<th>2 048</th>
</tr>
</thead>
<tbody>
<tr>
<td>Kiểu EDC</td>
<td>CRC-4</td>
</tr>
<tr>
<td>Số khối/1 giây</td>
<td>1 000</td>
</tr>
<tr>
<td>Số bit/1 khối</td>
<td>2 048</td>
</tr>
<tr>
<td>Ngưỡng SES trước Khuyến nghị G.826</td>
<td>x = 805</td>
</tr>
<tr>
<td>Ngưỡng ISM dựa trên SES của Khuyến<br>nghị G.826</td>
<td>x = 30% khối bị lỗi</td>
</tr>
</tbody>
</table>
|---|---| |Kiểu EDC|CRC-4| |Số khối/1 giây|1 000| |Số bit/1 khối|2 048| |Ngưỡng SES trước Khuyến nghị G.826|x = 805| |Ngưỡng ISM dựa trên SES của Khuyến<br>nghị G.826|x = 30% khối bị lỗi|