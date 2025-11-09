# Public_320

# Quan điểm, mục đích

### + Quan điểm:

✓ Đơn vị cần tuân thủ việc đánh giá đầy đủ qua các bước với các tiêu chí được nêu và  căn cứ vào kết quả đánh giá để ra quyết định lựa chọn công nghệ phù hợp với yêu cầu.
✓ Quy trình này hỗ trợ đưa ra căn cứ lựa chọn công trong các chỉ tiêu kỹ thuật cho các  dự án mua sắm, đầu tư tài nguyên lưu trữ mới.
✓ Các đơn vị có trách nhiệm cung cấp use cases thường xuyên để quy trình này được  cập nhật các tri thức mới. Đánh giá liên tục để đánh giá mức độ phù hợp với thực tế.
**+ Mục đích:** Quy trình này nhằm quy định thống nhất phương pháp lựa chọn hạ tầng lưu trữ dữ liệu tại các đơn vị.

# Phạm vi, đối tượng áp dụng

     * Phạm vi: Áp dụng cho hoạt động đánh giá, lựa chọn hạ tầng lưu trữ dữ liệu.
      * Đối tượng áp dụng: Các cơ quan, đơn vị trong Tập đoàn

# Tài liệu liên quan

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
<th>Ngày ban hành</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Bộ tiêu chuẩn Lưu trữ và Vận hành dữ liệu<br>TC.CNVTQĐ.CNTT.40</td>
<td>3/2021</td>
</tr>
<tr>
<td>2</td>
<td>Quy định xây dựng và áp dụng chỉ tiêu kỹ thuật cho sản<br>phẩm hàng hóa phục vụ hoạt động của Tập đoàn CNVTQĐ<br>mã hiệu 3208/QyĐ-CNVTQĐ-VTNet</td>
<td>9/2020</td>
</tr>
<tr>
<td>3</td>
<td>Guideline định cỡ cấp phát tài nguyên CNTT mã hiệu<br>GL.CNVTQĐ.CNTT.18.514</td>
<td>09/2021</td>
</tr>
</tbody>
</table>
|---|---|---| |1|Bộ tiêu chuẩn Lưu trữ và Vận hành dữ liệu<br>TC.CNVTQĐ.CNTT.40|3/2021| |2|Quy định xây dựng và áp dụng chỉ tiêu kỹ thuật cho sản<br>phẩm hàng hóa phục vụ hoạt động của Tập đoàn CNVTQĐ<br>mã hiệu 3208/QyĐ-CNVTQĐ-VTNet|9/2020| |3|Guideline định cỡ cấp phát tài nguyên CNTT mã hiệu<br>GL.CNVTQĐ.CNTT.18.514|09/2021|

# Giải thích thuật ngữ và từ viết tắt

     **Thuật ngữ**    * **Dữ liệu (Data):** là thông tin được máy tính lưu trữ, xử lý hoặc truy xuất theo  yêu cầu của người dùng hoặc theo tiến trình hoạt động của máy tính.
          * **Hạ tầng lưu trữ dữ liệu:** gồm hệ thống vật lý và logic có nhiệm vụ quản lý  và lưu trữ dữ liệu có thể bao gồm SAN (Storage Area Network), NAS (Network Attached Storage), DAS (Direct Attached System), Object Storage và (SDS) Software Define Storage.
     * **Retention:** Lưu giữ dữ liệu đảm bảo luôn sẵn sàng phục vụ nhu cầu truy  xuất của dữ liệu ngay khi có yêu cầu.
     * **Archive:** Lưu trữ dữ liệu lâu dài. Khi lưu trữ lâu dài, dữ liệu được chuyển  từ phân vùng lưu trữ tốc độ truy xuất cao sang phân vùng có hiệu năng thấp hơn. Khi dữ liệu chuyển từ giai đoạn “Retention” sang “Archive” được còn được gọi là “backup offline”.
     * **Backup dự phòng:** Là việc sao lưu dữ liệu để dự phòng khi có sự cố xảy  ra, dữ liệu vẫn đảm bảo tính sẵn sàng phục vụ cho nghiệp vụ.
     * **Node:** Một máy tính/ máy chủ vật lý lưu trữ và xử lý dữ liệu như một phần  của cơ sở dữ liệu phân tán.
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
<td>Non Relational hoặc Not Only SQL: Là loại DBMS<br>dành cho dữ liệu có cấu trúc linh hoạt</td>
</tr>
<tr>
<td>4.</td>
<td>CNTT</td>
<td>Công nghệ thông tin</td>
</tr>
<tr>
<td>5.</td>
<td>QHĐC</td>
<td>Quy hoạch định cỡ</td>
</tr>
<tr>
<td>6.</td>
<td>VHKT</td>
<td>Vận hành khai thác</td>
</tr>
</tbody>
</table>
          * **Từ viết tắt**  |---|---|---| |1.|CSDL|Cơ sở dữ liệu| |2.|RDBMS|Relational Database Management System (Hệ quản<br>trị CSDLquan hệ)| |3.|NoSQL|Non Relational hoặc Not Only SQL: Là loại DBMS<br>dành cho dữ liệu có cấu trúc linh hoạt| |4.|CNTT|Công nghệ thông tin| |5.|QHĐC|Quy hoạch định cỡ| |6.|VHKT|Vận hành khai thác|

