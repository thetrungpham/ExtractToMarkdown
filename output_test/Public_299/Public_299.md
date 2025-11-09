# Public_299

# Tổng quan

## Mục đích tài liệu

* Tài liệu này được xây dựng nhằm mục đích mô tả thiết kế các chức năng đáp ứng yêu cầu nghiệp vụ đăng ký tuyển dụng cho bưu tá, nhân viên lái xe trên website:
viettelpost.com.vn

## Phạm vi

* Luồng nghiệp vụ được áp dụng cho chức năng đăng ký tuyển dụng trên web:
https://viettelpost.com.vn/

## Thuật ngữ và chữ viết tắt

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Thuật ngữ/Từ viế t tắ t</th>
<th>Định nghĩa</th>
</tr>
</thead>
<tbody>
<tr>
<td>VTP</td>
<td>ViettelPost</td>
</tr>
<tr>
<td>KH</td>
<td>Khách hàng</td>
</tr>
</tbody>
</table>
|---|---| |VTP|ViettelPost| |KH|Khách hàng|

## Danh mục chức năng

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>STT</th>
<th>UC</th>
<th>Ứ ng dụng</th>
<th>Chức năng</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>UC01</td>
<td>App/Web<br>ViettelPost</td>
<td>Xây dựng chức năng đăng ký tuyển dụng trên<br>Website cho đối tượng bưu tá</td>
</tr>
<tr>
<td>2</td>
<td>UC02</td>
<td>Quản lý nhân sự</td>
<td>Báo cáo nhu cầu tuyển dụng</td>
</tr>
</tbody>
</table>
|---|---|---|---| |1|UC01|App/Web<br>ViettelPost|Xây dựng chức năng đăng ký tuyển dụng trên<br>Website cho đối tượng bưu tá| |2|UC02|Quản lý nhân sự|Báo cáo nhu cầu tuyển dụng|

# THIẾT KẾ CHỨC NĂNG

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>2.1 Mô tả chung</th>
<th>Col2</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Description**</td>
<td>Cho phép người dùng đăng ký tuyển dụng trên website:<br>https://viettelpost.com.vn/</td>
</tr>
<tr>
<td>**Actor(s)**</td>
<td>Người dùng, VTP, Hệ thống quản lý nhân sự</td>
</tr>
<tr>
<td>**Pre-**<br>**Condition(s)**</td>
<td>Người dùng vào web: https://viettelpost.com.vn/</td>
</tr>
<tr>
<td>**Trigger**</td>
<td>Người dùng click vào ứng tuyển nhanh trên website:<br>https://viettelpost.com.vn/</td>
</tr>
<tr>
<td>**Main flow**</td>
<td>1.  Người dùng vào web: https://viettelpost.com.vn/</td>
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
<th>Col1</th>
<th>2 Ch ọn ứng tuyể n nh anh<br>.<br>3 Nhập thông ti n ứng tuyể n<br>.<br>4 Cli ck Đăng ký<br>.<br>5 Hiể n thị popup đăng ký thành công<br>.</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Post-**<br>**Condition(s)**</td>
<td>1. Người dùng đăng ký thông tin ứng tuyển thành công<br>2. Dữ liệu người dùng đăng ký đẩy về hệ thống tuyển dụng</td>
</tr>
</tbody>
</table>
|---|---| |**Description**|Cho phép người dùng đăng ký tuyển dụng trên website:<br>https://viettelpost.com.vn/| |**Actor(s)**|Người dùng, VTP, Hệ thống quản lý nhân sự| |**Pre-**<br>**Condition(s)**|Người dùng vào web: https://viettelpost.com.vn/| |**Trigger**|Người dùng click vào ứng tuyển nhanh trên website:<br>https://viettelpost.com.vn/| |**Main flow**|1.  Người dùng vào web: https://viettelpost.com.vn/|    1          |---|---| |**Post-**<br>**Condition(s)**|1. Người dùng đăng ký thông tin ứng tuyển thành công<br>2. Dữ liệu người dùng đăng ký đẩy về hệ thống tuyển dụng|

