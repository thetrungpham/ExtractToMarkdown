# Public_319

### NỘI DUNG QUY TRÌNH

# **1. Quan điểm. mục đích**

### + Quan điểm:

✓ Quy trình chỉ ra các bước và các tiêu chí đánh giá, nguồn tri thức và thông tin  đáng tin cậy để đơn vị làm căn cứ đánh giá, lựa chọn hệ quản trị cơ sở dữ liệu (DBMS).
✓ Đơn vị cần tuân thủ việc đánh giá đầy đủ qua các bước với các tiêu chí được nêu  và căn cứ vào kết quả đánh giá để ra quyết định lựa chọn công nghệ phù hợp với dự án.
✓ Quy trình này nằm trong bước phân tích nghiệp vụ trong Quy trình phát triển  phần mềm của Tập đoàn, đầu ra của quy trình này sẽ giúp cho đơn vị đưa ra quyết định lựa chọn DBMS một cách đúng đắn, là cơ sở để xây dựng chỉ tiêu về hệ quản trị CSDL trong CTKT và tài liệu giải pháp.
✓ Các đơn vị có trách nhiệm cung cấp use cases thường xuyên để quy trình này  được cập nhật các tri thức mới. Đánh giá liên tục để xem có phù hợp với thực tế hay không.
**+ Mục đích:** Quy trình này nhằm quy định thống nhất phương pháp lựa chọn hệ quản trị CSDL cho các dự án xây mới và nâng cấp phát triển phần mềm.

# **2. Phạm vi, đối tượng áp dụng**

  * Phạm vi: Áp dụng cho hoạt động đánh giá, lựa chọn hệ quản trị CSDL cho  các dự án phần mềm.
   * Đối tượng áp dụng: Các cơ quan, đơn vị trong Tập đoàn

# **3. Tài liệu liên quan**

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>TT</th>
<th>Tàiliệ<br>u</th>
<th>Thờigianban<br>hành</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Bộ tiêu chuẩn Lưu trữ và Vận hành dữ liệu<br>TC.CNVTQĐ.CNTT.40</td>
<td>09/2022</td>
</tr>
<tr>
<td>2</td>
<td>Quy định thiết lập, quản lý, lưu trữ, khai thác log hệ thống<br>CNTT số 4137/QĐ-CNVTQĐ-CNTT.</td>
<td>9/2021</td>
</tr>
<tr>
<td>3</td>
<td>Quy định xây dựng, nâng cấp, bảo trì các sản phẩm phần<br>mềm trong Tập đoàn Công nghiệp – Viễn thông Quân đội<br>(3388/QĐ-CNVQTĐ-CNTT)</td>
<td>7/2021</td>
</tr>
<tr>
<td>4</td>
<td>Bộ tiêu chuẩn lưu trữ và vận hành dữ liệu<br>(TC.CNVTQĐ.CNTT.40)</td>
<td>9/2022</td>
</tr>
</tbody>
</table>
|---|---|---| |1|Bộ tiêu chuẩn Lưu trữ và Vận hành dữ liệu<br>TC.CNVTQĐ.CNTT.40|09/2022| |2|Quy định thiết lập, quản lý, lưu trữ, khai thác log hệ thống<br>CNTT số 4137/QĐ-CNVTQĐ-CNTT.|9/2021| |3|Quy định xây dựng, nâng cấp, bảo trì các sản phẩm phần<br>mềm trong Tập đoàn Công nghiệp – Viễn thông Quân đội<br>(3388/QĐ-CNVQTĐ-CNTT)|7/2021| |4|Bộ tiêu chuẩn lưu trữ và vận hành dữ liệu<br>(TC.CNVTQĐ.CNTT.40)|9/2022|

# **4. Giải thích thuật ngữ và từ viết tắt**

### Thuật ngữ