# Nội dung quy trình lựa chọn Hạ tầng lưu trữ dữ liệu

  * Sự kiện bắt đầu và kết thúc   Sự kiện bắt đầu: Khi có nhu cầu đầu tư hạ tầng lưu trữ dữ liệu mới.
   * Sự kiện kết thúc: Lựa chọn được hạ tầng lưu trữ dữ liệu phù hợp cho nhu cầu, đưa  vào CTKT phục vụ các dự án quy hoạch định cỡ và mua sắm tài nguyên hạ tầng lưu trữ dữ liệu mới.
   * Đầu vào: Khi có yêu cầu mua sắm, đầu tư tài nguyên hạ tầng lưu trữ mới.
       * Đầu ra: Loại hạ tầng lưu trữ phù hợp với nhu cầu nghiệp vụ và tối ưu chi phí, tài  nguyên và nỗ lực vận hành khai thác.
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
<th>Bước</th>
<th>Hoạt<br>động<br>chính</th>
<th>Côngviệc thựchiện</th>
<th>Phụtrách<br>thựchiện</th>
<th>Đầ uvào</th>
<th>Đầ<br>ura</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.</td>
<td>Phân tích,<br>đánh<br>giá<br>các<br>tiêu<br>chí<br>công<br>nghệ<br>về<br>lựa<br>chọn</td>
<td>Khi có nhu cầu đầu tư tài<br>nguyên lưu trữ dữ liệu từ<br>các đơn vị có yêu cầu, đơn<br>vị QHĐC thực hiện phân<br>tích, đánh giá theo các tiêu<br>chí công nghệ sau:<br>-  Kiến trúc lưu trữ</td>
<td>Đơn vị<br>yêu cầu<br>Đơn vị<br>QHĐC</td>
<td>Phân<br>tích<br>yêu cầu về<br>hạ tầng cần<br>đầu tư</td>
<td>Các nhận<br>định  về<br>loại<br>hạ<br>tầng<br>phù<br>hợp<br>với<br>từng<br>tiêu<br>chí sau khi</td>
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
<th>h ạtầ nglưu<br>trữ</th>
<th>- Nh u cầ u lưu trữ<br>trong gi ai đ oạn nào<br>của vòng đời dữ<br>liệu ( retenti<br>on<br>,<br>hi i b k )<br>arc v ng ac up<br>,<br>- Các yêu cầ u tính<br>năng và phi tính<br>năng của h ạ tầ ng<br>lưu trữ<br>Chi tiế t về các tiêu chí<br>công nghệ cầ n phân tích<br>,<br>đánh giá th eo Phụ lục 01<br>.</th>
<th>Col4</th>
<th>Col5</th>
<th>đánh giá<br>yêu cầ u</th>
</tr>
</thead>
<tbody>
<tr>
<td>2.</td>
<td>So   sánh<br>các  nhận<br>định<br>sau<br>đánh giá ở<br>Bước<br>1 <br>với các<br>loại<br>hạ<br>tầng<br>lưu<br>trữ<br>phổ<br>biến</td>
<td>Sau khi đưa ra nhận định<br>về loại hạ tầng lưu trữ phù<br>hợp với các tiêu chí đánh<br>giá ở Bước 1, đơn vị<br>QHĐC đưa ra các đề xuất<br>về các sản phẩm hạ tầng<br>phù hợp với các ưu tiên<br>của đơn vị yêu cầu, đánh<br>giá dựa trên toàn bộ các<br>tiêu chí công nghệ.<br>Thông tin về các loại hạ<br>tầng lưu trữ phổ biến và<br>các trường hợp áp dụng<br>của chúng xem trong**Phụ**<br>**lục 02.**<br>Thông tin về use cases sử<br>dụng các loại hạ tầng lưu<br>trữ phổ biến tại Viettel<br>xem trong**Phụ lục 05**</td>
<td>ĐV<br>QHĐC</td>
<td>Các loai hạ<br>tầng<br>phù<br>hợp với các<br>tiêu<br>chí<br>công nghệ<br>riêng lẻ</td>
<td>Tổng hợp<br>các loại hạ<br>tầng lưu<br>trữ<br>phù<br>hợp với tất<br>cả các tiêu<br>chí của bài<br>toán.</td>
</tr>
<tr>
<td>3.</td>
<td>Đánh giá<br>tiêu<br>chí<br>tính<br>phổ<br>biến<br>của</td>
<td>Xem xét tiêu chí về tính<br>phổ biến, mức độ chín<br>muồi và có nhiều phản hồi<br>về khả năng của sản phẩm</td>
<td>ĐV<br>QHĐC</td>
<td>Các căn cứ<br>đánh<br>giá<br>lựa<br>chọn<br>trong<br>các</td>
<td>Danh sách<br>sản phẩm<br>đáp<br>ứng<br>được tiêu</td>
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
<th>sản phẩ m<br>và chi phí</th>
<th>tại các cộng đồ ng công<br>nghệ trên thế giới<br>.<br>Xem xét chi phí ch o 1 đơn<br>vị lưu trữ trên từng l oại h ạ<br>tầ ng để ch ọn l oại tối ưu về<br>TCO<br>.</th>
<th>Col4</th>
<th>báo cáo<br>công nghệ<br>của đơn vị<br>và Tập<br>đ oàn<br>.<br>Các nguồ n<br>thông ti<br>n<br>đáng ti<br>n<br>cậy<br>.</th>
<th>chí về chi<br>phí và<br>mức độ<br>hổ biế<br>p n<br>của sản<br>hẩ<br>p m<br>.</th>
</tr>
</thead>
<tbody>
<tr>
<td>4</td>
<td>Đánh giá<br>năng<br>lực<br>làm<br> chủ<br>sản phẩm,<br>các<br>  sản<br>phẩm<br>DBMS và<br>hệ<br>điều<br>hành<br>hỗ<br>trợ</td>
<td>Đơn vị triển khai cài đặt và<br>Đơn vị vận hành hạ tầng<br>lưu trữ đánh giá năng lực<br>làm chủ sản phẩm. Ưu tiên<br>chọn sản phẩm mà đội dự<br>án am hiểu và thành thạo<br>nhất và vận hành đơn giản,<br>ít lỗi.<br>Trường hợp là hạ tầng lưu<br>trữ mới thì cần phải có<br>đánh giá thử nghiệp trước<br>khi ra quyết định lựa chọn.<br>Biểu mẫu đánh giá lựa<br>chọn từ Bước 1,2,3,4 xem<br>trong**Phụ lục 04.**</td>
<td>ĐV<br>QHĐC</td>
<td>Các use<br>cases<br>đội<br>dự án đã<br>triển<br>khai<br>hoặc tham<br>khảo từ các<br>đơn vị<br>khác.<br>Biên<br>bản<br>đánh<br>giá<br>kết quả thử<br>nghiệp theo<br>các tiêu chí<br>công  nghệ<br>được<br>ưu<br>tiên.</td>
<td>Kết<br>quả<br>lựa<br>chọn<br>hạ<br>tầng<br>lưu<br>trữ<br>được Lãnh<br>đạo đơn vị<br>QHĐC và<br>Lãnh đạo<br>đơn vị vận<br>hành   hạ<br>tầng lưu<br>trữ<br>phê<br>duyệt.</td>
</tr>
<tr>
<td>5</td>
<td>Xây dựng<br>CTKT về<br>Hạ<br>tầng<br>lưu trữ</td>
<td>Đội dự án đưa đưa kết quả<br>lựa chọn hạ tầng lưu trữ ở<br>Bước 4 vào CTKT mua<br>sắm đầu tư mới hạ tầng lưu<br>trữ theo QĐ 3208/QyĐ-<br>CNVTQĐ-VTNet.</td>
<td>ĐV<br>QHĐC</td>
<td>Căn cứ vào<br>kết quả phê<br>duyệt lựa<br>chọn<br>hạ<br>tầng lưu trữ</td>
<td>CTKT hạ<br>tầng<br>lưu<br>trữ</td>
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
<th>1<br>.</th>
<th>Đưarayêucầ uvề tài nguyênlưutrữ</th>
<th>A/R</th>
<th>Col4</th>
<th>Col5</th>
</tr>
</thead>
<tbody>
<tr>
<td>2.</td>
<td>Đánh giá, phân tích các tiêu chí về<br>công nghệ, chi phí, và khả năng làm<br>chủ công nghệ</td>
<td>I</td>
<td>A/R</td>
<td>R</td>
</tr>
<tr>
<td>3.</td>
<td>Thẩm định và phê duyệt lựa chọn hạ<br>tầng lưu trữ</td>
<td>R</td>
<td>A</td>
<td>R</td>
</tr>
<tr>
<td>4.</td>
<td>Đưa kết quả lựa chọn hạ tầng lưu trữ<br>vào CTKTphần mềm</td>
<td>I</td>
<td>A/R</td>
<td>C</td>
</tr>
</tbody>
</table>
    * Lưu đồ tổng thể quy trình   - Diễn giải chi tiết                 |---|---|---|---|---|---| |1.|Phân tích,<br>đánh<br>giá<br>các<br>tiêu<br>chí<br>công<br>nghệ<br>về<br>lựa<br>chọn|Khi có nhu cầu đầu tư tài<br>nguyên lưu trữ dữ liệu từ<br>các đơn vị có yêu cầu, đơn<br>vị QHĐC thực hiện phân<br>tích, đánh giá theo các tiêu<br>chí công nghệ sau:<br>-  Kiến trúc lưu trữ|Đơn vị<br>yêu cầu<br>Đơn vị<br>QHĐC|Phân<br>tích<br>yêu cầu về<br>hạ tầng cần<br>đầu tư|Các nhận<br>định  về<br>loại<br>hạ<br>tầng<br>phù<br>hợp<br>với<br>từng<br>tiêu<br>chí sau khi|    |<image_1>|               |---|---|---|---|---|---| |2.|So   sánh<br>các  nhận<br>định<br>sau<br>đánh giá ở<br>Bước<br>1 <br>với các<br>loại<br>hạ<br>tầng<br>lưu<br>trữ<br>phổ<br>biến|Sau khi đưa ra nhận định<br>về loại hạ tầng lưu trữ phù<br>hợp với các tiêu chí đánh<br>giá ở Bước 1, đơn vị<br>QHĐC đưa ra các đề xuất<br>về các sản phẩm hạ tầng<br>phù hợp với các ưu tiên<br>của đơn vị yêu cầu, đánh<br>giá dựa trên toàn bộ các<br>tiêu chí công nghệ.<br>Thông tin về các loại hạ<br>tầng lưu trữ phổ biến và<br>các trường hợp áp dụng<br>của chúng xem trong**Phụ**<br>**lục 02.**<br>Thông tin về use cases sử<br>dụng các loại hạ tầng lưu<br>trữ phổ biến tại Viettel<br>xem trong**Phụ lục 05**|ĐV<br>QHĐC|Các loai hạ<br>tầng<br>phù<br>hợp với các<br>tiêu<br>chí<br>công nghệ<br>riêng lẻ|Tổng hợp<br>các loại hạ<br>tầng lưu<br>trữ<br>phù<br>hợp với tất<br>cả các tiêu<br>chí của bài<br>toán.| |3.|Đánh giá<br>tiêu<br>chí<br>tính<br>phổ<br>biến<br>của|Xem xét tiêu chí về tính<br>phổ biến, mức độ chín<br>muồi và có nhiều phản hồi<br>về khả năng của sản phẩm|ĐV<br>QHĐC|Các căn cứ<br>đánh<br>giá<br>lựa<br>chọn<br>trong<br>các|Danh sách<br>sản phẩm<br>đáp<br>ứng<br>được tiêu|                |---|---|---|---|---|---| |4|Đánh giá<br>năng<br>lực<br>làm<br> chủ<br>sản phẩm,<br>các<br>  sản<br>phẩm<br>DBMS và<br>hệ<br>điều<br>hành<br>hỗ<br>trợ|Đơn vị triển khai cài đặt và<br>Đơn vị vận hành hạ tầng<br>lưu trữ đánh giá năng lực<br>làm chủ sản phẩm. Ưu tiên<br>chọn sản phẩm mà đội dự<br>án am hiểu và thành thạo<br>nhất và vận hành đơn giản,<br>ít lỗi.<br>Trường hợp là hạ tầng lưu<br>trữ mới thì cần phải có<br>đánh giá thử nghiệp trước<br>khi ra quyết định lựa chọn.<br>Biểu mẫu đánh giá lựa<br>chọn từ Bước 1,2,3,4 xem<br>trong**Phụ lục 04.**|ĐV<br>QHĐC|Các use<br>cases<br>đội<br>dự án đã<br>triển<br>khai<br>hoặc tham<br>khảo từ các<br>đơn vị<br>khác.<br>Biên<br>bản<br>đánh<br>giá<br>kết quả thử<br>nghiệp theo<br>các tiêu chí<br>công  nghệ<br>được<br>ưu<br>tiên.|Kết<br>quả<br>lựa<br>chọn<br>hạ<br>tầng<br>lưu<br>trữ<br>được Lãnh<br>đạo đơn vị<br>QHĐC và<br>Lãnh đạo<br>đơn vị vận<br>hành   hạ<br>tầng lưu<br>trữ<br>phê<br>duyệt.| |5|Xây dựng<br>CTKT về<br>Hạ<br>tầng<br>lưu trữ|Đội dự án đưa đưa kết quả<br>lựa chọn hạ tầng lưu trữ ở<br>Bước 4 vào CTKT mua<br>sắm đầu tư mới hạ tầng lưu<br>trữ theo QĐ 3208/QyĐ-<br>CNVTQĐ-VTNet.|ĐV<br>QHĐC|Căn cứ vào<br>kết quả phê<br>duyệt lựa<br>chọn<br>hạ<br>tầng lưu trữ|CTKT hạ<br>tầng<br>lưu<br>trữ|     - Vai trò của các bên liên quan         |---|---|---|---|---| |2.|Đánh giá, phân tích các tiêu chí về<br>công nghệ, chi phí, và khả năng làm<br>chủ công nghệ|I|A/R|R| |3.|Thẩm định và phê duyệt lựa chọn hạ<br>tầng lưu trữ|R|A|R| |4.|Đưa kết quả lựa chọn hạ tầng lưu trữ<br>vào CTKTphần mềm|I|A/R|C|

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
<td>Đơn vị/vai trò chịụ trách nhiệm giải trình k~~ế~~t quả của hoạt động</td>
</tr>
<tr>
<td>R</td>
<td>Đơn vị/vai trò chịu trách nhiệm thực hiện hoạt động<br></td>
</tr>
<tr>
<td>S</td>
<td>Đơn vị/vai trò cung c~~ấ~~p ngu~~ồ~~n lực và hỗ trợ thực hiện hoạt động</td>
</tr>
<tr>
<td>C</td>
<td>Đơn vị/vai trò cung cấp thông tin và tư vấn hỗ trợ trước và trong quá<br>trình thực hiện hoạt động</td>
</tr>
<tr>
<td>I</td>
<td>Đơn vị/vai trò được thông báo/cung cấp thông tin sau khi hoạt động<br>được thực hiện</td>
</tr>
</tbody>
</table>
|---|---| |A|Đơn vị/vai trò chịụ trách nhiệm giải trình k~~ế~~t quả của hoạt động| |R|Đơn vị/vai trò chịu trách nhiệm thực hiện hoạt động<br>| |S|Đơn vị/vai trò cung c~~ấ~~p ngu~~ồ~~n lực và hỗ trợ thực hiện hoạt động| |C|Đơn vị/vai trò cung cấp thông tin và tư vấn hỗ trợ trước và trong quá<br>trình thực hiện hoạt động| |I|Đơn vị/vai trò được thông báo/cung cấp thông tin sau khi hoạt động<br>được thực hiện|

