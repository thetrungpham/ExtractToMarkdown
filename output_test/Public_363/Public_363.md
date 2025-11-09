# Public_363

# Khái quát

Định vị di động có thể thực hiện bởi một số nguyên lý kỹ thuật, chẳng hạn như   [kỹ thuật tìm điểm giao thoa tín hiệu vô tuyến giữa (một số) tháp thu phát sóng di động](https://en.wikipedia.org/wiki/Cell_tower)
[của mạng và máy điện thoại hoặc đơn giản bằng cách sử dụng dữ liệu của hệ thống](https://en.wikipedia.org/wiki/Cellular_network)
[vệ tinh dẫn đường toàn cầu GNSS [23].](https://en.wikipedia.org/wiki/GNSS)
Để định vị điện thoại di động bằng cách tìm điểm giao thoa tín hiệu vô tuyến   di động, điện thoại đó phải phát ra ít nhất tín hiệu nhàn rỗi (tín hiệu chờ - Idle) để liên   [lạc với các cột ăng ten gần đó và không yêu cầu kích hoạt một cuộc gọi. Hệ thống](https://en.wikipedia.org/wiki/GSM)
[điện thoại di động toàn cầu GSM thực hiện kết nối điện thoại di động với mạng dựa](https://en.wikipedia.org/wiki/GSM)
trên cường độ tín hiệu của điện thoại tới các cột ăng ten gần đó [26].
[Kỹ thuật định vị có thể được sử dụng cho các dịch vụ dựa trên vị trí (LBS) [30,](https://en.wikipedia.org/wiki/Location-based_service)
[31] và khi đó sẽ tiết lộ tọa độ thực của điện thoại di động. Các công ty viễn thông di](https://en.wikipedia.org/wiki/Telecommunication)
[động sử dụng kỹ thuật này để xác định vị trí gần đúng của điện thoại di động và cả](https://en.wikipedia.org/wiki/Approximate)
người dùng của nó.

# Tổng quan các nguyên lý kỹ thuật định vị di động

Vị trí của thiết bị di động (điện thoại di động) có thể được xác định theo các   nguyên lý kỹ thuật cụ thể sau đây [23 -33]:

## Kỹ thuật định vị dựa trên mạng (Network-Based)

Vị trí của điện thoại di động có thể được xác định trên cơ sở hạ tầng mạng của   nhà cung cấp dịch vụ. Ưu điểm của các kỹ thuật dựa trên mạng là chúng có thể được   thực hiện mà không ảnh hưởng đến thiết bị cầm tay (tức không xâm phạm/ảnh hưởng   đến người dùng). Các kỹ thuật dựa trên mạng đã được phát triển nhiều năm trước khi   GPS trên thiết bị cầm tay được phổ biến rộng rãi.
Kỹ thuật định vị của một điện thoại di động dựa trên việc đo mức công suất và   [các phần tử ăng-ten, đồng thời sử dụng nguyên lý một điện thoại di động được cấp](https://en.wikipedia.org/wiki/Antenna_pattern)
[nguồn luôn giao tiếp vô tuyến với một trong những trạm gốc (BTS/eNB) gần nhất.](https://en.wikipedia.org/wiki/Base_station)
Do đó, các hiểu biết về vị trí của trạm gốc gợi ý rằng điện thoại di động cần định vị   đang ở gần trạm gốc đó.
Các hệ thống tiên tiến xác định khu vực mà điện thoại di động ở đó và ước tính   gần đúng khoảng cách đến trạm gốc. Xác định khoảng cách gần đúng được tính toán   [bằng phép nội suy tín hiệu giữa các cột ăng ten liền kề. Các dịch vụ đủ tiêu chuẩn có](https://en.wikipedia.org/wiki/Interpolating)
[thể đạt được độ chính xác đến 50 mét ở các khu vực đô thị nơi lưu lượng truy cập di](https://en.wikipedia.org/wiki/Urban_area)
[động và mật độ các cột ăng ten (trạm gốc) đủ cao. Tại các khu vực nông thôn và](https://en.wikipedia.org/wiki/Rural)
hoang vắng, do các trạm gốc có thể cách nhau hàng km nên việc xác định vị trí của   [điện thoại di động sẽ kém chính xác hơn. Định vị GSM sử dụng kỹ thuật giao thoa](https://en.wikipedia.org/wiki/Global_System_for_Mobile_Communications)
tín hiệu vô tuyến để xác định vị trí của điện thoại di động GSM hoặc sử dụng thiết bị   theo dõi chuyên dụng.
Độ chính xác của các kỹ thuật dựa trên mạng là khác nhau. Trong đó kỹ thuật   dựa trên nhận dạng tế bào (Cell-ID) là kém chính xác nhất (do có tín hiệu can nhiễu   chuyển đổi giữa các tháp di động, hay còn gọi là "tín hiệu phản xạ/dội ngược"); kỹ   thuật đo tam giác có độ chính xác vừa phải và kỹ thuật đo tam giác tín hiệu đường   lên tiên tiến bằng định thời gian là mới hơn và có độ chính xác cao nhất. Độ chính   xác của các kỹ thuật dựa trên mạng đều phụ thuộc vào mật độ của các trạm gốc tế   bào. Trong đó, môi trường đô thị thường đạt được độ chính xác cao nhất có thể do có   [số lượng tháp phát sóng nhiều hơn và sử dụng kỹ thuật định vị bằng phương pháp](https://en.wikipedia.org/wiki/Cell_tower)
định thời gian tiên tiến nhất.
Một trong những thách thức chính của các kỹ thuật dựa trên mạng là yêu cầu   sự hợp tác chặt chẽ với nhà cung cấp dịch vụ (nhà mạng), nó đòi hỏi phải lắp đặt phần   cứng và cài đặt phần mềm trong cơ sở hạ tầng của nhà điều hành mạng di động. Thông   thường, việc đặt phần cứng và phần mềm trong cơ sở hạ tầng của nhà mạng phải được   pháp luật của nước đó cho phép. Chẳng hạn như qui định của Mỹ trong bộ luật cho   dịch vụ cấp cứu, cứu hộ, cứu nạn E911 buộc nhà mạng di động phải triển khai giải   pháp kỹ thuật cung cấp khả năng định vị cho E911 trước khi cung cấp dịch vụ di động   [25].

## Kỹ thuật định vị dựa trên thiết bị cầm tay (Handset Based)

[Vị trí của điện thoại di động có thể được xác định bằng cách sử dụng phần](https://en.wikipedia.org/wiki/Client_software)
[mềm khách được cài đặt trên máy điện thoại cầm tay. Kỹ thuật này xác định vị trí của](https://en.wikipedia.org/wiki/Client_software)
thiết bị cầm tay bằng cách tính toán vị trí của tế bào di động và cường độ tín hiệu của   các tế bào nhà và lân cận mà liên tục được gửi từ thiết bị cầm tay đến nhà cung cấp   [dịch vụ. Ngoài ra, nếu điện thoại cầm tay được trang bị GPS thì có thể lấy được thông](https://en.wikipedia.org/wiki/GPS)
tin vị trí chính xác hơn do vị trí GPS của máy cầm tay có thể được gửi đến nhà cung   cấp dịch vụ. Một cách tiếp cận khác là sử dụng kỹ thuật dựa trên dấu vân tay, trong   đó "chữ ký" của tế bào nhà và tế bào lân cận báo hiệu cường độ tín hiệu tại các điểm   khác nhau trong khu vực quan tâm được ghi lại và khớp trong thời gian thực để xác   định vị trí của thiết bị cầm tay. Kỹ thuật này thường được thực hiện độc lập với nhà   cung cấp dịch vụ.
Nhược điểm chính của các kỹ thuật dựa trên thiết bị cầm tay là sự cần thiết   phải cài đặt phần mềm trên thiết bị. Nó đòi hỏi sự hợp tác tích cực, chặt chẽ của người   [sử dụng thuê bao di động cũng như phần mềm cài đặt phải có khả năng xử lý các hệ](https://en.wikipedia.org/wiki/Operating_system)
[điều hành khác nhau của thiết bị cầm tay mà nó liên tục được thay đổi. Nhưng điều](https://en.wikipedia.org/wiki/Operating_system)
này là khó khả thi vì đối tượng của CQAN thường là đối tượng giấu mặt, khó tiếp cận   hoặc chúng ở nước ngoài. Thông thường, chẳng hạn như điện thoại thông minh sẽ có   thể cài đặt và chạy phần mềm định vị đó cũng như cài đặt, chạy các phần mềm bản   đồ số như Google Maps để phục vụ kỹ thuật định vị dựa trên máy cầm tay.
[Một giải pháp được đề xuất là cài đặt phần cứng hoặc phần mềm nhúng trên](https://en.wikipedia.org/wiki/Embedded_system)
[thiết bị cầm tay, ví dụ phần mềm sử dụng kỹ thuật định vị bằng cách tính toán Chênh](https://en.wikipedia.org/wiki/Enhanced_Observed_Time_Difference)
[lệch thời gian quan sát nâng cao (E-OTD). Qua khảo sát, nghiên cứu, sẽ nhận thấy](https://en.wikipedia.org/wiki/Enhanced_Observed_Time_Difference)
phương pháp này không đạt được bước tiến đáng kể, do khó có thể thuyết phục các   nhà sản xuất điện thoại di động khác nhau hợp tác trên một cơ chế chung và chi phí   sản xuất điện thoại di động sẽ tăng cao. Một khó khăn khác là phải giải quyết vấn đề   kỹ thuật của các thiết bị cầm tay nước ngoài đang chuyển vùng trong mạng của nhà   cung

## Kỹ thuật định vị dựa trên SIM

[Sử dụng mô-đun nhận dạng thuê bao di động (SIM) trong thiết bị cầm tay](https://en.wikipedia.org/wiki/Subscriber_identity_module)
[GSM và UMTS, có thể thu được các phép đo vô tuyến thô từ thiết bị cầm tay. Các](https://en.wikipedia.org/wiki/GSM)
[phép đo khả dụng bao gồm: Cell-ID đang phục vụ, thời gian phản hồi và cường độ](https://en.wikipedia.org/wiki/Cell_ID)
tín hiệu. Loại thông tin thu được qua SIM có thể khác với loại thông tin có sẵn từ điện   thoại. Ví dụ: có thể không trực tiếp lấy được bất kỳ phép đo thô nào từ thiết bị cầm   tay nhưng vẫn nhận được các phép đo thông qua SIM.

## Kỹ thuật định vị dựa trên Wi-Fi

[Dữ liệu Wi-Fi từ nguồn dữ liệu Wifi cộng đồng cũng có thể được sử dụng để](https://en.wikipedia.org/wiki/Crowdsourcing)
xác định vị trí của thiết bị cầm tay. Hiệu suất kém của các kỹ thuật định vị dựa trên   GPS trong môi trường trong nhà (do tín hiệu thu GPS từ vệ tinh sẽ yếu, không đủ cả   ba vệ tinh cần thiết hoặc không thể thu được khi thiết bị cầm tay có gắn GPS ở trong   nhà) và sự phổ biến ngày càng tăng của Wi-Fi đã khuyến khích các viện nghiên cứu,
các công ty thiết kế các phương pháp mới và khả thi để thực hiện định vị điện thoại di   động hoặc thiết bị di động trong nhà dựa trên Wi-Fi.
[Hầu hết các điện thoại thông minh đều tích hợp modul lấy dữ liệu từ Hệ thống](https://en.wikipedia.org/wiki/Smartphone)
[vệ tinh dẫn đường toàn cầu (GNSS), chẳng hạn như GPS của Mỹ, GLONASS của](https://en.wikipedia.org/wiki/Satellite_navigation)
[Nga, Galileo của Châu Âu, Beidou của Trung Quốc với hệ thống định vị Wifi.](https://en.wikipedia.org/wiki/GLONASS)

## Nguyên lý kỹ thuật lai ghép (hỗn hợp)

[Hệ thống định vị lai ghép sử dụng kết hợp các kỹ thuật dựa trên mạng và dựa](https://en.wikipedia.org/wiki/Hybrid_positioning_system)
trên thiết bị cầm tay để xác định vị trí. Một ví dụ là phương pháp sử dụng một số chế   [độ của GPS có hỗ trợ (A-GPS), có thể sử dụng cả dữ liệu GPS và thông tin mạng để](https://en.wikipedia.org/wiki/Assisted_GPS)
tính toán vị trí của thiết bị cầm tay. Cả hai loại dữ liệu này đều được điện thoại sử   dụng để làm cho vị trí chính xác hơn (tức là kỹ thuật A-GPS). Ngoài ra, kỹ thuật định   vị lai ghép bằng cách theo dõi cả hai hệ thống cũng có thể thực hiện bằng cách để   [điện thoại thu được vị trí GPS của nó trực tiếp từ vệ tinh, sau đó nó gửi thông tin qua](https://en.wikipedia.org/wiki/Satellite)
mạng tới người đang muốn xác định vị trí của điện thoại.
Các hệ thống sử dụng kỹ thuật định vị lai ghép điển hình bao gồm: dịch vụ   [định vị của Google Maps, kỹ thuật OTDoA và E-CellID của mạng 4G-LTE. Ngoài](https://en.wikipedia.org/wiki/OTDOA)
ra còn có các hệ thống định vị kết hợp một số phương pháp tiếp cận/xác định vị trí   [khác nhau để định vị thiết bị di động bằng Wi-Fi, WiMAX, GSM, 4G-LTE, địa chỉ](https://en.wikipedia.org/wiki/Wi-Fi)
[IP và dữ liệu môi trường mạng, trong đó có dữ liệu đa phương tiện mà thiết bị di động](https://en.wikipedia.org/wiki/IP_address)
đã và đang sử dụng trên môi trường mạng đó.
Phương pháp định vị này có thể được gọi là phương pháp lai ghép tiên tiến, nó   kết hợp được cả các dịch vụ định vị dựa trên vị trí thông thường (LBS) và dịch vụ   định vị dựa trên đa phương tiện của vị trí (LBM).

## Tổng hợp các kỹ thuật định vị

Trong bảng dưới đây, luận án tổng hợp một số nguyên lý kỹ thuật, thuật toán   định vị khả dụng làm cơ sở tính toán, lựa chọn giải pháp kỹ thuật định vị theo mục   tiêu đặt ra. Bảng tổng hợp này được tham khảo từ các nguồn tài liệu [23-45].
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>TT</th>
<th>Kỹ th uật</th>
<th>Môtả/Đị nh nghĩa/Khái niệm</th>
<th>Th uật toán/ Côngthức<br>tínhtoán cơbản</th>
</tr>
</thead>
<tbody>
<tr>
<td>**I.**<br>**Dựa trên mạng**</td>
<td>**I.**<br>**Dựa trên mạng**</td>
<td>**I.**<br>**Dựa trên mạng**</td>
<td>**I.**<br>**Dựa trên mạng**</td>
</tr>
<tr>
<td>Định vị dựa trên thông tin tính toán của mạng di động</td>
<td>Định vị dựa trên thông tin tính toán của mạng di động</td>
<td>Định vị dựa trên thông tin tính toán của mạng di động</td>
<td>Định vị dựa trên thông tin tính toán của mạng di động</td>
</tr>
<tr>
<td>1</td>
<td>Multilateration<br>(MLAT)</td>
<td>Kỹ thuật đo đa phương hay còn<br>gọi là kỹ thuật định vị hyperbolic,<br>là kỹ thuật tính toán vị trí của thiết<br>bị trên cơ sở đo thời gian đến<br>(ToA) thiết bị của sóng vô tuyến<br>được phát từ nhiều trạm gốc.<br>Do đã biết dạng sóng, tốc độ và<br>địa điểm các trạm gốc, nên sẽ tính<br>được vị trí của thiết bị cần định vị.</td>
<td>ToAs (thời điểm đến) =<br>ToFs (thời gian bay) +<br>ToT (thời điểm phát).</td>
</tr>
<tr>
<td>2</td>
<td>Triangulation</td>
<td>Kỹ thuật đo tam giác để tính toán<br>vị trí của thiết bị bằng cách vẽ các<br>đường cắt thành hình tam giác từ<br>các điểm phát sóng đã biết (các<br>BTS/eNB) đến thiết bị (còn gọi là<br>kỹ thuật đo tam giác đường xuống<br>tiên tiến).</td>
<td>Các thuật toán tính toán<br>tam giác đạc.</td>
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
<th>II Dựa trên máy cầ m tay<br>.</th>
<th>Col2</th>
<th>Col3</th>
<th>Col4</th>
</tr>
</thead>
<tbody>
<tr>
<td>Định vị dựa trên phần mềm khách<br>cài đặt trên máy cầm tay, ví dụ<br>phần mềm ứng dụng vị trí GPS<br>trên máy điện thoại thông minh.<br>Kỹ thuật này xác định vị trí của<br>thiết bị cầm tay bởi các tham số<br>nhận dạng tế bào Cell-ID của<br>mạng di động phục vụ nó, cường<br>độ tín hiệu của các tế bào nhà và<br>lân cận, liên tục được gửi đến nhà<br>cung cấp dịch vụ. Một cách tiếp<br>cận khác là dựa trên “dấu vân<br>tay”, trong đó “chữ ký” của Cell<br>nhà và Cell lân cận báo hiệu<br>cường độ tín hiệu tại điểm quan<br>tâm khác nhau, được ghi lại và<br>khớp với thời gian thực để tính<br>toán vị trí của máy cầm tay.<br>(Phương pháp này độc lập với nhà<br>cung cấp dịch vụ, thường được sử<br>dụng trong các thiết bị định vị cơ<br>động).</td>
<td>- Các thuật toán tính toán<br>tọa độ địa lý trên cơ sở tín<br>hiệu GPS từ vệ tinh đến<br>máy cầm tay.<br>- Thuật toán tính chênh<br>lệch thời gian quan sát<br>nâng cao E-OTD. Thuật<br>toán tính chênh lệch thời<br>gian đến của đường lên<br>U-TDoA.</td>
</tr>
<tr>
<td>**III.**<br>**Dựa trên SIM**</td>
<td>**III.**<br>**Dựa trên SIM**</td>
<td>**III.**<br>**Dựa trên SIM**</td>
<td>**III.**<br>**Dựa trên SIM**</td>
</tr>
<tr>
<td>Đo các tham số vô tuyến từ máy<br>cầm tay bằng cách sử dụng SIM<br>của nó. Các tham số đo được là<br>Cell-ID đang phục vụ, thời gian<br>phản hồi và cường độ tín hiệu. Từ<br>đó tính toán được vị trí của máy<br>cầm tay.</td>
<td>Các thuật toán tính toán<br>giữa tham số Cell, thời<br>gian phản hồi và cường<br>độ tín hiệu.</td>
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
<th>IV Dựa trên Wifi<br>.</th>
<th>Col2</th>
<th>Col3</th>
<th>Col4</th>
</tr>
</thead>
<tbody>
<tr>
<td>Xác định vị trí của thiết bị cầm tay<br>bằng cách lấy dữ liệu Wi-Fi<br>nguồn cộng đồng</td>
</tr>
<tr>
<td>1</td>
<td>Signal strength<br>based<br>(AP-RSSI)</td>
<td>Kỹ thuật ghi lại cường độ tín hiệu<br>RSSI từ một số điểm truy cập<br>trong phạm vi máy cầm tay để<br>tính toán vị trí máy cầm tay.</td>
<td>Sử dụng các thuật toán<br>đo tam giác như mô tả ở<br>trên.</td>
</tr>
<tr>
<td>2</td>
<td>Fingerprinting<br>based</td>
<td>Kỹ thuật ghi lại cường độ tín hiệu<br>RSSI từ một số điểm truy cập vào<br>cơ sở dữ liệu, lấy một tọa độ đã<br>biết của thiết bị khách trong giai<br>đoạn ngoại tuyến, ước tính được<br>vị trí gần đúng nhất khi nó trực<br>tuyến.</td>
<td>Các thuật toán đo tam<br>giác và các thuật toán<br>ước lượng.</td>
</tr>
<tr>
<td>3</td>
<td>Angle of arrival<br>based (AoA)</td>
<td>Kỹ thuật ước tính góc đến<br>(AoA) của tín hiệu đa đường<br>nhận được tại các mảng ăng-ten<br>trong các điểm truy cập và áp<br>dụng phương pháp đo tam giác để<br>tính toán vị trí của các thiết bị<br>khách.</td>
<td>Thuật toán Music.</td>
</tr>
<tr>
<td>4</td>
<td>Time of flight<br>based (ToF)</td>
<td>Kỹ thuật lấy dấu thời gian được<br>cung cấp bởi các giao diện không<br>dây để tính toán ToF của tín hiệu<br>và sau đó sử dụng thông tin này<br>để ước tính khoảng cách và vị trí<br>tương đối của một thiết bị khách<br>đối với các điểm truy cập.</td>
<td>- Thuật toán đo tam giác<br>- Thuật toán đo thời gian</td>
</tr>
<tr>
<td>**V.**<br>**Lai ghép tiên tiến**</td>
<td>**V.**<br>**Lai ghép tiên tiến**</td>
<td>**V.**<br>**Lai ghép tiên tiến**</td>
<td>**V.**<br>**Lai ghép tiên tiến**</td>
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
<th>1</th>
<th>A GNSS<br>-<br>(A GPS)<br>-</th>
<th>Kỹ th uật đị nh vị toàn cầ u có hỗ<br>để tínhtoánvịtrímáycầ<br>trợ mtay<br>,<br>từ cả thông ti n tọa độ GPS và<br>thông ti n mạng (điện th oại có<br>được vị trí GPS của nó trực tiế p<br>từ vệ ti nh và sau đó gửi thông ti n<br>tới người đ đị nh vị<br>qua mạng ang<br>điện th oại đó)<br>.</th>
<th>-Th uật toán của Googl e<br>Maps<br>.<br>-Th uật toán OTDoA và<br>E -CellID của mạng 4G<br>LTE<br>.</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>Kết hợp</td>
<td>Kỹ thuật kết hợp một số phương<br>pháp tiếp cận vị trí khác nhau để<br>định vị thiết bị di động bằng Wi-<br>Fi, WiMAX, GSM, LTE, địa chỉ<br>IP và dữ liệu môi trường mạng.</td>
<td>Nhiều thuật toán của các<br>kỹ thuật trên kết hợp với<br>nhau để định vị hoặc dùng<br>mỗi thuật toán tùy theo dữ<br>liệu vào khả dụng.</td>
</tr>
</tbody>
</table>
**Bảng 1. 1** . Tổng hợp các kỹ thuật định vị di động               |---|---|---|---| |**I.**<br>**Dựa trên mạng**|**I.**<br>**Dựa trên mạng**|**I.**<br>**Dựa trên mạng**|**I.**<br>**Dựa trên mạng**| |Định vị dựa trên thông tin tính toán của mạng di động|Định vị dựa trên thông tin tính toán của mạng di động|Định vị dựa trên thông tin tính toán của mạng di động|Định vị dựa trên thông tin tính toán của mạng di động| |1|Multilateration<br>(MLAT)|Kỹ thuật đo đa phương hay còn<br>gọi là kỹ thuật định vị hyperbolic,<br>là kỹ thuật tính toán vị trí của thiết<br>bị trên cơ sở đo thời gian đến<br>(ToA) thiết bị của sóng vô tuyến<br>được phát từ nhiều trạm gốc.<br>Do đã biết dạng sóng, tốc độ và<br>địa điểm các trạm gốc, nên sẽ tính<br>được vị trí của thiết bị cần định vị.|ToAs (thời điểm đến) =<br>ToFs (thời gian bay) +<br>ToT (thời điểm phát).| |2|Triangulation|Kỹ thuật đo tam giác để tính toán<br>vị trí của thiết bị bằng cách vẽ các<br>đường cắt thành hình tam giác từ<br>các điểm phát sóng đã biết (các<br>BTS/eNB) đến thiết bị (còn gọi là<br>kỹ thuật đo tam giác đường xuống<br>tiên tiến).|Các thuật toán tính toán<br>tam giác đạc.|    5          |---|---|---|---| |||Định vị dựa trên phần mềm khách<br>cài đặt trên máy cầm tay, ví dụ<br>phần mềm ứng dụng vị trí GPS<br>trên máy điện thoại thông minh.<br>Kỹ thuật này xác định vị trí của<br>thiết bị cầm tay bởi các tham số<br>nhận dạng tế bào Cell-ID của<br>mạng di động phục vụ nó, cường<br>độ tín hiệu của các tế bào nhà và<br>lân cận, liên tục được gửi đến nhà<br>cung cấp dịch vụ. Một cách tiếp<br>cận khác là dựa trên “dấu vân<br>tay”, trong đó “chữ ký” của Cell<br>nhà và Cell lân cận báo hiệu<br>cường độ tín hiệu tại điểm quan<br>tâm khác nhau, được ghi lại và<br>khớp với thời gian thực để tính<br>toán vị trí của máy cầm tay.<br>(Phương pháp này độc lập với nhà<br>cung cấp dịch vụ, thường được sử<br>dụng trong các thiết bị định vị cơ<br>động).|- Các thuật toán tính toán<br>tọa độ địa lý trên cơ sở tín<br>hiệu GPS từ vệ tinh đến<br>máy cầm tay.<br>- Thuật toán tính chênh<br>lệch thời gian quan sát<br>nâng cao E-OTD. Thuật<br>toán tính chênh lệch thời<br>gian đến của đường lên<br>U-TDoA.| |**III.**<br>**Dựa trên SIM**|**III.**<br>**Dựa trên SIM**|**III.**<br>**Dựa trên SIM**|**III.**<br>**Dựa trên SIM**| |||Đo các tham số vô tuyến từ máy<br>cầm tay bằng cách sử dụng SIM<br>của nó. Các tham số đo được là<br>Cell-ID đang phục vụ, thời gian<br>phản hồi và cường độ tín hiệu. Từ<br>đó tính toán được vị trí của máy<br>cầm tay.|Các thuật toán tính toán<br>giữa tham số Cell, thời<br>gian phản hồi và cường<br>độ tín hiệu.|    6                |---|---|---|---| |||Xác định vị trí của thiết bị cầm tay<br>bằng cách lấy dữ liệu Wi-Fi<br>nguồn cộng đồng|| |1|Signal strength<br>based<br>(AP-RSSI)|Kỹ thuật ghi lại cường độ tín hiệu<br>RSSI từ một số điểm truy cập<br>trong phạm vi máy cầm tay để<br>tính toán vị trí máy cầm tay.|Sử dụng các thuật toán<br>đo tam giác như mô tả ở<br>trên.| |2|Fingerprinting<br>based|Kỹ thuật ghi lại cường độ tín hiệu<br>RSSI từ một số điểm truy cập vào<br>cơ sở dữ liệu, lấy một tọa độ đã<br>biết của thiết bị khách trong giai<br>đoạn ngoại tuyến, ước tính được<br>vị trí gần đúng nhất khi nó trực<br>tuyến.|Các thuật toán đo tam<br>giác và các thuật toán<br>ước lượng.| |3|Angle of arrival<br>based (AoA)|Kỹ thuật ước tính góc đến<br>(AoA) của tín hiệu đa đường<br>nhận được tại các mảng ăng-ten<br>trong các điểm truy cập và áp<br>dụng phương pháp đo tam giác để<br>tính toán vị trí của các thiết bị<br>khách.|Thuật toán Music.| |4|Time of flight<br>based (ToF)|Kỹ thuật lấy dấu thời gian được<br>cung cấp bởi các giao diện không<br>dây để tính toán ToF của tín hiệu<br>và sau đó sử dụng thông tin này<br>để ước tính khoảng cách và vị trí<br>tương đối của một thiết bị khách<br>đối với các điểm truy cập.|- Thuật toán đo tam giác<br>- Thuật toán đo thời gian| |**V.**<br>**Lai ghép tiên tiến**|**V.**<br>**Lai ghép tiên tiến**|**V.**<br>**Lai ghép tiên tiến**|**V.**<br>**Lai ghép tiên tiến**|    7            |---|---|---|---| |2|Kết hợp|Kỹ thuật kết hợp một số phương<br>pháp tiếp cận vị trí khác nhau để<br>định vị thiết bị di động bằng Wi-<br>Fi, WiMAX, GSM, LTE, địa chỉ<br>IP và dữ liệu môi trường mạng.|Nhiều thuật toán của các<br>kỹ thuật trên kết hợp với<br>nhau để định vị hoặc dùng<br>mỗi thuật toán tùy theo dữ<br>liệu vào khả dụng.|    8