* **Dữ liệu (Data):** là thông tin được máy tính lưu trữ, xử lý hoặc truy xuất  theo yêu cầu của người dùng hoặc theo tiến trình hoạt động của máy tính.
* **Cơ sở dữ liệu:** Chỉ mọi tập hợp dữ liệu được lưu trữ, bất kể cấu trúc  hoặc nội dung. Trong một số cơ sở dữ liệu lớn CSDL được nhắc đến như là instances và schema.
* **Instance** : Là một triển khai phần mềm cơ sở dữ liệu (DBMS) có nhiệm  vụ kiểm soát quyền truy cập vào một khu vực lưu trữ nhất định. Thường tổ chức có nhiều instance chạy đồng thời, độc lập nhau và mỗi instance kiểm soát truy cập vào các khu vực lưu trữ khác nhau.
* **Hệ quản trị CSDL hay DBMS (Database Management System):** Là  phần mềm tương tác với người dùng cuối, ứng dụng và chính cơ sở dữ liệu để thu thập và phân tích dữ liệu. Phần mềm DBMS bao gồm các tiện ích cốt lõi được cung cấp để quản trị cơ sở dữ liệu.
* **Node:** Một máy tính/ máy chủ vật lý lưu trữ và xử lý dữ liệu như một  phần của cơ sở dữ liệu phân tán.
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>STT</th>
<th>Thuật ngữ vàtừ viế t tắ t</th>
<th>Giảithích</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.</td>
<td>CSDL</td>
<td>Cơ sở dữ liệu</td>
</tr>
<tr>
<td>2.</td>
<td>RDBMS</td>
<td>Relational Database Management System (Hệ quản<br>trị CSDLquan hệ)</td>
</tr>
<tr>
<td>3.</td>
<td>NoSQL</td>
<td>NonRelational hoặc Not Only SQL: Là loại DBMS<br>dành cho dữ liệu có cấu trúc linh hoạt, không cố<br>định.<br></td>
</tr>
<tr>
<td>4.</td>
<td>ĐV PTPM</td>
<td>Đơn vị Phát tri~~ể~~n ph~~ầ~~n m~~ề~~m</td>
</tr>
<tr>
<td>5.</td>
<td>ĐV Nghiệp vụ</td>
<td>Đơn vị đặt hàng xây dựng phần mềm, am hiểu về<br>nghiệp vụ.</td>
</tr>
<tr>
<td>6.</td>
<td>ĐV VHKT</td>
<td>Đơn vị vận hành khai thác cơ sở dữ liệu</td>
</tr>
</tbody>
</table>
  * **Từ viết tắt:**  |---|---|---| |1.|CSDL|Cơ sở dữ liệu| |2.|RDBMS|Relational Database Management System (Hệ quản<br>trị CSDLquan hệ)| |3.|NoSQL|NonRelational hoặc Not Only SQL: Là loại DBMS<br>dành cho dữ liệu có cấu trúc linh hoạt, không cố<br>định.<br>| |4.|ĐV PTPM|Đơn vị Phát tri~~ể~~n ph~~ầ~~n m~~ề~~m| |5.|ĐV Nghiệp vụ|Đơn vị đặt hàng xây dựng phần mềm, am hiểu về<br>nghiệp vụ.| |6.|ĐV VHKT|Đơn vị vận hành khai thác cơ sở dữ liệu|

# **5. Nội dung quy trình lựa chọn Hệ quản trị cơ sở dữ liệu cho các dự án** **xây mới, nâng cấp phần mềm**

### Sự kiện bắt đầu và kết thúc

  * Sự kiện bắt đầu: Khi có nhu cầu lựa chọn DBMS cho các dự án xây mới, nâng  cấp phần mềm.
   * Sự kiện kết thúc: Lựa chọn được DBMS phù hợp với yêu cầu của bài toán  nghiệp vụ, đưa vào CTKT và tài liệu giải pháp của phần mềm được xây mới hoặc nâng cấp.
   * Đầu vào: Khi có yêu cầu xây mới/ nâng cấp phần mềm.
   * Đầu ra: DBMS được lựa chọn trong CTKT phần mềm và tài liệu giải pháp.

### Lưu đồ tổng thể quy trình

