# Public_300

## **1. GIỚI THIỆU** **1.1 Mục đích**

VTP bổ sung đối tượng bưu tá thuê ngoài vào đội ngũ giao nhận để đảm bảo đủ nguồn lực vận hành → Phát triển chính sách lương khoán riêng cho đối tượng này → Hệ thống tính lương khoán cần điều chỉnh để đáp ứng việc tính lương cho những đối tượng bưu tá khác nhau.

## **1.2 Phạm vi**

Hệ thống SCS, FICO

## **1.3 Danh mục khái niệm, từ viết tắt** **1.4 Tài liệu liên quan**

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>#</th>
<th>Tàiliệu</th>
<th>Ngườitạo</th>
<th>Ngàycập nhật</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Phụ lục lỗi</td>
<td>NhungPAC</td>
<td>22/03/2024</td>
</tr>
<tr>
<td>2</td>
<td>Phụ lục phân quyền</td>
<td>NhungPAC</td>
<td>22/03/2024</td>
</tr>
<tr>
<td>3</td>
<td>QLNVVP-2393 Tính lương cho bưu tá thuê ngoài (Bản chốt)</td>
<td>NhungPAC</td>
<td>15/11/2023</td>
</tr>
</tbody>
</table>
|---|---|---|---| |1|Phụ lục lỗi|NhungPAC|22/03/2024| |2|Phụ lục phân quyền|NhungPAC|22/03/2024| |3|QLNVVP-2393 Tính lương cho bưu tá thuê ngoài (Bản chốt)|NhungPAC|15/11/2023|

## **1.5 Tóm tắt tài liệu** **2. ĐẶC TẢ YÊU CẦU** **2.1 Yêu cầu chức năng** **2.1.1 Đặc tả use case:**

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
<th>#</th>
<th>Nhóm</th>
<th>UCID</th>
<th>Use Case</th>
<th>Priority</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Kỳ lương</td>
<td>UC1.1</td>
<td>Tra cứu kỳ lương</td>
<td>High</td>
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
<th>Col1</th>
<th>Col2</th>
<th>UC1 2<br>.</th>
<th>Tạo kỳ lương</th>
<th>Hi gh</th>
</tr>
</thead>
<tbody>
<tr>
<td>UC1.3</td>
<td>Chỉnh sửa kỳ lương</td>
<td>Low</td>
</tr>
<tr>
<td>UC1.4</td>
<td>Xóa kỳ lương</td>
<td>Low</td>
</tr>
<tr>
<td>2</td>
<td>Dữ liệu đầu vào</td>
<td>UC2.1</td>
<td>Lấy dữ liệu đầu vào</td>
<td>High</td>
</tr>
<tr>
<td>2</td>
<td>Dữ liệu đầu vào</td>
<td>UC2.2</td>
<td>Xuất dữ liệu đầu vào</td>
<td>Medium</td>
</tr>
<tr>
<td>3</td>
<td>Bảng chi</td>
<td>UC3.1</td>
<td>Tra cứu bảng chi</td>
<td>High</td>
</tr>
<tr>
<td>3</td>
<td>Bảng chi</td>
<td>UC3.2</td>
<td>Tạo bảng chi</td>
<td>High</td>
</tr>
<tr>
<td>3</td>
<td>Bảng chi</td>
<td>UC3.3</td>
<td>Chỉnh sửa bảng chi</td>
<td>Low</td>
</tr>
<tr>
<td>3</td>
<td>Bảng chi</td>
<td>UC3.4</td>
<td>Xóa bảng chi</td>
<td>Low</td>
</tr>
<tr>
<td>3</td>
<td>Bảng chi</td>
<td>UC3.5</td>
<td>Yêu cầu chi</td>
<td>High</td>
</tr>
<tr>
<td>4</td>
<td>Biên bản</td>
<td>UC4.1</td>
<td>Tổng hợp biên bản</td>
<td>High</td>
</tr>
<tr>
<td>4</td>
<td>Biên bản</td>
<td>UC4.2</td>
<td>Xem danh sách biên bản</td>
<td>High</td>
</tr>
<tr>
<td>4</td>
<td>Biên bản</td>
<td>UC4.3</td>
<td>Loại/Bỏ loại biên bản</td>
<td>High</td>
</tr>
<tr>
<td>4</td>
<td>Biên bản</td>
<td>UC4.5</td>
<td>Theo dõi tiến độ chi lương</td>
<td>Low</td>
</tr>
</tbody>
</table>
|---|---|---|---|---| |1|Kỳ lương|UC1.1|Tra cứu kỳ lương|High|    1          |---|---|---|---|---| |||UC1.3|Chỉnh sửa kỳ lương|Low| |||UC1.4|Xóa kỳ lương|Low| |2|Dữ liệu đầu vào|UC2.1|Lấy dữ liệu đầu vào|High| |2|Dữ liệu đầu vào|UC2.2|Xuất dữ liệu đầu vào|Medium| |3|Bảng chi|UC3.1|Tra cứu bảng chi|High| |3|Bảng chi|UC3.2|Tạo bảng chi|High| |3|Bảng chi|UC3.3|Chỉnh sửa bảng chi|Low| |3|Bảng chi|UC3.4|Xóa bảng chi|Low| |3|Bảng chi|UC3.5|Yêu cầu chi|High| |4|Biên bản|UC4.1|Tổng hợp biên bản|High| |4|Biên bản|UC4.2|Xem danh sách biên bản|High| |4|Biên bản|UC4.3|Loại/Bỏ loại biên bản|High| |4|Biên bản|UC4.5|Theo dõi tiến độ chi lương|Low|    2