## Mô tả nghiệp vụ

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
<th>Bước</th>
<th>Nghiệp<br>vụ</th>
<th>Hệ thố ng</th>
<th>Đối<br>tượng</th>
<th>Mô tả</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Vào web<br>viettelpost.co<br>m.vn</td>
<td>VTP</td>
<td>Người<br>dùng</td>
<td>Người dùng vào web<br>viettelpost.com.vn > Chọn ứng<br>tuyển giao hàng</td>
</tr>
<tr>
<td>2</td>
<td>Nhập thông<br>tin</td>
<td>VTP</td>
<td>Người<br>dùng</td>
<td>Người dùng nhập thông tin Họ và<br>tên, Năm sinh, Số điện thoại trên<br>màn tuyển dụng</td>
</tr>
<tr>
<td>3</td>
<td>Chọn vị trí<br>ứng tuyển</td>
<td>VTP</td>
<td>Người<br>dùng</td>
<td>Chọn 1 trong 3 vị trí ứng tuyển:<br>Nhân viên bưu tá, Nhân viên khai<br>thác, Tài xế xe tải</td>
</tr>
<tr>
<td>4</td>
<td>Chọn khu<br>vực ứng<br>tuyển: Tỉnh</td>
<td>VTP</td>
<td>Người<br>dùng</td>
<td>Người dùng chọn khu vực ứng<br>tuyển: Tỉnh</td>
</tr>
<tr>
<td>5</td>
<td>Lấy dữ liệu<br>chi nhánh từ<br>Hệ thống<br>quản lý nhân<br>sự</td>
<td>VTP</td>
<td>Hệ<br>thống</td>
<td>VTP lấy dữ liệu chi nhánh từ Hệ<br>thống quản lý nhân sự:</td>
</tr>
<tr>
<td>6</td>
<td>Trả ra dữ<br>liệu chi<br>nhánh</td>
<td>Hệ thống<br>quản lý nhân<br>sự</td>
<td>Hệ<br>thống</td>
<td>Hệ thống quản lý nhân sự trả dữ<br>liệu chi nhánh cho VTP<br>Dữ liệu chi nhánh: Toàn bộ Chi<br>nhánh bưu chính Viettel</td>
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
<th>7</th>
<th>Hiể thị dữ<br>n<br>liệu chi<br>nhánh</th>
<th>VTP</th>
<th>Hệ<br>thố<br>ng</th>
<th>Hiể n thị dữ liệu tỉnh từ Hệ thố ng<br>quản lý nhân sự trả về</th>
</tr>
</thead>
<tbody>
<tr>
<td>8</td>
<td>Chọn khu<br>vực ứng<br>tuyển: Bưu<br>cục</td>
<td>VTP</td>
<td>Người<br>dùng</td>
<td>Người dùng chọn khu vực ứng<br>tuyển: Bưu cục</td>
</tr>
<tr>
<td>9</td>
<td>Lấy dữ liệu<br>bưu cục từ<br>Hệ thống<br>quản lý nhân<br>sự</td>
<td>VTP</td>
<td>Hệ<br>thống</td>
<td>VTP lấy dữ liệu bưu cục từ Hệ<br>thống quản lý nhân sự</td>
</tr>
<tr>
<td>10</td>
<td>Trả ra dữ<br>liệu bưu cục</td>
<td>Hệ thống<br>quản lý nhân<br>sự</td>
<td>Hệ<br>thống</td>
<td>Hệ thống quản lý nhân sự trả dữ<br>liệu bưu cục cho VTP<br>Dữ liệu bưu cục: Bưu cục, Kho<br>vùng</td>
</tr>
<tr>
<td>11</td>
<td>Hiển thị dữ<br>liệu bưu cục</td>
<td>VTP</td>
<td>Hệ<br>thống</td>
<td>Hiển thị dữ liệu bưu cục từ Hệ<br>thống quản lý nhân sự trả về</td>
</tr>
<tr>
<td>12</td>
<td>Đăng ký</td>
<td>VTP</td>
<td>Người<br>dùng</td>
<td>Người dùng click đăng ký ở trên<br>web viettelpost.com.vn</td>
</tr>
<tr>
<td>13</td>
<td>Đẩy dữ liệu<br>về Hệ thống<br>quản lý nhân<br>sự</td>
<td>VTP</td>
<td>Hệ<br>thống</td>
<td>Đẩy dữ liệu đăng ký ứng tuyển về<br>Hệ thống quản lý nhân sự</td>
</tr>
<tr>
<td>14</td>
<td>Lưu dữ liệu<br>ứng viên</td>
<td>Hệ thống<br>quản lý nhân<br>sự</td>
<td>Hệ<br>thống</td>
<td>Hệ thống Hệ thống quản lý nhân<br>sự lưu dữ liệu ứng viên<br>_(Trong vòng 7 ngày: Cùng thông_<br>_tin cá nhân, cùng vị trí ứng tuyển,_<br>_cùng khu vực ứng tuyển, cùng_<br>_trạng thái chưa xử lý hồ sơ =>_</td>
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
<th>Col3</th>
<th>Col4</th>
<th>Khô ng tiế p nhậ n hồ sơ có cù ng<br>thô ng tin tương tự)</th>
</tr>
</thead>
<tbody>
<tr>
<td>15</td>
<td>Hiển thị<br>danh sách<br>ứng viên</td>
<td>Hệ thống<br>quản lý nhân<br>sự</td>
<td>Hệ<br>thống</td>
<td>Hiển thị danh sách hồ sơ ứng viên<br>được đẩy về từ VTP kèm các<br>trạng thái:<br>•<br>Tạo mới<br>•<br>Đang xử lý<br>•<br>Đạt<br>•<br>Không đạt</td>
</tr>
<tr>
<td>16</td>
<td>Cập nhật<br>trạng thái hồ<br>sơ ứng viên</td>
<td>Hệ thống<br>quản lý nhân<br>sự</td>
<td>Người<br>dùng</td>
<td>Người dùng cập nhật trạng thái hồ<br>sơ ứng viên, chuyển trạng thái hồ<br>sơ trên danh sách ứng viên</td>
</tr>
<tr>
<td>17</td>
<td>Trả kết quả<br>ứng tuyển<br>qua SMS/<br>Mocha</td>
<td>Hệ thống<br>quản lý nhân<br>sự</td>
<td>Hệ<br>thống</td>
<td>Hệ thống gửi thông báo về tiến<br>trình xử lý hồ sơ:<br>•<br>Đang xử lý: Hồ sơ đã được<br>tiếp nhận<br>•<br>Đạt: Hồ sơ ứng tuyển đạt<br>yêu cầu, bộ phận tuyển<br>dụng thực hiện quy trình<br>tuyển dụng thủ công<br>•<br>Không đạt: Hồ sơ bị từ<br>chối, người dùng có thể<br>ứng tuyển lại</td>
</tr>
</tbody>
</table>
|---|---|---|---|---| |1|Vào web<br>viettelpost.co<br>m.vn|VTP|Người<br>dùng|Người dùng vào web<br>viettelpost.com.vn > Chọn ứng<br>tuyển giao hàng| |2|Nhập thông<br>tin|VTP|Người<br>dùng|Người dùng nhập thông tin Họ và<br>tên, Năm sinh, Số điện thoại trên<br>màn tuyển dụng| |3|Chọn vị trí<br>ứng tuyển|VTP|Người<br>dùng|Chọn 1 trong 3 vị trí ứng tuyển:<br>Nhân viên bưu tá, Nhân viên khai<br>thác, Tài xế xe tải| |4|Chọn khu<br>vực ứng<br>tuyển: Tỉnh|VTP|Người<br>dùng|Người dùng chọn khu vực ứng<br>tuyển: Tỉnh| |5|Lấy dữ liệu<br>chi nhánh từ<br>Hệ thống<br>quản lý nhân<br>sự|VTP|Hệ<br>thống|VTP lấy dữ liệu chi nhánh từ Hệ<br>thống quản lý nhân sự:| |6|Trả ra dữ<br>liệu chi<br>nhánh|Hệ thống<br>quản lý nhân<br>sự|Hệ<br>thống|Hệ thống quản lý nhân sự trả dữ<br>liệu chi nhánh cho VTP<br>Dữ liệu chi nhánh: Toàn bộ Chi<br>nhánh bưu chính Viettel|    2                            |---|---|---|---|---| |8|Chọn khu<br>vực ứng<br>tuyển: Bưu<br>cục|VTP|Người<br>dùng|Người dùng chọn khu vực ứng<br>tuyển: Bưu cục| |9|Lấy dữ liệu<br>bưu cục từ<br>Hệ thống<br>quản lý nhân<br>sự|VTP|Hệ<br>thống|VTP lấy dữ liệu bưu cục từ Hệ<br>thống quản lý nhân sự| |10|Trả ra dữ<br>liệu bưu cục|Hệ thống<br>quản lý nhân<br>sự|Hệ<br>thống|Hệ thống quản lý nhân sự trả dữ<br>liệu bưu cục cho VTP<br>Dữ liệu bưu cục: Bưu cục, Kho<br>vùng| |11|Hiển thị dữ<br>liệu bưu cục|VTP|Hệ<br>thống|Hiển thị dữ liệu bưu cục từ Hệ<br>thống quản lý nhân sự trả về| |12|Đăng ký|VTP|Người<br>dùng|Người dùng click đăng ký ở trên<br>web viettelpost.com.vn| |13|Đẩy dữ liệu<br>về Hệ thống<br>quản lý nhân<br>sự|VTP|Hệ<br>thống|Đẩy dữ liệu đăng ký ứng tuyển về<br>Hệ thống quản lý nhân sự| |14|Lưu dữ liệu<br>ứng viên|Hệ thống<br>quản lý nhân<br>sự|Hệ<br>thống|Hệ thống Hệ thống quản lý nhân<br>sự lưu dữ liệu ứng viên<br>_(Trong vòng 7 ngày: Cùng thông_<br>_tin cá nhân, cùng vị trí ứng tuyển,_<br>_cùng khu vực ứng tuyển, cùng_<br>_trạng thái chưa xử lý hồ sơ =>_|    3       |---|---|---|---|---| |15|Hiển thị<br>danh sách<br>ứng viên|Hệ thống<br>quản lý nhân<br>sự|Hệ<br>thống|Hiển thị danh sách hồ sơ ứng viên<br>được đẩy về từ VTP kèm các<br>trạng thái:<br>•<br>Tạo mới<br>•<br>Đang xử lý<br>•<br>Đạt<br>•<br>Không đạt| |16|Cập nhật<br>trạng thái hồ<br>sơ ứng viên|Hệ thống<br>quản lý nhân<br>sự|Người<br>dùng|Người dùng cập nhật trạng thái hồ<br>sơ ứng viên, chuyển trạng thái hồ<br>sơ trên danh sách ứng viên| |17|Trả kết quả<br>ứng tuyển<br>qua SMS/<br>Mocha|Hệ thống<br>quản lý nhân<br>sự|Hệ<br>thống|Hệ thống gửi thông báo về tiến<br>trình xử lý hồ sơ:<br>•<br>Đang xử lý: Hồ sơ đã được<br>tiếp nhận<br>•<br>Đạt: Hồ sơ ứng tuyển đạt<br>yêu cầu, bộ phận tuyển<br>dụng thực hiện quy trình<br>tuyển dụng thủ công<br>•<br>Không đạt: Hồ sơ bị từ<br>chối, người dùng có thể<br>ứng tuyển lại|

## Mô tả màn hình

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
<th>STT</th>
<th>Thông<br>tin</th>
<th>Kiể<br>u<br>control</th>
<th>Bắ<br>t<br>buộc</th>
<th>Mặc<br>định</th>
<th>Mô tả</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**</td>
<td>**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**</td>
<td>**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**</td>
<td>**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**</td>
<td>**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**</td>
<td>**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**</td>
</tr>
<tr>
<td>**Thông tin cá nhân**</td>
<td>**Thông tin cá nhân**</td>
<td>**Thông tin cá nhân**</td>
<td>**Thông tin cá nhân**</td>
<td>**Thông tin cá nhân**</td>
<td>**Thông tin cá nhân**</td>
</tr>
<tr>
<td>1</td>
<td>Họ và<br>tên</td>
<td>Textbox</td>
<td>Có</td>
<td>Hint<br>text:</td>
<td>Cho phép nhập họ và tên<br>**Message:**</td>
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
<th>Col1</th>
<th>Col2</th>
<th>Col3</th>
<th>Col4</th>
<th>Nhập h<br>ọ<br>và tên</th>
<th>Để trố ng trường thông ti n > Hiể n thị<br>message:</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>Năm<br>sinh</td>
<td>Textbox</td>
<td>Có</td>
<td>Hint<br>text:<br>Nhập<br>năm sinh</td>
<td>Chỉ cho phép nhập số, tối đa 4 số<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:</td>
</tr>
<tr>
<td>3</td>
<td>Số<br>điện<br>thoại</td>
<td>Textbox</td>
<td>Có</td>
<td>Hint<br>text:<br>Nhập số<br>điện<br>thoại</td>
<td>Chỉ cho phép nhập số, tối đa 10 số, không<br>chứa ký tự đặc biệt<br>**Message:**<br>- Nhập sai định dạng > Hiển thị message:<br>“Số điện thoại không hợp lệ.”<br>- Để trống trường thông tin > Hiển thị<br>message:</td>
</tr>
<tr>
<td>**Vị trí ứng tuyển**</td>
<td>**Vị trí ứng tuyển**</td>
<td>**Vị trí ứng tuyển**</td>
<td>**Vị trí ứng tuyển**</td>
<td>**Vị trí ứng tuyển**</td>
<td>**Vị trí ứng tuyển**</td>
</tr>
<tr>
<td>1</td>
<td>Vị trí<br>ứng<br>tuyển</td>
<td>Check box</td>
<td>Có</td>
<td>N/A</td>
<td>Chọn 1 trong 3 vị trí ứng tuyển:<br>- Nhân viên bưu tá<br>- Nhân viên khai thác<br>- Tài xế xe tải<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:</td>
</tr>
<tr>
<td>**Khu vực ứng tuyển**</td>
<td>**Khu vực ứng tuyển**</td>
<td>**Khu vực ứng tuyển**</td>
<td>**Khu vực ứng tuyển**</td>
<td>**Khu vực ứng tuyển**</td>
<td>**Khu vực ứng tuyển**</td>
</tr>
<tr>
<td>1</td>
<td>Tỉnh</td>
<td>Dropdown<br>list</td>
<td>Có</td>
<td>Hint<br>text:<br>Chọn<br>tỉnh</td>
<td>Chọn tỉnh từ danh sách Hệ thống quản lý<br>nhân sự trả về<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:</td>
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
<th>Col1</th>
<th>Col2</th>
<th>Col3</th>
<th>Col4</th>
<th>Col5</th>
<th>Col6</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>Bưu<br>cục</td>
<td>Dropdown<br>list</td>
<td>Có</td>
<td>Hint<br>text:<br>Chọn<br>bưu cục</td>
<td>Chọn bưu cục theo tỉnh từ danh sách Hệ<br>thống quản lý nhân sự trả về. Chỉ được chọn<br>bưu cục khi đã chọn tỉnh<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:</td>
</tr>
<tr>
<td>3</td>
<td>Điều<br>khoản<br>quy<br>định</td>
<td>Check box</td>
<td>Có</td>
<td>N/A</td>
<td>Mặc định tích điều khoản quy định<br>**Message:**<br>Bỏ tích điều khoản quy định > Hiển thị<br>message:</td>
</tr>
<tr>
<td>4</td>
<td>Đăng<br>ký</td>
<td>Button</td>
<td>N/A</td>
<td>N/A</td>
<td>Click on => Hiển thị popup<br>**_Message:_**<br>Trong vòng 7 ngày: Cùng thông tin cá nhân,<br>cùng vị trí ứng tuyển, cùng khu vực ứng<br>tuyển, cùng trạng thái Chưa xử lý => Không<br>tiếp nhận hồ sơ tương tự.<br>Khi click on button => Hiển thị message:<br>“Bạn đã ứng tuyển cho vị trí này, vui lòng<br>đợi xét duyệt"<br>Click hủy => Giữ nguyên màn ứng tuyển<br>Click Xác nhận => Điều hướng màn hình</td>
</tr>
</tbody>
</table>
|---|---|---|---|---|---| |**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**|**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**|**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**|**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**|**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**|**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**| |**Thông tin cá nhân**|**Thông tin cá nhân**|**Thông tin cá nhân**|**Thông tin cá nhân**|**Thông tin cá nhân**|**Thông tin cá nhân**| |1|Họ và<br>tên|Textbox|Có|Hint<br>text:|Cho phép nhập họ và tên<br>**Message:**|    4                       |---|---|---|---|---|---| |2|Năm<br>sinh|Textbox|Có|Hint<br>text:<br>Nhập<br>năm sinh|Chỉ cho phép nhập số, tối đa 4 số<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:| |3|Số<br>điện<br>thoại|Textbox|Có|Hint<br>text:<br>Nhập số<br>điện<br>thoại|Chỉ cho phép nhập số, tối đa 10 số, không<br>chứa ký tự đặc biệt<br>**Message:**<br>- Nhập sai định dạng > Hiển thị message:<br>“Số điện thoại không hợp lệ.”<br>- Để trống trường thông tin > Hiển thị<br>message:| |**Vị trí ứng tuyển**|**Vị trí ứng tuyển**|**Vị trí ứng tuyển**|**Vị trí ứng tuyển**|**Vị trí ứng tuyển**|**Vị trí ứng tuyển**| |1|Vị trí<br>ứng<br>tuyển|Check box|Có|N/A|Chọn 1 trong 3 vị trí ứng tuyển:<br>- Nhân viên bưu tá<br>- Nhân viên khai thác<br>- Tài xế xe tải<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:| |**Khu vực ứng tuyển**|**Khu vực ứng tuyển**|**Khu vực ứng tuyển**|**Khu vực ứng tuyển**|**Khu vực ứng tuyển**|**Khu vực ứng tuyển**| |1|Tỉnh|Dropdown<br>list|Có|Hint<br>text:<br>Chọn<br>tỉnh|Chọn tỉnh từ danh sách Hệ thống quản lý<br>nhân sự trả về<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:|   5    |<image_1>|   |<image_2>|   |<image_3>|   |<image_4>|              |---|---|---|---|---|---| |2|Bưu<br>cục|Dropdown<br>list|Có|Hint<br>text:<br>Chọn<br>bưu cục|Chọn bưu cục theo tỉnh từ danh sách Hệ<br>thống quản lý nhân sự trả về. Chỉ được chọn<br>bưu cục khi đã chọn tỉnh<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:| |3|Điều<br>khoản<br>quy<br>định|Check box|Có|N/A|Mặc định tích điều khoản quy định<br>**Message:**<br>Bỏ tích điều khoản quy định > Hiển thị<br>message:| |4|Đăng<br>ký|Button|N/A|N/A|Click on => Hiển thị popup<br>**_Message:_**<br>Trong vòng 7 ngày: Cùng thông tin cá nhân,<br>cùng vị trí ứng tuyển, cùng khu vực ứng<br>tuyển, cùng trạng thái Chưa xử lý => Không<br>tiếp nhận hồ sơ tương tự.<br>Khi click on button => Hiển thị message:<br>“Bạn đã ứng tuyển cho vị trí này, vui lòng<br>đợi xét duyệt"<br>Click hủy => Giữ nguyên màn ứng tuyển<br>Click Xác nhận => Điều hướng màn hình|   6    |<image_5>|   |<image_6>|   |<image_7>|   |<image_8>|      7    |<image_9>|