### Diễn giải chi tiết

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
<th>Đưarayêu<br>cầ về dữ<br>u<br>liệu</th>
<th>Khi đơn vị nghiệp đưa<br>vụ<br>ra yêu cầ u về xây dựng<br>,<br>nâng cấ p phầ n mề m (th eo<br>biể mẫ được đị nh<br>u u quy<br>trong Phụ lục 01) đơn vị<br>,<br>PTPMphốihợpvớiđơnvị<br>nghiệp phân tích làm<br>vụ<br>,<br>rõ các yêu cầ u về quản lý<br>,<br>lưutrữvàxửlýdữliệucủa<br>ứng d ụng th eo các tiêu chí<br>sau:<br>- Cấ u trúc dữ liệu<br>Kiể tổ chức dữ<br>- u<br>liệu<br>Kiể uxử lý dữ liệu<br>-<br>- Yêu cầ u đảm bảo<br>tính ACID/BASE<br>,<br>các ưu tiên trong<br>đị nh l uật CAP<br>Nh ucầ đ ghi dữ<br>- u ọc<br>liệu<br>Quy mô dữ liệu<br>-<br>Chi tiế t về các tiêu chí<br>công nghệ cầ n phân tích<br>,<br>đánh giá th eo Phụ lục 02<br>.</th>
<th>ĐV<br>nghiệpvụ;<br>ĐV PTPM</th>
<th>Phân tích<br>yêucầ u xây<br>dựng nâng<br>,<br>ấ hầ<br>c p p n<br>ề<br>m m</th>
<th>Các nhận<br>đị h ề<br>n v<br>l i<br>oạ<br>DBMS<br>phù hợp<br>với từng<br>tiêu chí<br>khi<br>sau<br>đánh giá<br>yêu cầ u</th>
</tr>
</thead>
<tbody>
<tr>
<td>2.</td>
<td>So   sánh<br>các  nhận<br>định<br>sau<br>đánh giá ở<br>Bước<br>1 <br>với các<br>loại</td>
<td>Sau khi đưa ra nhận định<br>về loại DBMS phù hợp với<br>các tiêu chí đánh giá ở<br>Bước 1, đơn vị PTPM đưa<br>ra các đề xuất về các sản<br>phẩm DBMS có khả năng<br>đáp ứng yêu cầu bài toán</td>
<td>ĐV PTPM</td>
<td>Các<br>loai<br>DBMS phù<br>hợp với các<br>tiêu<br>chí<br>công nghệ<br>riêng lẻ</td>
<td>Tổng hợp<br>các<br>DBMS<br>phù<br>hợp<br>với tất cả<br>các   tiêu</td>
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
<th>DBMS<br>hổ biế<br>p n<br>trên thị<br>trường</th>
<th>về mặt công nghệ các ưu<br>,<br>tiên cầ n đáp ứng ch o bài<br>toán<br>.<br>Thông ti n về đặc trưng so<br>,<br>sánh các l oại DBMS phổ<br>biế n xem trong Phụ lục<br>03<br>.</th>
<th>Col4</th>
<th>Col5</th>
<th>chícủabài<br>toán<br>.</th>
</tr>
</thead>
<tbody>
<tr>
<td>3.</td>
<td>Đánh giá<br>vấn đề chi<br>phí và bản<br>quyền</td>
<td>Chọn DBMS thương mại<br>khi: Khách hàng có yêu<br>cầu chọn 1 hoặc loại<br>DBMS và đảm bảo có<br>ngân sách của dự án đủ chi<br>trả, hiệu quả kinh doanh<br>vượt trội so với chi phí bỏ<br>ra.<br>Các trường hợp còn lại:<br>Phải ưu tiên chọn DBMS<br>mã nguồn mở và tuân theo<br>HD về sử dụng mã nguồn<br>mở của Tập đoàn.<br>Các lưu ý về chi phí và<br>license cho DBMS xem<br>trong **Phụ lục 04**.</td>
<td>ĐV PTPM</td>
<td>Các căn cứ<br>lựa<br>chọn<br>sản<br>phẩm<br>thương mại</td>
<td>Danh sách<br>sản phẩm<br>đáp<br>ứng<br>được tiêu<br>chí về chi<br>phí/<br>bản<br>quyền.</td>
</tr>
<tr>
<td>4</td>
<td>Đánh  giá<br>năng lực<br>làm<br>chủ<br>sản phẩm<br>của đội dự<br>án</td>
<td>Đội dự án của ĐV PTPM<br>và Đơn vị VHKT dữ liệu<br>(dự kiến) đánh giá năng<br>lực làm chủ của mình đối<br>với sản phẩm được chọn<br>qua 3 bước trên. Ưu tiên<br>chọn sản phẩm mà đội dự<br>án am hiểu và thành thạo<br>nhất và vận hành đơn giản,<br>ít lỗi.<br>Trường hợp là DBMS mới<br>đối với đơn vị thìcần phải</td>
<td>ĐV PTPM<br>ĐV<br>VHKT</td>
<td>Các use<br>cases<br>đội<br>dự án đã<br>triển<br>khai<br>hoặc tham<br>khảo từ các<br>đơn vị<br>khác.<br>Biên<br>bản<br>đánh<br>giá<br>kết quả thử<br>nghiệp theo</td>
<td>Kết   quả<br>lựa<br>chọn<br>sản phẩm<br>DBMS tối<br>ưu cho dự<br>án<br>được<br>Trưởng dự<br>án và Lãnh<br>đạo đơn vị<br>vận hành<br>CSDL.</td>
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
<th>có đánh giá thử nghiệp<br>trước khi ra quyế t đị nh lựa<br>h<br>c ọn<br>.<br>Biể mẫ đánh giá lựa<br>u u<br>ch ọn từ Bước 1 2 3 4 xem<br>,,,<br>trong Phụ lục 05<br>.<br>Các đơn vị th am khảo<br>thêmki nh nghiệm sửd<br>ụng<br>các DBMS phổ biế n tại<br>Vi ettel th eo Phụlục 06<br>.</th>
<th>Col4</th>
<th>các tiêu chí<br>công nghệ<br>được ưu<br>tiên<br>.</th>
<th>Col6</th>
</tr>
</thead>
<tbody>
<tr>
<td>5</td>
<td>Xây dựng<br>CTKT về<br>DBMS<br>cho<br>ứng<br>dụng phần<br>mềm</td>
<td>Đội dự án đưa kết quả lựa<br>chọn DBMS ở Bước 4 vào<br>CTKT phần mềm.<br>Xem hướng dẫn xây dựng<br>CTKT cho phần mềm theo<br>**42/HD.00.CNTT.17.**</td>
<td>ĐV PTPM</td>
<td>Căn cứ vào<br>kết quả phê<br>duyệt<br>lựa<br>chọn<br>DMBS</td>
<td>CTKT<br>phần mềm</td>
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
<th>STT</th>
<th>Hoạtđộng chính</th>
<th>ĐVNghiệp<br>vụ</th>
<th>ĐV PTPM</th>
<th>ĐV VHKT</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.</td>
<td>Đưa rayêu c~~ầ~~u v~~ề~~ dữ liệu</td>
<td>A/R</td>
<td>S</td>
</tr>
<tr>
<td>2.</td>
<td>Lựa chọn sản phẩm có khả năng đáp<br>ứng yêu cầu theo các tiêu chí công<br>nghệ</td>
<td>R</td>
<td>A/R</td>
<td>I</td>
</tr>
<tr>
<td>3.</td>
<td>Đánh giá vấn đề chi phí và bản<br>quyền</td>
<td>I</td>
<td>A/R</td>
<td>R</td>
</tr>
<tr>
<td>4.</td>
<td>Đánh giá khả năng làm chủ công<br>nghệ</td>
<td>R</td>
<td>A</td>
<td>R</td>
</tr>
<tr>
<td>5.</td>
<td>Báo cáo, phê duyệt, thẩm định và<br>đưa vào CTKT</td>
<td>I</td>
<td>A/R</td>
<td>I</td>
</tr>
</tbody>
</table>
|<image_1>|                 |---|---|---|---|---|---| |2.|So   sánh<br>các  nhận<br>định<br>sau<br>đánh giá ở<br>Bước<br>1 <br>với các<br>loại|Sau khi đưa ra nhận định<br>về loại DBMS phù hợp với<br>các tiêu chí đánh giá ở<br>Bước 1, đơn vị PTPM đưa<br>ra các đề xuất về các sản<br>phẩm DBMS có khả năng<br>đáp ứng yêu cầu bài toán|ĐV PTPM|Các<br>loai<br>DBMS phù<br>hợp với các<br>tiêu<br>chí<br>công nghệ<br>riêng lẻ|Tổng hợp<br>các<br>DBMS<br>phù<br>hợp<br>với tất cả<br>các   tiêu|                  |---|---|---|---|---|---| |3.|Đánh giá<br>vấn đề chi<br>phí và bản<br>quyền|Chọn DBMS thương mại<br>khi: Khách hàng có yêu<br>cầu chọn 1 hoặc loại<br>DBMS và đảm bảo có<br>ngân sách của dự án đủ chi<br>trả, hiệu quả kinh doanh<br>vượt trội so với chi phí bỏ<br>ra.<br>Các trường hợp còn lại:<br>Phải ưu tiên chọn DBMS<br>mã nguồn mở và tuân theo<br>HD về sử dụng mã nguồn<br>mở của Tập đoàn.<br>Các lưu ý về chi phí và<br>license cho DBMS xem<br>trong **Phụ lục 04**.|ĐV PTPM|Các căn cứ<br>lựa<br>chọn<br>sản<br>phẩm<br>thương mại|Danh sách<br>sản phẩm<br>đáp<br>ứng<br>được tiêu<br>chí về chi<br>phí/<br>bản<br>quyền.| |4|Đánh  giá<br>năng lực<br>làm<br>chủ<br>sản phẩm<br>của đội dự<br>án|Đội dự án của ĐV PTPM<br>và Đơn vị VHKT dữ liệu<br>(dự kiến) đánh giá năng<br>lực làm chủ của mình đối<br>với sản phẩm được chọn<br>qua 3 bước trên. Ưu tiên<br>chọn sản phẩm mà đội dự<br>án am hiểu và thành thạo<br>nhất và vận hành đơn giản,<br>ít lỗi.<br>Trường hợp là DBMS mới<br>đối với đơn vị thìcần phải|ĐV PTPM<br>ĐV<br>VHKT|Các use<br>cases<br>đội<br>dự án đã<br>triển<br>khai<br>hoặc tham<br>khảo từ các<br>đơn vị<br>khác.<br>Biên<br>bản<br>đánh<br>giá<br>kết quả thử<br>nghiệp theo|Kết   quả<br>lựa<br>chọn<br>sản phẩm<br>DBMS tối<br>ưu cho dự<br>án<br>được<br>Trưởng dự<br>án và Lãnh<br>đạo đơn vị<br>vận hành<br>CSDL.|              |---|---|---|---|---|---| |5|Xây dựng<br>CTKT về<br>DBMS<br>cho<br>ứng<br>dụng phần<br>mềm|Đội dự án đưa kết quả lựa<br>chọn DBMS ở Bước 4 vào<br>CTKT phần mềm.<br>Xem hướng dẫn xây dựng<br>CTKT cho phần mềm theo<br>**42/HD.00.CNTT.17.**|ĐV PTPM|Căn cứ vào<br>kết quả phê<br>duyệt<br>lựa<br>chọn<br>DMBS|CTKT<br>phần mềm|     - **Vai trò của các bên liên quan**        |---|---|---|---|---| |1.|Đưa rayêu c~~ầ~~u v~~ề~~ dữ liệu|A/R|S|| |2.|Lựa chọn sản phẩm có khả năng đáp<br>ứng yêu cầu theo các tiêu chí công<br>nghệ|R|A/R|I| |3.|Đánh giá vấn đề chi phí và bản<br>quyền|I|A/R|R| |4.|Đánh giá khả năng làm chủ công<br>nghệ|R|A|R| |5.|Báo cáo, phê duyệt, thẩm định và<br>đưa vào CTKT|I|A/R|I|