#### Kỳ lương:

#### UC1.1 - Tra cứu kỳ lương

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Use Case</th>
<th>Tra cứu kỳ lương</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Use Case ID**</td>
<td>UC1.1</td>
</tr>
<tr>
<td>**Description**</td>
<td>Cho phép người dùng tìm kiếm danh sách các kỳ lương đã tạo theo bộ lọc tự thiết lập để sử dụng.</td>
</tr>
<tr>
<td>**Actor(s)**</td>
<td>SCS, TTVH, TCLĐ</td>
</tr>
<tr>
<td>**Priority**</td>
<td>High</td>
</tr>
<tr>
<td>**Trigger**</td>
<td>Người dùng truy cập vào SCS → Hợp đồng thuê khoán → Quản lý kỳ lương.</td>
</tr>
<tr>
<td>**Pre-Condition(s)**</td>
<td>•<br>Người dùng đăng nhập thành công vào web SCS.<br>•<br>Người dùng đang ở màn hình SCS → Hợp đồng thuê khoán</td>
</tr>
<tr>
<td>**Post-Condition(s)**</td>
<td>Người dùng chọn thành công 1 kỳ lương để sử dụng.</td>
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
<th>Main Flow</th>
<th>(1)SCS hiể nthị giaodiệntracứukỳlươngvàthiế tlậpbộlọcmặcđịnh<br>.<br>(2)SCS tìmkiế mtheobộlọcđãthiế tlập<br>.<br>(3) Yes - Tìm kiế m thành công .<br>(4)SCS hiể nthị kế tquảtìmkiế m<br>.<br>(5) Yes - Kế t quả tìm kiế m có bao gồ m kỳ lương người dùng muố n sử dụng .<br>(6)Ngườidùngchọnkỳlươngvàchọnbutton"Sửdụng"<br>.<br>(7)Hệthố ngđónggiaodiệntracứu +fill tênkỳ lươngmuố nsửdụngvàomụckỳlươngtạitrangchủHợpđồ ngthuê<br>khoán<br>.<br>UseCasehoànthành<br>.</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Alternative Flow**</td>
<td>(5) No - Kết quả tìm kiếm KHÔNG bao gồm kỳ lương người dùng muốn sử dụng.<br>(8) Người dùng thiết lập bộ lọc và chọn tìm kiếm.<br>Use Case tiếp tục ở bước (2).</td>
</tr>
<tr>
<td>**Exception Flow**</td>
<td>(3) No - Tìm kiếm thất bại.<br>(6) Hệ thống báo lỗi tương ứng, tham chiếu phụ lục lỗi.<br>Use Case kết thúc.</td>
</tr>
</tbody>
</table>
|---|---| |**Use Case ID**|UC1.1| |**Description**|Cho phép người dùng tìm kiếm danh sách các kỳ lương đã tạo theo bộ lọc tự thiết lập để sử dụng.| |**Actor(s)**|SCS, TTVH, TCLĐ| |**Priority**|High| |**Trigger**|Người dùng truy cập vào SCS → Hợp đồng thuê khoán → Quản lý kỳ lương.| |**Pre-Condition(s)**|•<br>Người dùng đăng nhập thành công vào web SCS.<br>•<br>Người dùng đang ở màn hình SCS → Hợp đồng thuê khoán| |**Post-Condition(s)**|Người dùng chọn thành công 1 kỳ lương để sử dụng.|    3    |<image_1>|         |---|---| |**Alternative Flow**|(5) No - Kết quả tìm kiếm KHÔNG bao gồm kỳ lương người dùng muốn sử dụng.<br>(8) Người dùng thiết lập bộ lọc và chọn tìm kiếm.<br>Use Case tiếp tục ở bước (2).| |**Exception Flow**|(3) No - Tìm kiếm thất bại.<br>(6) Hệ thống báo lỗi tương ứng, tham chiếu phụ lục lỗi.<br>Use Case kết thúc.|    4    |<image_2>|   |<image_3>|