# Tiêu chí, chỉ số đánh giá việc thực hiện quy trình

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Miêutả KPI</th>
<th>Công thức tính : Tỉ lệ tuâ n thủ quy trì nh = Tổ ng sốd ự á n cóbá ocá o l ựa<br>ch ọn h ạ tầ ng l ưu trữ đú ng quy trì nh trướ c khi xâ y d ựng CTKT/ Tổ ng số<br>d á<br>ự n<br>.<br>Cáchtính :Hàngquýđơnvị chị utrách nhiệmràsoátvàlấ ysốlượngtrên<br>hệ thố ng để tính tỉ lệ<br>.</th>
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
<td>Đơn vị chịu<br>trách<br>nhiệm<br>thực hiện KPI</td>
<td>ĐV QHĐC</td>
</tr>
</tbody>
</table>
|---|---| |Mục đích KPI|Quản lý việc tuân thủquy trình.| |Ngưỡng KPI<br>mục tiêu|>=90% (Kiểm tra thử nghiệm sau 3 tháng sau đó sẽ điều chỉnh ngưỡng<br>KPI theo thực tế)| |Đơn vị chịu<br>trách<br>nhiệm<br>thực hiện KPI|ĐV QHĐC|

# Phụ lục đính kèm

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
<th>Mã số</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Phụ lục 01_Các tiêu chí lựa chọn hạ t~~ầ~~ng lưu trữ<br></td>
<td>PL01</td>
</tr>
<tr>
<td>2</td>
<td>Phụ lục 02 Các loại hạ t~~ầ~~ng lưu trữph~~ổ~~ bi~~ế~~n</td>
<td>PL02</td>
</tr>
<tr>
<td>3</td>
<td>Phụ lục 03 So sánh về giá cả và hiệu năng giữa các<br>loại hạ tầng lưu trữphổ biến<br></td>
<td>PL03</td>
</tr>
<tr>
<td>4</td>
<td>Phụ lục 04 Bi~~ể~~u mẫu đánhgiá t~~ổ~~ng hợp</td>
<td>PL04</td>
</tr>
<tr>
<td>5</td>
<td>Phụ lục 05 Danh sách Use cases các hạ tầng lưu trữ<br>phổ biến tại Viettel</td>
<td>PL05</td>
</tr>
</tbody>
</table>
|---|---|---| |1|Phụ lục 01_Các tiêu chí lựa chọn hạ t~~ầ~~ng lưu trữ<br>|PL01| |2|Phụ lục 02 Các loại hạ t~~ầ~~ng lưu trữph~~ổ~~ bi~~ế~~n|PL02| |3|Phụ lục 03 So sánh về giá cả và hiệu năng giữa các<br>loại hạ tầng lưu trữphổ biến<br>|PL03| |4|Phụ lục 04 Bi~~ể~~u mẫu đánhgiá t~~ổ~~ng hợp|PL04| |5|Phụ lục 05 Danh sách Use cases các hạ tầng lưu trữ<br>phổ biến tại Viettel|PL05|