### Giải thích:

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Chữviế ttắ<br>t</th>
<th>Ý nghĩa</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>Đơn vị/vai trò chịu trách nhiệm giải trình k~~ế~~t quả của hoạt động</td>
</tr>
<tr>
<td>R</td>
<td>Đơn vị/vai trò chịu trách nhiệm thực hiện hoạt động<br></td>
</tr>
<tr>
<td>S</td>
<td>Đơn vị/vai trò cung c~~ấ~~p ngu~~ồ~~n lực và hỗ trợ thực hiện hoạt động</td>
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
<th>C</th>
<th>Đơn vị/ vai trò cung cấ p thông ti n và tư vấ n hỗ trợtrước và trong quá<br>trìnhthực hiện h oạt động</th>
</tr>
</thead>
<tbody>
<tr>
<td>I</td>
<td>Đơn vị/vai trò được thông báo/cung cấp thông tin sau khi hoạt động<br>được thực hiện</td>
</tr>
</tbody>
</table>
|---|---| |A|Đơn vị/vai trò chịu trách nhiệm giải trình k~~ế~~t quả của hoạt động| |R|Đơn vị/vai trò chịu trách nhiệm thực hiện hoạt động<br>| |S|Đơn vị/vai trò cung c~~ấ~~p ngu~~ồ~~n lực và hỗ trợ thực hiện hoạt động|      |---|---| |I|Đơn vị/vai trò được thông báo/cung cấp thông tin sau khi hoạt động<br>được thực hiện|