#### UC1.2 Tạo kỳ lương

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Use Case</th>
<th>Tạo kỳ lương</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Use Case ID**</td>
<td>UC1.2</td>
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
<th>Description</th>
<th>Ch o phép người dùng tạo mới 1 kỳ lương<br>.</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Actor(s)**</td>
<td>SCS, TCLĐ, TTVH</td>
</tr>
<tr>
<td>**Priority**</td>
<td>High</td>
</tr>
<tr>
<td>**Trigger**</td>
<td>Tại pop up quản lý kỳ lương, người dùng chọn "Thêm mới"</td>
</tr>
<tr>
<td>**Pre-Condition(s)**</td>
<td>Người dùng đăng nhập thành công vào web SCS.</td>
</tr>
<tr>
<td>**Post-Condition(s)**</td>
<td>Thông tin kỳ lương mới được lưu thành công vào CSDL.</td>
</tr>
<tr>
<td>**Main Flow**</td>
<td>(1) Hệ thống hiển thị biểu mẫu dưới dạng 1 tab cho người dùng nhập thông tin kỳ lương.<br>(2) Người dùng nhập thông tin.<br>(3) Yes - Người dùng chọn "Ghi lại".<br>(4) Hệ thống kiểm tra điều kiện hợp lệ của dữ liệu.<br>(5) Yes - Thông tin đã nhập là hợp lệ.<br>(7) Yes - Hệ thống tạo mới chu kỳ tính lương và lưu vào CSDL thành công.<br>(8) Hệ thống thông báo cho người dùng rằng chu kỳ tính lương đã được thêm thành công + đóng tab Thêm mới.<br>_Use case hoàn thành._</td>
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
<th>Alternative Flow</th>
<th>(3) No Người dùng đóng form nhập<br>- .<br>(9) Yes Đang nhập dở ít nhấ t 1 trường thông tin<br>- .<br>(10)Hệthố ngyêu cầ ungườidùngxácnhậnhủythôngtinđangnhập dở<br>.<br>(11) No - Người dùng hủy yêu cầ u đóng form .<br>UseCasequayl ạib ước(2)<br>(5) No Thông tin đã nhập không hợp lệ<br>- .<br>(12)Hệthố ngtrảralỗituong ứngchophépngườidùngđiề uchỉnhthôngtinđãnhập (Tham chiế u phụlụclỗi)<br>.<br>UseCasequayl ạib ước(3)</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Exception Flow**</td>
<td>(9) No - Không có trường nào đang nhập dở<br>(13) Đóng form nhập.<br>Use Case kết thúc<br>(11) Yes - Người dùng hủy yêu cầu đóng form.<br>(13) Đóng form nhập.<br>Use Case kết thúc<br>(7) No - Lưu vào CSDL thất bại.<br>(13) Hệ thông trả ra lỗi tương ứng, yêu cầu người dùng thử lại sau. (Tham chiếu phụ lục lỗi)<br>_Use Case kết thúc._</td>
</tr>
</tbody>
</table>
|---|---| |**Use Case ID**|UC1.2|    5          |---|---| |**Actor(s)**|SCS, TCLĐ, TTVH| |**Priority**|High| |**Trigger**|Tại pop up quản lý kỳ lương, người dùng chọn "Thêm mới"| |**Pre-Condition(s)**|Người dùng đăng nhập thành công vào web SCS.| |**Post-Condition(s)**|Thông tin kỳ lương mới được lưu thành công vào CSDL.| |**Main Flow**|(1) Hệ thống hiển thị biểu mẫu dưới dạng 1 tab cho người dùng nhập thông tin kỳ lương.<br>(2) Người dùng nhập thông tin.<br>(3) Yes - Người dùng chọn "Ghi lại".<br>(4) Hệ thống kiểm tra điều kiện hợp lệ của dữ liệu.<br>(5) Yes - Thông tin đã nhập là hợp lệ.<br>(7) Yes - Hệ thống tạo mới chu kỳ tính lương và lưu vào CSDL thành công.<br>(8) Hệ thống thông báo cho người dùng rằng chu kỳ tính lương đã được thêm thành công + đóng tab Thêm mới.<br>_Use case hoàn thành._|    6    |<image_4>|   |<image_5>|         |---|---| |**Exception Flow**|(9) No - Không có trường nào đang nhập dở<br>(13) Đóng form nhập.<br>Use Case kết thúc<br>(11) Yes - Người dùng hủy yêu cầu đóng form.<br>(13) Đóng form nhập.<br>Use Case kết thúc<br>(7) No - Lưu vào CSDL thất bại.<br>(13) Hệ thông trả ra lỗi tương ứng, yêu cầu người dùng thử lại sau. (Tham chiếu phụ lục lỗi)<br>_Use Case kết thúc._|    7    |<image_6>|          8