# **6. Tiêu chí, chỉ số đánh giá việc thực hiện quy trình**

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Miêutả KPI</th>
<th>Côngthứctính : Tỉlệtuâ nthủ quytrì nh =Tổ ngsốd ựá ncóbá ocá ol ựa<br>ch DBMS đú trì nh trướ khi xâ d CTKT/ Tổ số d á<br>ọn ng quy c y ựng ng ự n<br>.<br>Cáchtính :Hàngquýđơnvị chị utrách nhiệmràsoátvàlấ ysốlượngtrên<br>hệ thố ng đ ể tính tỉ lệ<br>.</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mục đích KPI</td>
<td>Quản lý việc tuân thủquy trình.</td>
</tr>
<tr>
<td>Ngưỡng KPI<br>mục tiêu</td>
<td>>=90% (Kiểm tra thử nghiệm sau 3 tháng sau đó sẽ điều chỉnh ngưỡng<br>KPI theo thực tế)</td>
</tr>
<tr>
<td>Đơn  vị  chịu<br>trách<br>nhiệm<br>thực hiện KPI</td>
<td>ĐV PTPM</td>
</tr>
<tr>
<td>Đơn vị rà soát<br>việc thực hiện<br>KPI</td>
<td>Bộ phận Quản trị dữ liệu</td>
</tr>
</tbody>
</table>
|---|---| |Mục đích KPI|Quản lý việc tuân thủquy trình.| |Ngưỡng KPI<br>mục tiêu|>=90% (Kiểm tra thử nghiệm sau 3 tháng sau đó sẽ điều chỉnh ngưỡng<br>KPI theo thực tế)| |Đơn  vị  chịu<br>trách<br>nhiệm<br>thực hiện KPI|ĐV PTPM| |Đơn vị rà soát<br>việc thực hiện<br>KPI|Bộ phận Quản trị dữ liệu|

# **7. Phụ lục đính kèm**

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>TT</th>
<th>Tênphục lục/ biể u mẫ u</th>
<th>Mãsố</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Phụ lục 01 Bi~~ể~~u mẫu PYC xây mới, nâng c~~ấ~~p phàn m~~ề~~m</td>
<td>PL01</td>
</tr>
<tr>
<td>2</td>
<td>Phụ lục 02 Các tiêu chí công nghệ<br></td>
<td>PL01</td>
</tr>
<tr>
<td>3</td>
<td>Phụ lục 03 Các loại DBMSph~~ổ~~ bi~~ế~~n <br></td>
<td>PL02</td>
</tr>
<tr>
<td>4</td>
<td>Phụ luc 04 Hướng dẫn đánhgiá chiphí và bảnquy~~ề~~n <br></td>
<td>PL03</td>
</tr>
<tr>
<td>5</td>
<td>Phụ lục 05 Bi~~ể~~u mẫu đánhgiá t~~ổ~~ng hợp</td>
<td>PL05</td>
</tr>
<tr>
<td>6</td>
<td>Phụ lục 06 DS Usecase sử dụng DBMS tại Viettel</td>
<td>PL06</td>
</tr>
</tbody>
</table>
|---|---|---| |1|Phụ lục 01 Bi~~ể~~u mẫu PYC xây mới, nâng c~~ấ~~p phàn m~~ề~~m|PL01| |2|Phụ lục 02 Các tiêu chí công nghệ<br>|PL01| |3|Phụ lục 03 Các loại DBMSph~~ổ~~ bi~~ế~~n <br>|PL02| |4|Phụ luc 04 Hướng dẫn đánhgiá chiphí và bảnquy~~ề~~n <br>|PL03| |5|Phụ lục 05 Bi~~ể~~u mẫu đánhgiá t~~ổ~~ng hợp|PL05| |6|Phụ lục 06 DS Usecase sử dụng DBMS tại Viettel|PL06|