# Public_328

### Mục đích

“Hướng dẫn lựa chọn kỹ thuật AI” cung cấp một khuôn khổ tư duy có hệ thống, giúp các tổ chức và doanh nghiệp nhận diện đúng bản chất bài toán AI, đồng thời lựa chọn chính xác các kỹ thuật phù hợp với mục tiêu và điều kiện triển khai. Việc chuẩn hóa cách phân loại bài toán và kỹ thuật AI không chỉ giúp tối ưu nguồn lực đầu tư mà còn đảm bảo tính nhất quán, minh bạch và hiệu quả trong toàn bộ vòng đời phát triển và vận hành giải pháp AI.

### Đối tượng áp dụng

Hướng dẫn áp dụng với các dự án phát triển sản phẩm ứng dụng học máy, trí tuệ nhân tạo tại các đơn vị trong Tập đoàn.

### Định nghĩa, thuật ngữ và viết tắt

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>STT</th>
<th>Thuật ngữ & viế t tắ t</th>
<th>Giải thí ch</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>CNTT</td>
<td>Công nghệ thông tin</td>
</tr>
<tr>
<td>2</td>
<td>AI</td>
<td>Artificial Intelligence:<br>Lĩnh vực khoa học máy<br>tính nghiên cứu và phát<br>triển các hệ thống có khả<br>năng thực hiện những tác<br>vụ đòi hỏi trí tuệ tương<br>đương con người.</td>
</tr>
<tr>
<td>3</td>
<td>GPU</td>
<td>Graphics Processing<br>Unit: Vi xử lý chuyên<br>dụng tối ưu cho tính toán<br>song song cường độ cao,</td>
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
<th>STT</th>
<th>Thuật ngữ & viế t tắ t</th>
<th>Giải thí ch</th>
</tr>
</thead>
<tbody>
<tr>
<td>thường được sử dụng<br>trong huấn luyện mô hình<br>DL.</td>
</tr>
<tr>
<td>4</td>
<td>TPU</td>
<td>Tensor Processing Unit:<br>Vi xử lý do Google phát<br>triển, tối ưu cho các phép<br>toán tensor thường dùng<br>trong huấn luyện và suy<br>luận DL.</td>
</tr>
<tr>
<td>5</td>
<td>GAN</td>
<td>Generative Adversarial<br>Network: Mô hình<br>Generative AI gồm hai<br>mạng (generator,<br>discriminator) thi đua<br>nhau để sinh dữ liệu có<br>phân phối giống dữ liệu<br>thật.</td>
</tr>
<tr>
<td>6</td>
<td>VAE</td>
<td>Variational Autoencoder:<br>Mô hình Generative AI<br>học phân phối tiềm ẩn để<br>sinh dữ liệu mới qua cơ<br>chế mã hóa–giải mã với<br>chuẩn hóa xác suất.</td>
</tr>
<tr>
<td>7</td>
<td>GPT</td>
<td>Generative Pre-trained<br>Transformer: Mô hình</td>
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
<th>STT</th>
<th>Thuật ngữ & viế t tắ t</th>
<th>Giải thí ch</th>
</tr>
</thead>
<tbody>
<tr>
<td>transformer tiền huấn<br>luyện trên khối lượng lớn<br>văn bản, có khả năng<br>sinh ngôn ngữ tự nhiên.</td>
</tr>
<tr>
<td>8</td>
<td>Stable Diffusion</td>
<td>Kỹ thuật tạo ảnh từ nhiễu<br>dựa trên quá trình khuếch<br>tán ngược, kiểm soát chất<br>lượng và phong cách.</td>
</tr>
<tr>
<td>9</td>
<td>Whisper</td>
<td>Mô hình nhận diện giọng<br>nói của OpenAI, chuyển<br>đổi âm thanh giọng nói<br>thành văn bản.</td>
</tr>
<tr>
<td>10</td>
<td>MusicGen</td>
<td>Mô hình DL sinh nhạc tự<br>động theo phong cách và<br>cấu trúc đầu vào.</td>
</tr>
<tr>
<td>11</td>
<td>CNN</td>
<td>Convolutional Neural<br>Network: Mạng nơ-ron<br>tích chập, chuyên xử lý<br>dữ liệu lưới (ảnh, video)<br>bằng lớp tích chập để<br>trích xuất đặc trưng.</td>
</tr>
<tr>
<td>12</td>
<td>RNN</td>
<td>Recurrent Neural<br>Network: Mạng nơ-ron<br>hồi tiếp, phù hợp xử lý<br>dữ liệu tuần tự nhờ liên</td>
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
<th>STT</th>
<th>Thuật ngữ & viế t tắ t</th>
<th>Giải thí ch</th>
</tr>
</thead>
<tbody>
<tr>
<td>kết trạng thái qua thời<br>gian.</td>
</tr>
<tr>
<td>13</td>
<td>LSTM</td>
<td>Long Short-Term<br>Memory: Biến thể của<br>RNN, giúp duy trì thông<br>tin dài hạn qua cổng nhớ.</td>
</tr>
<tr>
<td>14</td>
<td>GRU</td>
<td>Gated Recurrent Unit:<br>Biến thể RNN tích hợp<br>cổng cập nhật và khôi<br>phục, đơn giản hóa cấu<br>trúc so với LSTM.</td>
</tr>
<tr>
<td>15</td>
<td>Transformer</td>
<td>Kiến trúc mạng dựa trên<br>cơ chế self-attention, xử<br>lý song song và đạt hiệu<br>quả cao trong NLP.</td>
</tr>
<tr>
<td>16</td>
<td>ResNet</td>
<td>Residual Network: Mạng<br>nơ-ron với kết nối tắt<br>(skip connection), giảm<br>thiểu mất mát thông tin<br>khi mô hình sâu tầng.</td>
</tr>
<tr>
<td>17</td>
<td>EfficientNet</td>
<td>Kiến trúc CNN tự động<br>cân chỉnh độ sâu, độ rộng<br>và độ phân giải để tối ưu<br>hiệu suất.</td>
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
<th>STT</th>
<th>Thuật ngữ & viế t tắ t</th>
<th>Giải thí ch</th>
</tr>
</thead>
<tbody>
<tr>
<td>18</td>
<td>SVM</td>
<td>Support Vector Machine:<br>thuật toán học có giám<br>sát, phân loại bằng cách<br>tìm siêu phẳng tối ưu<br>phân tách các lớp dữ liệu.</td>
</tr>
<tr>
<td>19</td>
<td>KNN</td>
<td>k-Nearest Neighbors:<br>thuật toán học máy có<br>giám sát, phân loại dựa<br>trên nhãn của k mẫu gần<br>nhất trong không gian<br>đặc trưng.</td>
</tr>
<tr>
<td>20</td>
<td>DBSCAN</td>
<td>Density-Based Spatial<br>Clustering of<br>Applications with Noise:<br>thuật toán học máy<br>không giám sát, phân<br>nhóm dữ liệu dựa trên<br>mật độ, tự động phát hiện<br>điểm nhiễu.</td>
</tr>
<tr>
<td>21</td>
<td>XGBoost</td>
<td>Extreme Gradient<br>Boosting: Thuật toán học<br>máy có giám sát dựa trên<br>kỹ thuật tăng cường<br>(boosting), sử dụng nhiều<br>cây quyết định liên tiếp</td>
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
<th>STT</th>
<th>Thuật ngữ & viế t tắ t</th>
<th>Giải thí ch</th>
</tr>
</thead>
<tbody>
<tr>
<td>để tối ưu độ chính xác.<br>Thuật toán tập trung vào<br>khả năng xử lý dữ liệu bị<br>thiếu, kiểm soát tình<br>trạng quá khớp<br>(overfitting) tốt.</td>
</tr>
<tr>
<td>22</td>
<td>LightGBM</td>
<td>Light Gradient Boosting<br>Machine: Thuật toán học<br>máy có giám sát dựa trên<br>kỹ thuật boosting, sử<br>dụng nhiều cây quyết<br>định liên tiếp để tối ưu độ<br>chính xác. Thuật toán tập<br>trung vào các kỹ thuật<br>giúp tăng tốc độ huấn<br>luyện, giảm bộ nhớ tiêu<br>thụ.</td>
</tr>
<tr>
<td>23</td>
<td>K-means</td>
<td>Thuật toán phân cụm<br>không giám sát, nhóm dữ<br>liệu thành k cụm để tối<br>thiểu hoá khoảng cách tới<br>tâm cụm.</td>
</tr>
<tr>
<td>24</td>
<td>PCA</td>
<td>Principal Component<br>Analysis: Phương pháp<br>giảm chiều bằng cách</td>
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
<th>STT</th>
<th>Thuật ngữ & viế t tắ t</th>
<th>Giải thí ch</th>
</tr>
</thead>
<tbody>
<tr>
<td>chiếu dữ liệu lên trục<br>chính có phương sai lớn<br>nhất.</td>
</tr>
<tr>
<td>25</td>
<td>t-SNE</td>
<td>t-Distributed Stochastic<br>Neighbor Embedding:<br>Phương pháp giảm chiều<br>phi tuyến, giữ cấu trúc<br>không gian cục bộ khi<br>trực quan hóa dữ liệu cao<br>chiều.</td>
</tr>
<tr>
<td>26</td>
<td>Isolation Forest</td>
<td>Thuật toán phát hiện bất<br>thường, cô lập điểm dữ<br>liệu khác biệt qua mô<br>hình rừng cây ngẫu<br>nhiên.</td>
</tr>
</tbody>
</table>
|---|---|---| |1|CNTT|Công nghệ thông tin| |2|AI|Artificial Intelligence:<br>Lĩnh vực khoa học máy<br>tính nghiên cứu và phát<br>triển các hệ thống có khả<br>năng thực hiện những tác<br>vụ đòi hỏi trí tuệ tương<br>đương con người.| |3|GPU|Graphics Processing<br>Unit: Vi xử lý chuyên<br>dụng tối ưu cho tính toán<br>song song cường độ cao,|    1    |<image_1>|   |<image_2>|   |<image_3>|               |---|---|---| |||thường được sử dụng<br>trong huấn luyện mô hình<br>DL.| |4|TPU|Tensor Processing Unit:<br>Vi xử lý do Google phát<br>triển, tối ưu cho các phép<br>toán tensor thường dùng<br>trong huấn luyện và suy<br>luận DL.| |5|GAN|Generative Adversarial<br>Network: Mô hình<br>Generative AI gồm hai<br>mạng (generator,<br>discriminator) thi đua<br>nhau để sinh dữ liệu có<br>phân phối giống dữ liệu<br>thật.| |6|VAE|Variational Autoencoder:<br>Mô hình Generative AI<br>học phân phối tiềm ẩn để<br>sinh dữ liệu mới qua cơ<br>chế mã hóa–giải mã với<br>chuẩn hóa xác suất.| |7|GPT|Generative Pre-trained<br>Transformer: Mô hình|    2                  |---|---|---| |||transformer tiền huấn<br>luyện trên khối lượng lớn<br>văn bản, có khả năng<br>sinh ngôn ngữ tự nhiên.| |8|Stable Diffusion|Kỹ thuật tạo ảnh từ nhiễu<br>dựa trên quá trình khuếch<br>tán ngược, kiểm soát chất<br>lượng và phong cách.| |9|Whisper|Mô hình nhận diện giọng<br>nói của OpenAI, chuyển<br>đổi âm thanh giọng nói<br>thành văn bản.| |10|MusicGen|Mô hình DL sinh nhạc tự<br>động theo phong cách và<br>cấu trúc đầu vào.| |11|CNN|Convolutional Neural<br>Network: Mạng nơ-ron<br>tích chập, chuyên xử lý<br>dữ liệu lưới (ảnh, video)<br>bằng lớp tích chập để<br>trích xuất đặc trưng.| |12|RNN|Recurrent Neural<br>Network: Mạng nơ-ron<br>hồi tiếp, phù hợp xử lý<br>dữ liệu tuần tự nhờ liên|    3                  |---|---|---| |||kết trạng thái qua thời<br>gian.| |13|LSTM|Long Short-Term<br>Memory: Biến thể của<br>RNN, giúp duy trì thông<br>tin dài hạn qua cổng nhớ.| |14|GRU|Gated Recurrent Unit:<br>Biến thể RNN tích hợp<br>cổng cập nhật và khôi<br>phục, đơn giản hóa cấu<br>trúc so với LSTM.| |15|Transformer|Kiến trúc mạng dựa trên<br>cơ chế self-attention, xử<br>lý song song và đạt hiệu<br>quả cao trong NLP.| |16|ResNet|Residual Network: Mạng<br>nơ-ron với kết nối tắt<br>(skip connection), giảm<br>thiểu mất mát thông tin<br>khi mô hình sâu tầng.| |17|EfficientNet|Kiến trúc CNN tự động<br>cân chỉnh độ sâu, độ rộng<br>và độ phân giải để tối ưu<br>hiệu suất.|    4                |---|---|---| |18|SVM|Support Vector Machine:<br>thuật toán học có giám<br>sát, phân loại bằng cách<br>tìm siêu phẳng tối ưu<br>phân tách các lớp dữ liệu.| |19|KNN|k-Nearest Neighbors:<br>thuật toán học máy có<br>giám sát, phân loại dựa<br>trên nhãn của k mẫu gần<br>nhất trong không gian<br>đặc trưng.| |20|DBSCAN|Density-Based Spatial<br>Clustering of<br>Applications with Noise:<br>thuật toán học máy<br>không giám sát, phân<br>nhóm dữ liệu dựa trên<br>mật độ, tự động phát hiện<br>điểm nhiễu.| |21|XGBoost|Extreme Gradient<br>Boosting: Thuật toán học<br>máy có giám sát dựa trên<br>kỹ thuật tăng cường<br>(boosting), sử dụng nhiều<br>cây quyết định liên tiếp|    5              |---|---|---| |||để tối ưu độ chính xác.<br>Thuật toán tập trung vào<br>khả năng xử lý dữ liệu bị<br>thiếu, kiểm soát tình<br>trạng quá khớp<br>(overfitting) tốt.| |22|LightGBM|Light Gradient Boosting<br>Machine: Thuật toán học<br>máy có giám sát dựa trên<br>kỹ thuật boosting, sử<br>dụng nhiều cây quyết<br>định liên tiếp để tối ưu độ<br>chính xác. Thuật toán tập<br>trung vào các kỹ thuật<br>giúp tăng tốc độ huấn<br>luyện, giảm bộ nhớ tiêu<br>thụ.| |23|K-means|Thuật toán phân cụm<br>không giám sát, nhóm dữ<br>liệu thành k cụm để tối<br>thiểu hoá khoảng cách tới<br>tâm cụm.| |24|PCA|Principal Component<br>Analysis: Phương pháp<br>giảm chiều bằng cách|    6            |---|---|---| |||chiếu dữ liệu lên trục<br>chính có phương sai lớn<br>nhất.| |25|t-SNE|t-Distributed Stochastic<br>Neighbor Embedding:<br>Phương pháp giảm chiều<br>phi tuyến, giữ cấu trúc<br>không gian cục bộ khi<br>trực quan hóa dữ liệu cao<br>chiều.| |26|Isolation Forest|Thuật toán phát hiện bất<br>thường, cô lập điểm dữ<br>liệu khác biệt qua mô<br>hình rừng cây ngẫu<br>nhiên.|

### Các kỹ thuật AI

Các kỹ thuật AI được chia thành 3 kỹ thuật chính: (1) Học máy (Machine Learning – ML); (2) Học sâu (Deep Learning –  DL); (3) Trí tuệ nhân tạo tạo sinh (Generative AI – GenAI). Mỗi kỹ thuật sở hữu những ưu điểm và hạn chế đặc thù — từ khả năng giải thích rõ ràng, hiệu suất cao của ML, đến sức mạnh xử lý dữ liệu phi cấu trúc của DL và khả năng sáng tạo của GenAI. Cụ thể như sau:
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
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
<th>Kỹ<br>thuật</th>
<th>Định nghĩa</th>
<th>Ư điể<br>u m</th>
<th>Nhượcđiể<br>m</th>
<th>Ứ ngdụngđiể<br>n<br>hình</th>
<th>Thuậttoánđiể<br>n<br>hìn h</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><br>ML1</td>
<td>- Kỹ thuật AI sử<br>dụng thuật toán<br>thống kê để học từ<br>dữ liệu quá khứ và<br>đưa ra dự đoán mà<br>không cần lập trình<br>tường minh.</td>
<td>- Xử lý tốt dữ liệu<br>có cấu trúc.<br>- Một số thuật toán<br>có khả năng giải<br>thích được và tốt<br>hơn học sâu.<br>- Chi phí tính toán thấp<br>hơn<br>học sâu.<br>- Mạnh với dữ liệu<br>vừa và nhỏ.</td>
<td><br>- Hiệu suất kém với dữ liệu phi<br>cấu trúc (ảnh, video, âm thanh,<br>văn bản).<br>- Cần bước trích chọn đặc<br>trưng thủ công.<br>- Độ chính xác giới hạn với bài<br>toán có mẫu phức tạp.<br>- Giới hạn khả năng khai thác<br>tương tác giữa các đặc trưng<br>phức tạp (phi tuyến).</td>
<td>- Dự báo nhu cầu,<br>dự báo doanh<br>thu.<br>- Phân loại tín<br>dụng, rủi ro.<br>- Phát hiện gian<br>lận.<br>Dự đoán khách<br>hàng<br>rời mạng.</td>
<td>- Linear Regression,<br>Logistic Regression.<br>- Decision Tree,<br>Random Forest.<br>- Gradient<br>Boosting,<br>XGBoost,<br>LightGBM.<br>- SVM, KNN,<br>- Naive Bayes.<br>- K-means,<br>DBSCAN</td>
</tr>
<tr>
<td>2</td>
<td>DL2</td>
<td>Nhánh của ML sử dụng<br>mạng nơ-ron sâu<br>(Deep Neural Networks<br>– DNN) có khả năng tự<br>động học biểu diễn từ dữ<br>liệu.<br></td>
<td><br> <br>- Tự động trích<br>xuất đặc trưng từ<br>dữ liệu.<br>- Xử lý mạnh dữ liệu phi<br>cấu trúc (ảnh, âm thanh,<br>văn bản, video).<br>- Hỗ trợ học đa<br>phương thức bao<br>gồm ảnh, văn bản,<br>dữ liệu bảng...<br>- Tối ưu hóa tốt cho<br>các bài toán có dữ<br>liệu lớn, phức tạp.<br>- Đạt độ chính xác rất<br><br><br><br><br></td>
<td><br>- Yêu cầu dữ liệu rất lớn và tài<br>nguyên<br>phần<br>cứng<br>mạnh<br>(GPU/TPU).<br>- Tính đóng, khó giải thích.<br>- Chi phí tính toán cao, độ trễ cao<br>khi suy luận.<br>- Dễ bị quá khớp(overfitting)<br>nếu không có dữ liệu hoặc kỹ<br>thuật chính quy hóa<br>(regularization) tốt.<br>- Quá trình huấn luyện phức tạp,<br>nhạy với các siêu tham số, do đó<br>cần tinh chỉnh kỹ lưỡng.<br><br><br><br></td>
<td><br> <br>- Nhận diện<br>khuôn mặt, y tế<br>chẩn đoán hình<br>ảnh.<br>- Phân tích văn bản,<br>phân tích cảm xúc.<br>- Dịch máy,<br>nhận dạng<br>tiếng nói.<br>- Phát hiện đối tượng<br>trong video.</td>
<td>- CNN<br>- RNN, LSTM,<br>GRU<br>- Transformer<br>- ResNet,<br>EfficientNet</td>
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
<col/>
</colgroup>
<thead>
<tr>
<th>STT</th>
<th>Kỹ<br>thuật</th>
<th>Định nghĩa</th>
<th>Ư điể<br>u m</th>
<th>Nhượcđiể<br>m</th>
<th>Ứ ngdụngđiể<br>n<br>hình</th>
<th>Thuậttoánđiể<br>n<br>hìn h</th>
</tr>
</thead>
<tbody>
<tr>
<td>cao trong thị giác<br>máy tính, xử lý ngôn<br>ngữ tự nhiên.</td>
</tr>
<tr>
<td>3</td>
<td><br>GenAI</td>
<td>Nhánh của học sâu sử<br>dụng các mô hình có<br>khả năng sinh ra dữ liệu<br>mới (văn bản, hình ảnh,<br>âm thanh, video, code,<br>nhạc).</td>
<td>- Sinh nội dung sáng tạo<br>(văn bản, ảnh, video,<br>nhạc, code).<br>- Học biểu diễn phức<br>tạp từ dữ liệu phi cấu<br>trúc.<br>- Tăng tốc quy trình<br>sáng tạo, lập trình,<br>nghiên cứu và phát<br>triển (R&D).<br>- Hỗ trợ xây dựng dữ<br>liệu<br>tổng<br>hợp<br>(synthetic<br>data)<br>để<br>huấn luyện mô hình<br>khác.<br>- Kết hợp mạnh với tạo<br>sinh dựa trên truy xuất<br>tăng cường (RAG), hỗ<br>trợ bài toán doanh<br>nghiệp phức tạp.</td>
<td>- Chi phí tính toán rất cao.<br>- Đầu ra có thể chứa thông tin<br>sai lệch, thiên kiến (bias), ảo<br>giác (hallucination).<br>- Độ tin cậy phụ thuộc mạnh<br>vào prompt, chất lượng tinh<br>chỉnh mô hình (fine tune).<br>- Vấn đề về bản quyền, đạo đức<br>và kiểm duyệt nội dung.<br>- Khó kiểm soát chính xác logic<br>nội tại của mô hình.</td>
<td>- Sinh nội dung<br>truyền thông<br>- Trợ lý lập trình:<br>sinh mã nguồn,<br>sinh tài liệu phân<br>tích.<br>- Trợ lý ảo cho<br>doanh nghiệp.<br>- Tạo dữ liệu tổng<br>hợp trong nghiên<br>cứu y học, sản<br>xuất.</td>
<td><br>- GPT.<br>- Stable Diffusion<br>- Whisper.<br>- MusicGen.<br>- GAN, VAE</td>
</tr>
</tbody>
</table>
_Bảng 1. Các kỹ thuật AI_    7    |<image_4>|                                                               |---|---|---|---|---|---|---| |1|<br>ML1|- Kỹ thuật AI sử<br>dụng thuật toán<br>thống kê để học từ<br>dữ liệu quá khứ và<br>đưa ra dự đoán mà<br>không cần lập trình<br>tường minh.|- Xử lý tốt dữ liệu<br>có cấu trúc.<br>- Một số thuật toán<br>có khả năng giải<br>thích được và tốt<br>hơn học sâu.<br>- Chi phí tính toán thấp<br>hơn<br>học sâu.<br>- Mạnh với dữ liệu<br>vừa và nhỏ.|<br>- Hiệu suất kém với dữ liệu phi<br>cấu trúc (ảnh, video, âm thanh,<br>văn bản).<br>- Cần bước trích chọn đặc<br>trưng thủ công.<br>- Độ chính xác giới hạn với bài<br>toán có mẫu phức tạp.<br>- Giới hạn khả năng khai thác<br>tương tác giữa các đặc trưng<br>phức tạp (phi tuyến).|- Dự báo nhu cầu,<br>dự báo doanh<br>thu.<br>- Phân loại tín<br>dụng, rủi ro.<br>- Phát hiện gian<br>lận.<br>Dự đoán khách<br>hàng<br>rời mạng.|- Linear Regression,<br>Logistic Regression.<br>- Decision Tree,<br>Random Forest.<br>- Gradient<br>Boosting,<br>XGBoost,<br>LightGBM.<br>- SVM, KNN,<br>- Naive Bayes.<br>- K-means,<br>DBSCAN| |2|DL2|Nhánh của ML sử dụng<br>mạng nơ-ron sâu<br>(Deep Neural Networks<br>– DNN) có khả năng tự<br>động học biểu diễn từ dữ<br>liệu.<br>|<br> <br>- Tự động trích<br>xuất đặc trưng từ<br>dữ liệu.<br>- Xử lý mạnh dữ liệu phi<br>cấu trúc (ảnh, âm thanh,<br>văn bản, video).<br>- Hỗ trợ học đa<br>phương thức bao<br>gồm ảnh, văn bản,<br>dữ liệu bảng...<br>- Tối ưu hóa tốt cho<br>các bài toán có dữ<br>liệu lớn, phức tạp.<br>- Đạt độ chính xác rất<br><br><br><br><br>|<br>- Yêu cầu dữ liệu rất lớn và tài<br>nguyên<br>phần<br>cứng<br>mạnh<br>(GPU/TPU).<br>- Tính đóng, khó giải thích.<br>- Chi phí tính toán cao, độ trễ cao<br>khi suy luận.<br>- Dễ bị quá khớp(overfitting)<br>nếu không có dữ liệu hoặc kỹ<br>thuật chính quy hóa<br>(regularization) tốt.<br>- Quá trình huấn luyện phức tạp,<br>nhạy với các siêu tham số, do đó<br>cần tinh chỉnh kỹ lưỡng.<br><br><br><br>|<br> <br>- Nhận diện<br>khuôn mặt, y tế<br>chẩn đoán hình<br>ảnh.<br>- Phân tích văn bản,<br>phân tích cảm xúc.<br>- Dịch máy,<br>nhận dạng<br>tiếng nói.<br>- Phát hiện đối tượng<br>trong video.|- CNN<br>- RNN, LSTM,<br>GRU<br>- Transformer<br>- ResNet,<br>EfficientNet|    8                    |---|---|---|---|---|---|---| ||||cao trong thị giác<br>máy tính, xử lý ngôn<br>ngữ tự nhiên.|||| |3|<br>GenAI|Nhánh của học sâu sử<br>dụng các mô hình có<br>khả năng sinh ra dữ liệu<br>mới (văn bản, hình ảnh,<br>âm thanh, video, code,<br>nhạc).|- Sinh nội dung sáng tạo<br>(văn bản, ảnh, video,<br>nhạc, code).<br>- Học biểu diễn phức<br>tạp từ dữ liệu phi cấu<br>trúc.<br>- Tăng tốc quy trình<br>sáng tạo, lập trình,<br>nghiên cứu và phát<br>triển (R&D).<br>- Hỗ trợ xây dựng dữ<br>liệu<br>tổng<br>hợp<br>(synthetic<br>data)<br>để<br>huấn luyện mô hình<br>khác.<br>- Kết hợp mạnh với tạo<br>sinh dựa trên truy xuất<br>tăng cường (RAG), hỗ<br>trợ bài toán doanh<br>nghiệp phức tạp.|- Chi phí tính toán rất cao.<br>- Đầu ra có thể chứa thông tin<br>sai lệch, thiên kiến (bias), ảo<br>giác (hallucination).<br>- Độ tin cậy phụ thuộc mạnh<br>vào prompt, chất lượng tinh<br>chỉnh mô hình (fine tune).<br>- Vấn đề về bản quyền, đạo đức<br>và kiểm duyệt nội dung.<br>- Khó kiểm soát chính xác logic<br>nội tại của mô hình.|- Sinh nội dung<br>truyền thông<br>- Trợ lý lập trình:<br>sinh mã nguồn,<br>sinh tài liệu phân<br>tích.<br>- Trợ lý ảo cho<br>doanh nghiệp.<br>- Tạo dữ liệu tổng<br>hợp trong nghiên<br>cứu y học, sản<br>xuất.|<br>- GPT.<br>- Stable Diffusion<br>- Whisper.<br>- MusicGen.<br>- GAN, VAE|    9      1 Lưu ý: ML là khái niệm tổng quát bao gồm tất cả các phương pháp cho phép hệ thống học từ dữ liệu, bao gồm cả học sâu. Tuy nhiên trong tài liệu này, khi đề cập tới ML, ngầm hiểu là ML cổ điển, bao gồm lớp thuật toán thống kê, không bao gồm kiến trúc mạng nơ-ron sâu đặc trưng của học sâu.
2 Lưu ý: DL là tập hợp các kỹ thuật học dựa trên kiến trúc mạng nơ-ron sâu, bao gồm cả mô hình dự đoán và mô hình sinh. Tuy nhiên trong tài liệu này, trí tuệ nhân tạo tạo sinh được tách riêng khỏi học sâu để nhấn mạnh nhóm mô hình có mục tiêu sinh dữ liệu mới (văn bản, hình ảnh, âm thanh…). Vì vậy, khi đề cập tới học sâu, ngầm hiểu là nhóm mô hình học sâu với mục tiêu dự đoán, nhận diện, không bao gồm nhóm mô hình sinh dữ liệu.

### Bộ tiêu chí đánh giá mức độ phù hợp của các kỹ thuật AI

 * Để lựa chọn kỹ thuật AI phù hợp với từng bài toán cụ thể trong doanh nghiệp, cần thiết lập một bộ tiêu chí đánh giá rõ  ràng. Các tiêu chí này giúp tổ chức hiểu đúng bản chất bài toán, đặc điểm dữ liệu, cũng như yêu cầu triển khai thực tế, từ đó giới hạn và đề xuất phạm vi kỹ thuật có thể áp dụng.
  * Để đánh giá mức độ phù hợp của các kỹ thuật AI với từng tiêu chí, tài liệu áp dụng thang đo 3 mức như sau:
   * Phù hợp (P): Kỹ thuật được thiết kế và hoạt động hiệu quả nhất cho tiêu chí này.
  * Cân nhắc (C): Kỹ thuật có thể đáp ứng tiêu chí trong một số điều kiện nhất định, hoặc khi được kết hợp với các kỹ  thuật khác, nhưng không phải là lựa chọn hàng đầu.
  * Không phù hợp (K): Kỹ thuật không phù hợp hoặc hoạt động kém hiệu quả cho tiêu chí này.
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
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
<th>Tiêuchí</th>
<th>Thuộctính<br>đánh giá</th>
<th>Định nghĩa</th>
<th>Đánhgiáchitiế<br>t</th>
<th>ML</th>
<th>DL</th>
<th>Gen<br>AI</th>
</tr>
</thead>
<tbody>
<tr>
<td><br>1</td>
<td><br>Mục tiêu<br>bài toán</td>
<td>Dự đoán</td>
<td>Dự báo biến liên<br>tục<br>(regression)<br>hoặc  phân<br>loại<br>nhãn (classification)<br>dựa trên tập dữ<br>liệu có nhãn.</td>
<td>- ML, DL phù hợp: bản chất của ML và DL là xây dựng mô hình<br>học ánh xạ từ dữ liệu đầu vào tới một kết quả xác định.<br>- GenAI cân nhắc: vì GenAI không được thiết kế cho bài toán dự<br>đoán, tuy nhiên có thể sử dụng trong một số trường hợp đặc biệt<br>như sinh kết quả dự đoán dựa trên ngữ cảnh, nhưng không phải<br>là lựa chọn tối ưu cho các bài toán dự đoán hoặc phân loại nhãn<br>rõ ràng.</td>
<td>**P**</td>
<td>**P**</td>
<td>_C _</td>
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
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>STT</th>
<th>Tiêuchí</th>
<th>Thuộctính<br>đánh giá</th>
<th>Định nghĩa</th>
<th>Đánhgiáchitiế<br>t</th>
<th>ML</th>
<th>DL</th>
<th>Gen<br>AI</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>Loại<br>dữ<br>liệu</td>
<td>Tạo sinh</td>
<td>Tạo mới dữ liệu<br>phi cấu trúc như<br>văn bản, hình ảnh,<br>video, âm thanh<br>hoặc mã nguồn.</td>
<td>- GenAI phù hợp: Đây là mục tiêu chính của GenAI<br>- DL cân nhắc: Các mô hình DL truyền thống không linh hoạt và<br>hiệu quả bằng các mô hình sinh hiện đại, tuy nhiên có thể cân<br>nhắc trong trường hợp dữ liệu không quá lớn.<br>- ML không phù hợp: Các thuật toán ML không có khả năng<br>sinh<br>dữ liệu mới.</td>
<td>**K**</td>
<td>**C **</td>
<td>**P**</td>
</tr>
<tr>
<td>2</td>
<td>Loại<br>dữ<br>liệu</td>
<td>Dữ liệu có<br>cấu trúc</td>
<td><br>Dữ liệu dạng bảng,<br>gồm hàng và cột<br>với kiểu dữ liệu rõ<br>ràng.</td>
<td>- ML phù hợp: Các thuật toán ML được tối ưu hóa để xử lý và<br>tìm ra các mối quan hệ trong dữ liệu có cấu trúc<br>- DL cân nhắc: DL có thể xử lý được có cấu trúc nhưng thường<br>không mang lại kết quả vượt trội so với ML mà lại tốn kém tài<br>nguyên hơn. Do đó DL không phải lựa chọn ưu tiên.<br>- GenAI không phù hợp: GenAI không được thiết kế để làm việc<br>với dữ liệu có cấu trúc.</td>
<td><br> <br>**P**</td>
<td><br>**C**</td>
<td><br>**K**</td>
</tr>
<tr>
<td>2</td>
<td>Loại<br>dữ<br>liệu</td>
<td>Dữ liệu phi<br>cấu trúc</td>
<td>Dữ liệu không có<br>cấu trúc bảng định<br>sẵn, bao gồm ảnh,<br>văn bản tự do, âm<br>thanh, video…</td>
<td>- ML không phù hợp: ML không xử lý trực tiếp dữ liệu phi cấu<br>trúc, cần phải trích xuất các đặc trưng thủ công trước khi áp dụng<br>mô hình, điều này rất tốn thời gian và không hiệu quả.<br>- DL và GenAI phù hợp: DL và GenAI đều được thiết kế để xử lý<br>dữ liệu phi cấu trúc thông qua các kiến trúc mạng nơ-ron sâu, có<br>khả năng học các đặc trưng phức tạp một cách tự động.</td>
<td><br> <br>**K**</td>
<td><br>**P**</td>
<td><br>**P**</td>
</tr>
<tr>
<td>3</td>
<td>Nhãn<br>dữ<br>liệu</td>
<td>Có nhãn rõ<br>ràng</td>
<td>Tập dữ liệu đã gán<br>nhãn đầu ra<br>(supervised).</td>
<td>- ML và DL phù hợp: Các kỹ thuật đều dựa trên dữ liệu có nhãn<br>để<br>học các mẫu và mối quan hệ.<br>- GenAI cân nhắc:</td>
<td>**P**</td>
<td>**P**</td>
<td>**C**</td>
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
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>STT</th>
<th>Tiêuchí</th>
<th>Thuộctính<br>đánh giá</th>
<th>Định nghĩa</th>
<th>Đánhgiáchitiế<br>t</th>
<th>ML</th>
<th>DL</th>
<th>Gen<br>AI</th>
</tr>
</thead>
<tbody>
<tr>
<td>Không nhãn</td>
<td>Tập dữ liệu chưa có<br>nhãn, cần khám phá<br>cấu trúc tiềm ẩn<br>(unsupervised).</td>
<td>- GenAI phù hợp: Kỹ thuật này học và tạo ra cấu trúc từ dữ liệu<br>thô, không cần nhãn.<br>- ML và DL cân nhắc: Trong trường hợp các bài toán<br>unsupervised, các kỹ thuật này có thể sử dụng để khám phá các<br>cấu trúc từ dữ liệu.</td>
<td>**C**</td>
<td>**C**</td>
<td>**P**</td>
</tr>
<tr>
<td>4</td>
<td>Số<br>chiều<br>dữ liệu</td>
<td>Số chiều dữ<br>liệu nhỏ</td>
<td>Dữ liệu có số lượng<br>đặc trưng (feature)<br>nhỏ.</td>
<td>- ML phù hợp: ML hoạt động hiệu quả với dữ liệu có ít feature<br>- DL và GenAI cân nhắc: Có thể cân nhắc sử dụng nhưng<br>thường không cần thiết và có nguy cơ overfitting.</td>
<td>**P**</td>
<td>**C**</td>
<td>**C**</td>
</tr>
<tr>
<td>4</td>
<td>Số<br>chiều<br>dữ liệu</td>
<td>Số chiều dữ<br>liệu lớn</td>
<td>Dữ liệu có số lượng<br>feature rất lớn</td>
<td>- DL và GenAI phù hợp: Kiến trúc mạng nơ-ron sâu được thiết<br>kế để xử lý và trích xuất đặc trưng từ dữ liệu có số chiều lớn một<br>cách tự động.<br>- ML không phù hợp: ML có hiệu suất kém và khó xử lý khi số<br>lượng đặc trưng tăng lên.</td>
<td>**K**</td>
<td>**P**</td>
<td>**P**</td>
</tr>
<tr>
<td><br>5</td>
<td><br>Số lượng<br>dữ liệu</td>
<td>Khối lượng dữ<br>liệu nhỏ</td>
<td><br>Tập dữ liệu nhỏ</td>
<td>- ML phù hợp: ML hoạt động tốt trên các tập dữ liệu nhỏ, yêu<br>cầu<br>ít tài nguyên tính toán và thường cho kết quả tốt.<br>- DL và GenAI cân nhắc: DL và GenAI đòi hỏi lượng lớn dữ liệu<br>để học các đặc trưng phức tạp. Với dữ liệu nhỏ, DL dễ bị<br>overfitting và kém hiệu quả. Tuy nhiên có thể cân nhắc nếu sử<br>dụng các mô hình đã được huấn luyện sẵn hoặc tinh chỉnh trên<br>dữ liệu nhỏ.</td>
<td>**P**</td>
<td>**C**</td>
<td>**C**</td>
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
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>STT</th>
<th>Tiêuchí</th>
<th>Thuộctính<br>đánh giá</th>
<th>Định nghĩa</th>
<th>Đánhgiáchitiế<br>t</th>
<th>ML</th>
<th>DL</th>
<th>Gen<br>AI</th>
</tr>
</thead>
<tbody>
<tr>
<td>Khối lượng dữ<br>liệu lớn</td>
<td><br>Tập dữ liệu lớn</td>
<td>- DL và GenAI phù hợp: Các kỹ thuật này có khả năng khai<br>thác<br>các mối quan hệ phức tạp từ dữ liệu lớn.<br>- ML cân nhắc: ML có thể hoạt động nhưng thường kém hiệu<br>quả hơn, đặc biệt khi dữ liệu có nhiều đặc trưng phức tạp.</td>
<td>**C**</td>
<td>**P**</td>
<td>**P**</td>
</tr>
<tr>
<td>6</td>
<td>Yêu cầu<br>khả năng<br>giải thích</td>
<td>Yêu cầu khả<br>năng giải thích<br>rõ ràng, dễ<br>kiểm tra</td>
<td><br>Yêu cầu khả năng<br>giải thích rõ ràng, dễ<br>kiểm tra nguyên<br>nhân mô hình đưa ra<br>quyết định cụ thể.</td>
<td><br> <br>- ML phù hợp: Các thuật toán ML như Linear regression,<br>Decision tree thường dễ giải thích, minh bạch và có thể kiểm tra<br>các quyết định của mô hình.<br>- DL và GenAI cân nhắc: Các kỹ thuật này dựa trên các mô hình<br>mang tính chất hộp đen (black-box), rất khó để giải thích và truy<br>vết nguyên nhân cụ thể. Tuy nhiên, có thể cân nhắc khi áp dụng<br>kết hợp các kỹ thuật giải thích mô hình bổ sung hoặc đối với<br>GenAI thì yêu cầu sinh phương pháp lý luận (tuy nhiên về bản<br>chất mô hình vẫn không diễn giải được)</td>
<td>**P**</td>
<td>**C **</td>
<td>**C **</td>
</tr>
</tbody>
</table>
  * Bảng 2. Bảng đánh giá mức độ phù hợp của các kỹ thuật AI theo từng tiêu chí                       |---|---|---|---|---|---|---|---| |<br>1|<br>Mục tiêu<br>bài toán|Dự đoán|Dự báo biến liên<br>tục<br>(regression)<br>hoặc  phân<br>loại<br>nhãn (classification)<br>dựa trên tập dữ<br>liệu có nhãn.|- ML, DL phù hợp: bản chất của ML và DL là xây dựng mô hình<br>học ánh xạ từ dữ liệu đầu vào tới một kết quả xác định.<br>- GenAI cân nhắc: vì GenAI không được thiết kế cho bài toán dự<br>đoán, tuy nhiên có thể sử dụng trong một số trường hợp đặc biệt<br>như sinh kết quả dự đoán dựa trên ngữ cảnh, nhưng không phải<br>là lựa chọn tối ưu cho các bài toán dự đoán hoặc phân loại nhãn<br>rõ ràng.|**P**|**P**|_C _|    10    |<image_5>|                                   |---|---|---|---|---|---|---|---| |2|Loại<br>dữ<br>liệu|Tạo sinh|Tạo mới dữ liệu<br>phi cấu trúc như<br>văn bản, hình ảnh,<br>video, âm thanh<br>hoặc mã nguồn.|- GenAI phù hợp: Đây là mục tiêu chính của GenAI<br>- DL cân nhắc: Các mô hình DL truyền thống không linh hoạt và<br>hiệu quả bằng các mô hình sinh hiện đại, tuy nhiên có thể cân<br>nhắc trong trường hợp dữ liệu không quá lớn.<br>- ML không phù hợp: Các thuật toán ML không có khả năng<br>sinh<br>dữ liệu mới.|**K**|**C **|**P**| |2|Loại<br>dữ<br>liệu|Dữ liệu có<br>cấu trúc|<br>Dữ liệu dạng bảng,<br>gồm hàng và cột<br>với kiểu dữ liệu rõ<br>ràng.|- ML phù hợp: Các thuật toán ML được tối ưu hóa để xử lý và<br>tìm ra các mối quan hệ trong dữ liệu có cấu trúc<br>- DL cân nhắc: DL có thể xử lý được có cấu trúc nhưng thường<br>không mang lại kết quả vượt trội so với ML mà lại tốn kém tài<br>nguyên hơn. Do đó DL không phải lựa chọn ưu tiên.<br>- GenAI không phù hợp: GenAI không được thiết kế để làm việc<br>với dữ liệu có cấu trúc.|<br> <br>**P**|<br>**C**|<br>**K**| |2|Loại<br>dữ<br>liệu|Dữ liệu phi<br>cấu trúc|Dữ liệu không có<br>cấu trúc bảng định<br>sẵn, bao gồm ảnh,<br>văn bản tự do, âm<br>thanh, video…|- ML không phù hợp: ML không xử lý trực tiếp dữ liệu phi cấu<br>trúc, cần phải trích xuất các đặc trưng thủ công trước khi áp dụng<br>mô hình, điều này rất tốn thời gian và không hiệu quả.<br>- DL và GenAI phù hợp: DL và GenAI đều được thiết kế để xử lý<br>dữ liệu phi cấu trúc thông qua các kiến trúc mạng nơ-ron sâu, có<br>khả năng học các đặc trưng phức tạp một cách tự động.|<br> <br>**K**|<br>**P**|<br>**P**| |3|Nhãn<br>dữ<br>liệu|Có nhãn rõ<br>ràng|Tập dữ liệu đã gán<br>nhãn đầu ra<br>(supervised).|- ML và DL phù hợp: Các kỹ thuật đều dựa trên dữ liệu có nhãn<br>để<br>học các mẫu và mối quan hệ.<br>- GenAI cân nhắc:|**P**|**P**|**C**|    11                              |---|---|---|---|---|---|---|---| |||Không nhãn|Tập dữ liệu chưa có<br>nhãn, cần khám phá<br>cấu trúc tiềm ẩn<br>(unsupervised).|- GenAI phù hợp: Kỹ thuật này học và tạo ra cấu trúc từ dữ liệu<br>thô, không cần nhãn.<br>- ML và DL cân nhắc: Trong trường hợp các bài toán<br>unsupervised, các kỹ thuật này có thể sử dụng để khám phá các<br>cấu trúc từ dữ liệu.|**C**|**C**|**P**| |4|Số<br>chiều<br>dữ liệu|Số chiều dữ<br>liệu nhỏ|Dữ liệu có số lượng<br>đặc trưng (feature)<br>nhỏ.|- ML phù hợp: ML hoạt động hiệu quả với dữ liệu có ít feature<br>- DL và GenAI cân nhắc: Có thể cân nhắc sử dụng nhưng<br>thường không cần thiết và có nguy cơ overfitting.|**P**|**C**|**C**| |4|Số<br>chiều<br>dữ liệu|Số chiều dữ<br>liệu lớn|Dữ liệu có số lượng<br>feature rất lớn|- DL và GenAI phù hợp: Kiến trúc mạng nơ-ron sâu được thiết<br>kế để xử lý và trích xuất đặc trưng từ dữ liệu có số chiều lớn một<br>cách tự động.<br>- ML không phù hợp: ML có hiệu suất kém và khó xử lý khi số<br>lượng đặc trưng tăng lên.|**K**|**P**|**P**| |<br>5|<br>Số lượng<br>dữ liệu|Khối lượng dữ<br>liệu nhỏ|<br>Tập dữ liệu nhỏ|- ML phù hợp: ML hoạt động tốt trên các tập dữ liệu nhỏ, yêu<br>cầu<br>ít tài nguyên tính toán và thường cho kết quả tốt.<br>- DL và GenAI cân nhắc: DL và GenAI đòi hỏi lượng lớn dữ liệu<br>để học các đặc trưng phức tạp. Với dữ liệu nhỏ, DL dễ bị<br>overfitting và kém hiệu quả. Tuy nhiên có thể cân nhắc nếu sử<br>dụng các mô hình đã được huấn luyện sẵn hoặc tinh chỉnh trên<br>dữ liệu nhỏ.|**P**|**C**|**C**|    12                            |---|---|---|---|---|---|---|---| |||Khối lượng dữ<br>liệu lớn|<br>Tập dữ liệu lớn|- DL và GenAI phù hợp: Các kỹ thuật này có khả năng khai<br>thác<br>các mối quan hệ phức tạp từ dữ liệu lớn.<br>- ML cân nhắc: ML có thể hoạt động nhưng thường kém hiệu<br>quả hơn, đặc biệt khi dữ liệu có nhiều đặc trưng phức tạp.|**C**|**P**|**P**| |6|Yêu cầu<br>khả năng<br>giải thích|Yêu cầu khả<br>năng giải thích<br>rõ ràng, dễ<br>kiểm tra|<br>Yêu cầu khả năng<br>giải thích rõ ràng, dễ<br>kiểm tra nguyên<br>nhân mô hình đưa ra<br>quyết định cụ thể.|<br> <br>- ML phù hợp: Các thuật toán ML như Linear regression,<br>Decision tree thường dễ giải thích, minh bạch và có thể kiểm tra<br>các quyết định của mô hình.<br>- DL và GenAI cân nhắc: Các kỹ thuật này dựa trên các mô hình<br>mang tính chất hộp đen (black-box), rất khó để giải thích và truy<br>vết nguyên nhân cụ thể. Tuy nhiên, có thể cân nhắc khi áp dụng<br>kết hợp các kỹ thuật giải thích mô hình bổ sung hoặc đối với<br>GenAI thì yêu cầu sinh phương pháp lý luận (tuy nhiên về bản<br>chất mô hình vẫn không diễn giải được)|**P**|**C **|**C **|

## **Các bài toán AI phổ biến**

# - Theo Viện tiêu chuẩn và Công nghệ Quốc gia của Hoa Kỳ (National Institute of Standards and Technology – NIST), bài toán AI được phân loại theo 14 bài toán phổ biến như sau: # Bảng 3. Bảng phân loại các bài toán AI phổ biến

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
<th>Tạonội<br>dun g</th>
<th>Tạoracácsảnphẩ m dữliệuhoặcnộidungmớidựatrên<br>các yêu cầ uho ặcmụ, c tiê uđư ợcx ácđ ịnhrõ ràn g<br>.</th>
<th>Tạophụđề tựđộngchovideoquảngcáo;sinhmãlậptrìnhtừ<br>m ô tả;tạo hìn hảnh từnội dung văn bản</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>Tổng hợp<br>nội dung</td>
<td>K~~ế~~t hợp, phân tích, tóm t~~ắ~~t các dữ liệu hoặc thông tin<br>riêng lẻ để tạo ra một nội dung hoàn chỉnh, có cấu trúc và<br>ý nghĩa rõ ràng.</td>
<td>Tóm tắt báo cáo tài chính; chuyển đổi ghi chú y tế phi cấu trúc<br>của bác sĩ thành hồ sơ bệnh án đầy đủ.</td>
</tr>
<tr>
<td>3</td>
<td>Ra quyết<br>định</td>
<td>Hỗ trợ hoặc đề xuất quyết định tối ưu từ nhiều lựa chọn,<br>dựa trên phân tích dữ liệu, dự đoán hoặc đánh giá rủi ro.</td>
<td><br> <br>Hỗ trợ quyết định mua bán cổ phiếu; hệ thống đề xuất phê<br>duyệt khoản vay tự động dựa trên lịch sử tín dụng.</td>
</tr>
<tr>
<td>4</td>
<td>Phát hiện</td>
<td>Nhận diện và xác định sự hiện diện của các vấn đề, sự<br>kiện hoặc nguy cơ tiềm ẩn thông qua phân tích dữ liệu.</td>
<td>Phát hiện gian lận giao dịch ngân hàng; phát hiện tấn công<br>mạng; nhận dạng sự cố kỹ thuật trong dây chuyền sản xuất.</td>
</tr>
<tr>
<td>5</td>
<td>Trợ lý ảo</td>
<td>Hỗ trợ người dùng bằng cách hiểu, phản hồi và thực hiện<br>các yêu cầu hoặc tác vụ qua giao tiếp tự nhiên như một<br>trợ lý cá nhân.</td>
<td>Siri, Alexa hỗ trợ đặt lịch họp; trợ lý ảo giúp trả lời câu hỏi<br>khách hàng trực tuyến tự động.</td>
</tr>
<tr>
<td>6</td>
<td>Khám phá</td>
<td>Khai phá, nhận dạng hoặc tìm ra thông tin, sản phẩm hoặc<br>quy trình hoàn toàn mới mà con người chưa biết tới hoặc<br>chưa tiếp cận được trước đó.</td>
<td>Phát hiện phân tử mới trong dược phẩm; khám phá vật liệu pin<br>tiên tiến; tối ưu công thức sản phẩm mới trong sản xuất.</td>
</tr>
<tr>
<td>7</td>
<td>Phân tích<br>hình ảnh</td>
<td>Nhận diện và phân tích nội dung từ hình ảnh số để đưa ra<br>thông tin hữu ích, hỗ trợ việc ra quyết định.</td>
<td><br>Hệ thống nhận dạng ung thư sớm từ hình ảnh chẩn đoán y tế;<br>phân tích sản phẩm lỗi từ hình ảnh trên dây chuyền sản xuất.</td>
</tr>
<tr>
<td>8</td>
<td>Truy xuất<br>thông tin</td>
<td>Hỗ trợ người dùng tìm kiếm, tiếp cận nhanh chóng và<br>chính xác các thông tin cần thiết từ nguồn dữ liệu lớn, đa<br>dạng.</td>
<td>Truy xuất tài liệu pháp lý theo từ khóa; tìm kiếm protein ổn<br>định cho nghiên cứu thuốc nhanh hơn.</td>
</tr>
<tr>
<td>9</td>
<td>Giám sát</td>
<td>Theo dõi, giám sát liên tục trạng thái, chất lượng hoặc<br>hiệu suất của hệ thống để phát hiện bất thường hoặc cải<br>tiến hoạt động.</td>
<td>Giám sát tình trạng thiết bị công nghiệp theo thời gian thực;<br>giám sát môi trường để phát hiện cháy rừng tự động.</td>
</tr>
<tr>
<td>10</td>
<td>Cải thiện<br>hiệu suất</td>
<td>Tối ưu hóa, nâng cao chất lượng, độ chính xác hoặc hiệu<br>suất vận hành của quy trình hoặc hệ thống hiện có.</td>
<td><br>Tối ưu thuật toán phân tích dữ liệu lớn; cải tiến độ chính xác<br>mô hình dự báo thời tiết.</td>
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
<th>11</th>
<th>Cánhânhóa</th>
<th>Điề uchỉnhvàcungcấ psảnphẩ m dịchvụ nộidungphù<br>,,<br>hợp nhấ t với từng cá nhân dựa trên hành vi sở thích và<br>,<br>đặcđiể mriêng củahọ<br>.</th>
<th>Cá nhân hóa nội dung quảng cáo theo hành vi mua sắ m trực<br>tuyế n;cungcấ pnội dung giáodụcphùhợptheonănglựchọc<br>viên<br>.</th>
</tr>
</thead>
<tbody>
<tr>
<td>12</td>
<td>Dự báo</td>
<td>Dự đoán khả năng xảy ra của các sự kiện hoặc kết quả<br>trong tương lai, dựa trên phân tích dữ liệu lịch sử và<br>mô hình thống kê.</td>
<td>Dự báo doanh thu quý kế tiếp; dự báo khả năng hỏng hóc máy<br>móc trong sản xuất; dự báo lưu lượng khách hàng để tối ưu<br>dịch vụ.</td>
</tr>
<tr>
<td>13</td>
<td>Tự động hóa<br>quy trình</td>
<td>Thực hiện các tác vụ thường xuyên, lặp lại hoặc dễ xảy<br>ra sai sót nhằm giảm thời gian, tiết kiệm nguồn lực và<br>nâng cao hiệu quả hoạt động.</td>
<td>Tự động hóa quản lý hóa đơn và thanh toán; xử lý, phân loại<br>email nội bộ tự động.</td>
</tr>
<tr>
<td>14</td>
<td>Khuyến nghị</td>
<td>Đưa ra các gợi ý, lựa chọn hợp lý nhất cho người dùng<br>nhằm hỗ trợ họ ra quyết định một cách hiệu quả.</td>
<td>Đề xuất sản phẩm phù hợp cho khách hàng mua sắm trực tuyến;<br>gợi ý phản hồi nhanh trong hệ thống chăm sóc khách hàng.</td>
</tr>
</tbody>
</table>
13    |<image_6>|                       |---|---|---|---| |2|Tổng hợp<br>nội dung|K~~ế~~t hợp, phân tích, tóm t~~ắ~~t các dữ liệu hoặc thông tin<br>riêng lẻ để tạo ra một nội dung hoàn chỉnh, có cấu trúc và<br>ý nghĩa rõ ràng.|Tóm tắt báo cáo tài chính; chuyển đổi ghi chú y tế phi cấu trúc<br>của bác sĩ thành hồ sơ bệnh án đầy đủ.| |3|Ra quyết<br>định|Hỗ trợ hoặc đề xuất quyết định tối ưu từ nhiều lựa chọn,<br>dựa trên phân tích dữ liệu, dự đoán hoặc đánh giá rủi ro.|<br> <br>Hỗ trợ quyết định mua bán cổ phiếu; hệ thống đề xuất phê<br>duyệt khoản vay tự động dựa trên lịch sử tín dụng.| |4|Phát hiện|Nhận diện và xác định sự hiện diện của các vấn đề, sự<br>kiện hoặc nguy cơ tiềm ẩn thông qua phân tích dữ liệu.|Phát hiện gian lận giao dịch ngân hàng; phát hiện tấn công<br>mạng; nhận dạng sự cố kỹ thuật trong dây chuyền sản xuất.| |5|Trợ lý ảo|Hỗ trợ người dùng bằng cách hiểu, phản hồi và thực hiện<br>các yêu cầu hoặc tác vụ qua giao tiếp tự nhiên như một<br>trợ lý cá nhân.|Siri, Alexa hỗ trợ đặt lịch họp; trợ lý ảo giúp trả lời câu hỏi<br>khách hàng trực tuyến tự động.| |6|Khám phá|Khai phá, nhận dạng hoặc tìm ra thông tin, sản phẩm hoặc<br>quy trình hoàn toàn mới mà con người chưa biết tới hoặc<br>chưa tiếp cận được trước đó.|Phát hiện phân tử mới trong dược phẩm; khám phá vật liệu pin<br>tiên tiến; tối ưu công thức sản phẩm mới trong sản xuất.| |7|Phân tích<br>hình ảnh|Nhận diện và phân tích nội dung từ hình ảnh số để đưa ra<br>thông tin hữu ích, hỗ trợ việc ra quyết định.|<br>Hệ thống nhận dạng ung thư sớm từ hình ảnh chẩn đoán y tế;<br>phân tích sản phẩm lỗi từ hình ảnh trên dây chuyền sản xuất.| |8|Truy xuất<br>thông tin|Hỗ trợ người dùng tìm kiếm, tiếp cận nhanh chóng và<br>chính xác các thông tin cần thiết từ nguồn dữ liệu lớn, đa<br>dạng.|Truy xuất tài liệu pháp lý theo từ khóa; tìm kiếm protein ổn<br>định cho nghiên cứu thuốc nhanh hơn.| |9|Giám sát|Theo dõi, giám sát liên tục trạng thái, chất lượng hoặc<br>hiệu suất của hệ thống để phát hiện bất thường hoặc cải<br>tiến hoạt động.|Giám sát tình trạng thiết bị công nghiệp theo thời gian thực;<br>giám sát môi trường để phát hiện cháy rừng tự động.| |10|Cải thiện<br>hiệu suất|Tối ưu hóa, nâng cao chất lượng, độ chính xác hoặc hiệu<br>suất vận hành của quy trình hoặc hệ thống hiện có.|<br>Tối ưu thuật toán phân tích dữ liệu lớn; cải tiến độ chính xác<br>mô hình dự báo thời tiết.|    14                          |---|---|---|---| |12|Dự báo|Dự đoán khả năng xảy ra của các sự kiện hoặc kết quả<br>trong tương lai, dựa trên phân tích dữ liệu lịch sử và<br>mô hình thống kê.|Dự báo doanh thu quý kế tiếp; dự báo khả năng hỏng hóc máy<br>móc trong sản xuất; dự báo lưu lượng khách hàng để tối ưu<br>dịch vụ.| |13|Tự động hóa<br>quy trình|Thực hiện các tác vụ thường xuyên, lặp lại hoặc dễ xảy<br>ra sai sót nhằm giảm thời gian, tiết kiệm nguồn lực và<br>nâng cao hiệu quả hoạt động.|Tự động hóa quản lý hóa đơn và thanh toán; xử lý, phân loại<br>email nội bộ tự động.| |14|Khuyến nghị|Đưa ra các gợi ý, lựa chọn hợp lý nhất cho người dùng<br>nhằm hỗ trợ họ ra quyết định một cách hiệu quả.|Đề xuất sản phẩm phù hợp cho khách hàng mua sắm trực tuyến;<br>gợi ý phản hồi nhanh trong hệ thống chăm sóc khách hàng.|

### Đánh giá mức độ phù hợp của các kỹ thuật AI theo từng bài toán phổ biến

Để đánh giá mức độ phù hợp của các kỹ thuật AI theo từng bài toán, thực hiện như sau:
   * Thực hiện đánh giá các đặc điểm và yêu cầu của bài toán dựa trên bộ tiêu chí đã được xây dựng.
    * Tham chiếu bảng đánh giá đã xây dựng, với mỗi tiêu chí xác định mức độ phù hợp của từng kỹ thuật AI:
    * Không phù hợp (K): Kết luận kỹ thuật không phù hợp.
   * Cân nhắc (C): Không cộng điểm.
   * Phù hợp (P): Cộng 1 điểm.
    * Độ phù hợp tổng thể của một kỹ thuật AI được xác định bằng tổng điểm các tiêu chí (chỉ tính nếu không có tiêu chí nào bị đánh giá là không phù hợp).
     * Kỹ thuật có tổng điểm cao nhất được ưu tiên lựa chọn (phù hợp), các kỹ thuật có tổng điểm thấp hơn cần được cân nhắc và đánh giá kỹ lưỡng, có thể được áp dụng trong các trường hợp đặc biệt hoặc kết hợp với các kỹ thuật khác để khắc phục các điểm yếu cho kỹ thuật chính. Trong trường hợp có nhiều kỹ thuật có tổng điểm bằng nhau, cần ưu tiên theo thứ tự quan trọng của tiêu chí từ mục tiêu bài toán, loại dữ liệu, nhãn dữ liệu, số chiều dữ liệu, số lượng dữ liệu, cho đến yêu cầu khả năng giải thích hoặc   15    |<image_7>|

# cân nhắc kết hợp các kỹ thuật để tận dụng điểm mạnh của từng kỹ thuật. - Căn cứ dựa trên đặc điểm6 của 14 bài toán AI phổ biến đã được phân loại, chiếu theo bộ tiêu chí đánh giá đã xây dựng để xác định mức độ phù hợp của các kỹ thuật AI cho từng bài toán. Cụ thể như sau: - _Bảng 4. Bảng đánh giá mức độ phù hợp của các kỹ thuật AI theo từng bài toán phổ biến._

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
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
<th>Bài toán</th>
<th>Chiề<br>u<br>đánhgiá</th>
<th>Col4</th>
<th>Mụctiêu<br>bài toán</th>
<th>Loạidữ<br>liệu</th>
<th>Nhãndữ<br>liệu</th>
<th>Số chiề udữ<br>liệu</th>
<th>Sốlượng<br>dữliệu</th>
<th>Yêu cầ u khả<br>nănggiảithích</th>
<th>Tổ<br>ng<br>điể<br>m</th>
<th>Kế<br>t<br>luận</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>**Tạo nội**<br>**dung**</td>
<td>Đặc đi~~ể~~m</td>
<td>Đặc đi~~ể~~m</td>
<td>Tạo sinh</td>
<td>Phi c~~ấ~~u trúc</td>
<td>Không nhãn</td>
<td>Lớn</td>
<td>Lớn</td>
<td>Không b~~ắ~~t buộc</td>
</tr>
<tr>
<td>1</td>
<td>**Tạo nội**<br>**dung**</td>
<td>Kỹ<br>thuật<br></td>
<td>ML</td>
<td>**K**</td>
<td>**K**</td>
<td>**C **</td>
<td>**K**</td>
<td>**C **</td>
<td>**P**</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>1</td>
<td>**Tạo nội**<br>**dung**</td>
<td>Kỹ<br>thuật<br></td>
<td>DL</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**4 **</td>
<td>**C **</td>
</tr>
<tr>
<td>1</td>
<td>**Tạo nội**<br>**dung**</td>
<td>Kỹ<br>thuật<br></td>
<td>GenAI<br></td>
<td>**P**</td>
<td>**P**<br></td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**<br></td>
<td>**6 **</td>
<td>**P**</td>
</tr>
<tr>
<td>2</td>
<td>**Tổng**<br>**hợp nội**<br>**dung**</td>
<td>Đặc đi~~ể~~m</td>
<td>Đặc đi~~ể~~m</td>
<td>Tạo sinh</td>
<td>Phi c~~ấ~~u trúc</td>
<td>Không nhãn</td>
<td>Lớn</td>
<td>Lớn</td>
<td>Không b~~ắ~~t buộc</td>
</tr>
<tr>
<td>2</td>
<td>**Tổng**<br>**hợp nội**<br>**dung**</td>
<td>Kỹ<br>thuật</td>
<td>ML</td>
<td>**K**</td>
<td>**K**</td>
<td>**C **</td>
<td>**K**</td>
<td>**C **</td>
<td>**P**</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>2</td>
<td>**Tổng**<br>**hợp nội**<br>**dung**</td>
<td>Kỹ<br>thuật</td>
<td>DL</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**4 **</td>
<td>**C **</td>
</tr>
<tr>
<td>2</td>
<td>**Tổng**<br>**hợp nội**<br>**dung**</td>
<td>Kỹ<br>thuật</td>
<td>GenAI</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**6 **</td>
<td>**P**</td>
</tr>
<tr>
<td>3</td>
<td>**Ra**<br>**quyết**<br>**định**</td>
<td>Đặc điểm</td>
<td>Đặc điểm</td>
<td>Dự đoán</td>
<td>Có cấu trúc</td>
<td>Có nhãn</td>
<td>Nhỏ</td>
<td>Lớn</td>
<td>Có</td>
</tr>
<tr>
<td>3</td>
<td>**Ra**<br>**quyết**<br>**định**</td>
<td>Kỹ<br>thuật<br></td>
<td>ML</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**5 **</td>
<td>**P**</td>
</tr>
<tr>
<td>3</td>
<td>**Ra**<br>**quyết**<br>**định**</td>
<td>Kỹ<br>thuật<br></td>
<td>DL</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**4 **</td>
<td>**C **</td>
</tr>
<tr>
<td>3</td>
<td>**Ra**<br>**quyết**<br>**định**</td>
<td>Kỹ<br>thuật<br></td>
<td>GenAI<br></td>
<td>**C **</td>
<td>**K**<br></td>
<td>**C **</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>4</td>
<td>**Phát**<br>**hiện**</td>
<td>Đặc đi~~ể~~m</td>
<td>Đặc đi~~ể~~m</td>
<td>Dự đoán</td>
<td>Phi c~~ấ~~u trúc</td>
<td>Có nhãn</td>
<td>Nhỏ</td>
<td>Lớn</td>
<td>Có</td>
</tr>
<tr>
<td>4</td>
<td>**Phát**<br>**hiện**</td>
<td>Kỹ<br>thuật<br></td>
<td>ML</td>
<td>**P**</td>
<td>**K**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>4</td>
<td>**Phát**<br>**hiện**</td>
<td>Kỹ<br>thuật<br></td>
<td>DL</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**5 **</td>
<td>**P**</td>
</tr>
<tr>
<td>4</td>
<td>**Phát**<br>**hiện**</td>
<td>Kỹ<br>thuật<br></td>
<td>GenAI<br></td>
<td>**C **</td>
<td>**P**<br></td>
<td>**C **</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**2 **</td>
<td>**C **</td>
</tr>
<tr>
<td>5</td>
<td>**Trợ lý**<br>**ảo**</td>
<td>Đặc đi~~ể~~m</td>
<td>Đặc đi~~ể~~m</td>
<td>Tạo sinh</td>
<td>Phi c~~ấ~~u trúc</td>
<td>Không nhãn</td>
<td>Lớn</td>
<td>Lớn</td>
<td>Có</td>
</tr>
<tr>
<td>5</td>
<td>**Trợ lý**<br>**ảo**</td>
<td>Kỹ<br>thuật</td>
<td>ML</td>
<td>**K**</td>
<td>**K**</td>
<td>**C **</td>
<td>**K**</td>
<td>**C **</td>
<td>**P**</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>5</td>
<td>**Trợ lý**<br>**ảo**</td>
<td>Kỹ<br>thuật</td>
<td>DL</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**3 **</td>
<td>**C **</td>
</tr>
<tr>
<td>5</td>
<td>**Trợ lý**<br>**ảo**</td>
<td>Kỹ<br>thuật</td>
<td>GenAI</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**5 **</td>
<td>**P**</td>
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
<th>Bài toán</th>
<th>Chiề<br>u<br>đánhgiá</th>
<th>Col4</th>
<th>Mụctiêu<br>bài toán</th>
<th>Loạidữ<br>liệu</th>
<th>Nhãndữ<br>liệu</th>
<th>Số chiề udữ<br>liệu</th>
<th>Sốlượng<br>dữliệu</th>
<th>Yêu cầ u khả<br>nănggiảithích</th>
<th>Tổ<br>ng<br>điể<br>m</th>
<th>Kế<br>t<br>luận</th>
</tr>
</thead>
<tbody>
<tr>
<td>6</td>
<td>**Khám**<br>**phá**</td>
<td>Đặc điểm</td>
<td>Đặc điểm</td>
<td>Tạo sinh</td>
<td>Phi cấu trúc</td>
<td>Không nhãn</td>
<td>Lớn</td>
<td>Lớn</td>
<td>Có</td>
</tr>
<tr>
<td>6</td>
<td>**Khám**<br>**phá**</td>
<td>Kỹ<br>thuật</td>
<td>ML</td>
<td>**K**</td>
<td>**K**</td>
<td>**C **</td>
<td>**K**</td>
<td>**C **</td>
<td>**P**</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>6</td>
<td>**Khám**<br>**phá**</td>
<td>Kỹ<br>thuật</td>
<td>DL</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**3 **</td>
<td>**C **</td>
</tr>
<tr>
<td>6</td>
<td>**Khám**<br>**phá**</td>
<td>Kỹ<br>thuật</td>
<td>GenAI</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**5 **</td>
<td>**P**</td>
</tr>
<tr>
<td>7</td>
<td>**Phân**<br>**tích**<br>**hình**<br>**ảnh**</td>
<td>Đặc điểm</td>
<td>Đặc điểm</td>
<td>Dự đoán</td>
<td>Phi cấu trúc</td>
<td>Có nhãn</td>
<td>Lớn</td>
<td>Lớn</td>
<td>Không bắt buộc</td>
</tr>
<tr>
<td>7</td>
<td>**Phân**<br>**tích**<br>**hình**<br>**ảnh**</td>
<td>Kỹ<br>thuật</td>
<td>ML</td>
<td>**P**</td>
<td>**K**</td>
<td>**P**</td>
<td>**K**</td>
<td>**C **</td>
<td>**P**</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>7</td>
<td>**Phân**<br>**tích**<br>**hình**<br>**ảnh**</td>
<td>Kỹ<br>thuật</td>
<td>DL</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**6 **</td>
<td>**P**</td>
</tr>
<tr>
<td>7</td>
<td>**Phân**<br>**tích**<br>**hình**<br>**ảnh**</td>
<td>Kỹ<br>thuật</td>
<td>GenAI</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**4 **</td>
<td>**C **</td>
</tr>
<tr>
<td>8</td>
<td>**Truy**<br>**xuất**<br>**thông**<br>**tin**</td>
<td>Đặc điểm</td>
<td>Đặc điểm</td>
<td>Dự đoán</td>
<td>Phi cấu trúc</td>
<td>Có nhãn</td>
<td>Lớn</td>
<td>Lớn</td>
<td>Có</td>
</tr>
<tr>
<td>8</td>
<td>**Truy**<br>**xuất**<br>**thông**<br>**tin**</td>
<td>Kỹ<br>thuật</td>
<td>ML</td>
<td>**P**</td>
<td>**K**</td>
<td>**P**</td>
<td>**K**</td>
<td>**C **</td>
<td>**P**</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>8</td>
<td>**Truy**<br>**xuất**<br>**thông**<br>**tin**</td>
<td>Kỹ<br>thuật</td>
<td>DL</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**5 **</td>
<td>**P**</td>
</tr>
<tr>
<td>8</td>
<td>**Truy**<br>**xuất**<br>**thông**<br>**tin**</td>
<td>Kỹ<br>thuật</td>
<td>GenAI</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**3 **</td>
<td>**C **</td>
</tr>
<tr>
<td>9</td>
<td>**Giám**<br>**sát**</td>
<td>Đặc điểm</td>
<td>Đặc điểm</td>
<td>Dự đoán</td>
<td>Có cấu trúc</td>
<td>Không nhãn</td>
<td>Nhỏ</td>
<td>Lớn</td>
<td>Có</td>
</tr>
<tr>
<td>9</td>
<td>**Giám**<br>**sát**</td>
<td>Kỹ<br>thuật</td>
<td>ML</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**4 **</td>
<td>**P**</td>
</tr>
<tr>
<td>9</td>
<td>**Giám**<br>**sát**</td>
<td>Kỹ<br>thuật</td>
<td>DL</td>
<td>**P**</td>
<td>**C **</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**3 **</td>
<td>**C **</td>
</tr>
<tr>
<td>9</td>
<td>**Giám**<br>**sát**</td>
<td>Kỹ<br>thuật</td>
<td>GenAI</td>
<td>**C **</td>
<td>**K**</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>10</td>
<td>**Cải**<br>**thiện**<br>**hiệu**<br>**suất**</td>
<td>Đặc điểm</td>
<td>Đặc điểm</td>
<td>Dự đoán</td>
<td>Có cấu trúc</td>
<td>Có nhãn</td>
<td>Nhỏ</td>
<td>Nhỏ</td>
<td>Có</td>
</tr>
<tr>
<td>10</td>
<td>**Cải**<br>**thiện**<br>**hiệu**<br>**suất**</td>
<td>Kỹ<br>thuật</td>
<td>ML</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**5 **</td>
<td>**P**</td>
</tr>
<tr>
<td>10</td>
<td>**Cải**<br>**thiện**<br>**hiệu**<br>**suất**</td>
<td>Kỹ<br>thuật</td>
<td>DL</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**4 **</td>
<td>**C **</td>
</tr>
<tr>
<td>10</td>
<td>**Cải**<br>**thiện**<br>**hiệu**<br>**suất**</td>
<td>Kỹ<br>thuật</td>
<td>GenAI</td>
<td>**C **</td>
<td>**K**</td>
<td>**C **</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>11</td>
<td>**Cá nhân**<br>**hóa**</td>
<td>Đặc điểm</td>
<td>Đặc điểm</td>
<td>Dự đoán</td>
<td>Có cấu trúc</td>
<td>Có nhãn</td>
<td>Nhỏ</td>
<td>Lớn</td>
<td>Có</td>
</tr>
<tr>
<td>11</td>
<td>**Cá nhân**<br>**hóa**</td>
<td>Kỹ<br>thuật</td>
<td>ML</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**5 **</td>
<td>**P**</td>
</tr>
<tr>
<td>11</td>
<td>**Cá nhân**<br>**hóa**</td>
<td>Kỹ<br>thuật</td>
<td>DL</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**4 **</td>
<td>**C **</td>
</tr>
<tr>
<td>11</td>
<td>**Cá nhân**<br>**hóa**</td>
<td>Kỹ<br>thuật</td>
<td>GenAI</td>
<td>**C **</td>
<td>**K**</td>
<td>**C **</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**0 **</td>
<td>**K**</td>
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
<th>Bài toán</th>
<th>Chiề<br>u<br>đánhgiá</th>
<th>Col4</th>
<th>Mụctiêu<br>bài toán</th>
<th>Loạidữ<br>liệu</th>
<th>Nhãndữ<br>liệu</th>
<th>Số chiề udữ<br>liệu</th>
<th>Sốlượng<br>dữliệu</th>
<th>Yêu cầ u khả<br>nănggiảithích</th>
<th>Tổ<br>ng<br>điể<br>m</th>
<th>Kế<br>t<br>luận</th>
</tr>
</thead>
<tbody>
<tr>
<td>12</td>
<td>**Dự báo**</td>
<td>Đặc điểm</td>
<td>Đặc điểm</td>
<td>Dự đoán</td>
<td>Có c~~ấ~~u trúc</td>
<td>Có nhãn</td>
<td>Nhỏ</td>
<td>Lớn</td>
<td>Có</td>
</tr>
<tr>
<td>12</td>
<td>**Dự báo**</td>
<td>Kỹ<br>thuật</td>
<td>ML</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**5 **</td>
<td>**P**</td>
</tr>
<tr>
<td>12</td>
<td>**Dự báo**</td>
<td>Kỹ<br>thuật</td>
<td>DL</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**4 **</td>
<td>**C **</td>
</tr>
<tr>
<td>12</td>
<td>**Dự báo**</td>
<td>Kỹ<br>thuật</td>
<td>GenAI</td>
<td>**C **</td>
<td>**K**<br></td>
<td>**C **</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **<br></td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>13</td>
<td>**Tự động**<br>**hóa quy**<br>**trình**</td>
<td>Đặc điểm</td>
<td>Đặc điểm</td>
<td>Dự đoán</td>
<td>Có c~~ấ~~u trúc</td>
<td>Không nhãn</td>
<td>Nhỏ</td>
<td>Nhỏ</td>
<td>Không b~~ắ~~t buộc</td>
</tr>
<tr>
<td>13</td>
<td>**Tự động**<br>**hóa quy**<br>**trình**</td>
<td>Kỹ<br>thuật</td>
<td>ML</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**5 **</td>
<td>**P**</td>
</tr>
<tr>
<td>13</td>
<td>**Tự động**<br>**hóa quy**<br>**trình**</td>
<td>Kỹ<br>thuật</td>
<td>DL</td>
<td>**P**</td>
<td>**C **</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**3 **</td>
<td>**C **</td>
</tr>
<tr>
<td>13</td>
<td>**Tự động**<br>**hóa quy**<br>**trình**</td>
<td>Kỹ<br>thuật</td>
<td>GenAI</td>
<td>**C **</td>
<td>**K**<br></td>
<td>**P**</td>
<td>**C **</td>
<td>**C **</td>
<td>**P**</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
<tr>
<td>14</td>
<td>**Khuyến**<br>**nghị**</td>
<td>Đặc điểm</td>
<td>Đặc điểm</td>
<td>Dự đoán</td>
<td>Có c~~ấ~~u trúc</td>
<td>Có nhãn</td>
<td>Nhỏ</td>
<td>Lớn</td>
<td>Có</td>
</tr>
<tr>
<td>14</td>
<td>**Khuyến**<br>**nghị**</td>
<td>Kỹ<br>thuật</td>
<td>ML</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**5 **</td>
<td>**P**</td>
</tr>
<tr>
<td>14</td>
<td>**Khuyến**<br>**nghị**</td>
<td>Kỹ<br>thuật</td>
<td>DL</td>
<td>**P**</td>
<td>**C **</td>
<td>**P**</td>
<td>**P**</td>
<td>**P**</td>
<td>**C **</td>
<td>**4 **</td>
<td>**C **</td>
</tr>
<tr>
<td>14</td>
<td>**Khuyến**<br>**nghị**</td>
<td>Kỹ<br>thuật</td>
<td>GenAI</td>
<td>**C **</td>
<td>**K**</td>
<td>**C **</td>
<td>**C **</td>
<td>**P**</td>
<td>**C **</td>
<td>**0 **</td>
<td>**K**</td>
</tr>
</tbody>
</table>
|---|---|---|---|---|---|---|---|---|---|---|---| |1|**Tạo nội**<br>**dung**|Đặc đi~~ể~~m|Đặc đi~~ể~~m|Tạo sinh|Phi c~~ấ~~u trúc|Không nhãn|Lớn|Lớn|Không b~~ắ~~t buộc||| |1|**Tạo nội**<br>**dung**|Kỹ<br>thuật<br>|ML|**K**|**K**|**C **|**K**|**C **|**P**|**0 **|**K**| |1|**Tạo nội**<br>**dung**|Kỹ<br>thuật<br>|DL|**C **|**P**|**C **|**P**|**P**|**P**|**4 **|**C **| |1|**Tạo nội**<br>**dung**|Kỹ<br>thuật<br>|GenAI<br>|**P**|**P**<br>|**P**|**P**|**P**|**P**<br>|**6 **|**P**| |2|**Tổng**<br>**hợp nội**<br>**dung**|Đặc đi~~ể~~m|Đặc đi~~ể~~m|Tạo sinh|Phi c~~ấ~~u trúc|Không nhãn|Lớn|Lớn|Không b~~ắ~~t buộc||| |2|**Tổng**<br>**hợp nội**<br>**dung**|Kỹ<br>thuật|ML|**K**|**K**|**C **|**K**|**C **|**P**|**0 **|**K**| |2|**Tổng**<br>**hợp nội**<br>**dung**|Kỹ<br>thuật|DL|**C **|**P**|**C **|**P**|**P**|**P**|**4 **|**C **| |2|**Tổng**<br>**hợp nội**<br>**dung**|Kỹ<br>thuật|GenAI|**P**|**P**|**P**|**P**|**P**|**P**|**6 **|**P**| |3|**Ra**<br>**quyết**<br>**định**|Đặc điểm|Đặc điểm|Dự đoán|Có cấu trúc|Có nhãn|Nhỏ|Lớn|Có||| |3|**Ra**<br>**quyết**<br>**định**|Kỹ<br>thuật<br>|ML|**P**|**P**|**P**|**P**|**C **|**P**|**5 **|**P**| |3|**Ra**<br>**quyết**<br>**định**|Kỹ<br>thuật<br>|DL|**P**|**C **|**P**|**P**|**P**|**C **|**4 **|**C **| |3|**Ra**<br>**quyết**<br>**định**|Kỹ<br>thuật<br>|GenAI<br>|**C **|**K**<br>|**C **|**C **|**P**|**C **|**0 **|**K**| |4|**Phát**<br>**hiện**|Đặc đi~~ể~~m|Đặc đi~~ể~~m|Dự đoán|Phi c~~ấ~~u trúc|Có nhãn|Nhỏ|Lớn|Có||| |4|**Phát**<br>**hiện**|Kỹ<br>thuật<br>|ML|**P**|**K**|**P**|**P**|**C **|**P**|**0 **|**K**| |4|**Phát**<br>**hiện**|Kỹ<br>thuật<br>|DL|**P**|**P**|**P**|**P**|**P**|**C **|**5 **|**P**| |4|**Phát**<br>**hiện**|Kỹ<br>thuật<br>|GenAI<br>|**C **|**P**<br>|**C **|**C **|**P**|**C **|**2 **|**C **| |5|**Trợ lý**<br>**ảo**|Đặc đi~~ể~~m|Đặc đi~~ể~~m|Tạo sinh|Phi c~~ấ~~u trúc|Không nhãn|Lớn|Lớn|Có||| |5|**Trợ lý**<br>**ảo**|Kỹ<br>thuật|ML|**K**|**K**|**C **|**K**|**C **|**P**|**0 **|**K**| |5|**Trợ lý**<br>**ảo**|Kỹ<br>thuật|DL|**C **|**P**|**C **|**P**|**P**|**C **|**3 **|**C **| |5|**Trợ lý**<br>**ảo**|Kỹ<br>thuật|GenAI|**P**|**P**|**P**|**P**|**P**|**C **|**5 **|**P**|    16                                                                |---|---|---|---|---|---|---|---|---|---|---|---| |6|**Khám**<br>**phá**|Đặc điểm|Đặc điểm|Tạo sinh|Phi cấu trúc|Không nhãn|Lớn|Lớn|Có||| |6|**Khám**<br>**phá**|Kỹ<br>thuật|ML|**K**|**K**|**C **|**K**|**C **|**P**|**0 **|**K**| |6|**Khám**<br>**phá**|Kỹ<br>thuật|DL|**C **|**P**|**C **|**P**|**P**|**C **|**3 **|**C **| |6|**Khám**<br>**phá**|Kỹ<br>thuật|GenAI|**P**|**P**|**P**|**P**|**P**|**C **|**5 **|**P**| |7|**Phân**<br>**tích**<br>**hình**<br>**ảnh**|Đặc điểm|Đặc điểm|Dự đoán|Phi cấu trúc|Có nhãn|Lớn|Lớn|Không bắt buộc||| |7|**Phân**<br>**tích**<br>**hình**<br>**ảnh**|Kỹ<br>thuật|ML|**P**|**K**|**P**|**K**|**C **|**P**|**0 **|**K**| |7|**Phân**<br>**tích**<br>**hình**<br>**ảnh**|Kỹ<br>thuật|DL|**P**|**P**|**P**|**P**|**P**|**P**|**6 **|**P**| |7|**Phân**<br>**tích**<br>**hình**<br>**ảnh**|Kỹ<br>thuật|GenAI|**C **|**P**|**C **|**P**|**P**|**P**|**4 **|**C **| |8|**Truy**<br>**xuất**<br>**thông**<br>**tin**|Đặc điểm|Đặc điểm|Dự đoán|Phi cấu trúc|Có nhãn|Lớn|Lớn|Có||| |8|**Truy**<br>**xuất**<br>**thông**<br>**tin**|Kỹ<br>thuật|ML|**P**|**K**|**P**|**K**|**C **|**P**|**0 **|**K**| |8|**Truy**<br>**xuất**<br>**thông**<br>**tin**|Kỹ<br>thuật|DL|**P**|**P**|**P**|**P**|**P**|**C **|**5 **|**P**| |8|**Truy**<br>**xuất**<br>**thông**<br>**tin**|Kỹ<br>thuật|GenAI|**C **|**P**|**C **|**P**|**P**|**C **|**3 **|**C **| |9|**Giám**<br>**sát**|Đặc điểm|Đặc điểm|Dự đoán|Có cấu trúc|Không nhãn|Nhỏ|Lớn|Có||| |9|**Giám**<br>**sát**|Kỹ<br>thuật|ML|**P**|**P**|**C **|**P**|**C **|**P**|**4 **|**P**| |9|**Giám**<br>**sát**|Kỹ<br>thuật|DL|**P**|**C **|**C **|**P**|**P**|**C **|**3 **|**C **| |9|**Giám**<br>**sát**|Kỹ<br>thuật|GenAI|**C **|**K**|**P**|**C **|**P**|**C **|**0 **|**K**| |10|**Cải**<br>**thiện**<br>**hiệu**<br>**suất**|Đặc điểm|Đặc điểm|Dự đoán|Có cấu trúc|Có nhãn|Nhỏ|Nhỏ|Có||| |10|**Cải**<br>**thiện**<br>**hiệu**<br>**suất**|Kỹ<br>thuật|ML|**P**|**P**|**P**|**P**|**C **|**P**|**5 **|**P**| |10|**Cải**<br>**thiện**<br>**hiệu**<br>**suất**|Kỹ<br>thuật|DL|**P**|**C **|**P**|**P**|**P**|**C **|**4 **|**C **| |10|**Cải**<br>**thiện**<br>**hiệu**<br>**suất**|Kỹ<br>thuật|GenAI|**C **|**K**|**C **|**C **|**P**|**C **|**0 **|**K**| |11|**Cá nhân**<br>**hóa**|Đặc điểm|Đặc điểm|Dự đoán|Có cấu trúc|Có nhãn|Nhỏ|Lớn|Có||| |11|**Cá nhân**<br>**hóa**|Kỹ<br>thuật|ML|**P**|**P**|**P**|**P**|**C **|**P**|**5 **|**P**| |11|**Cá nhân**<br>**hóa**|Kỹ<br>thuật|DL|**P**|**C **|**P**|**P**|**P**|**C **|**4 **|**C **| |11|**Cá nhân**<br>**hóa**|Kỹ<br>thuật|GenAI|**C **|**K**|**C **|**C **|**P**|**C **|**0 **|**K**|    17                                                |---|---|---|---|---|---|---|---|---|---|---|---| |12|**Dự báo**|Đặc điểm|Đặc điểm|Dự đoán|Có c~~ấ~~u trúc|Có nhãn|Nhỏ|Lớn|Có||| |12|**Dự báo**|Kỹ<br>thuật|ML|**P**|**P**|**P**|**P**|**C **|**P**|**5 **|**P**| |12|**Dự báo**|Kỹ<br>thuật|DL|**P**|**C **|**P**|**P**|**P**|**C **|**4 **|**C **| |12|**Dự báo**|Kỹ<br>thuật|GenAI|**C **|**K**<br>|**C **|**C **|**P**|**C **<br>|**0 **|**K**| |13|**Tự động**<br>**hóa quy**<br>**trình**|Đặc điểm|Đặc điểm|Dự đoán|Có c~~ấ~~u trúc|Không nhãn|Nhỏ|Nhỏ|Không b~~ắ~~t buộc||| |13|**Tự động**<br>**hóa quy**<br>**trình**|Kỹ<br>thuật|ML|**P**|**P**|**C **|**P**|**P**|**P**|**5 **|**P**| |13|**Tự động**<br>**hóa quy**<br>**trình**|Kỹ<br>thuật|DL|**P**|**C **|**C **|**P**|**C **|**P**|**3 **|**C **| |13|**Tự động**<br>**hóa quy**<br>**trình**|Kỹ<br>thuật|GenAI|**C **|**K**<br>|**P**|**C **|**C **|**P**|**0 **|**K**| |14|**Khuyến**<br>**nghị**|Đặc điểm|Đặc điểm|Dự đoán|Có c~~ấ~~u trúc|Có nhãn|Nhỏ|Lớn|Có||| |14|**Khuyến**<br>**nghị**|Kỹ<br>thuật|ML|**P**|**P**|**P**|**P**|**C **|**P**|**5 **|**P**| |14|**Khuyến**<br>**nghị**|Kỹ<br>thuật|DL|**P**|**C **|**P**|**P**|**P**|**C **|**4 **|**C **| |14|**Khuyến**<br>**nghị**|Kỹ<br>thuật|GenAI|**C **|**K**|**C **|**C **|**P**|**C **|**0 **|**K**|

### Đánh giá chung:

    * ML: phù hợp với các bài toán yêu cầu mô hình đơn giản, có khả năng giải thích tốt và dữ liệu có cấu trúc, điển hình như ra quyết định, giám sát, cải thiện hiệu suất, cá nhân hóa, dự báo, tự động hóa quy trình và khuyến nghị. Đây là những trường hợp mà dữ liệu đã được gán nhãn đầy đủ, số chiều không cao và yêu cầu giải thích thường được đặt ra rõ ràng. Tuy nhiên, ML không phù hợp với các bài toán có đặc điểm sinh nội dung, dữ liệu phi cấu trúc và không nhãn như tạo nội dung, tổng hợp nội dung,
    * trợ lý số, khám phá, phân tích hình ảnh hay truy xuất thông tin. ML cũng gặp hạn chế trong bài toán phát hiện, nơi dữ liệu phi cấu trúc và nhãn phức tạp khiến hiệu quả suy giảm.
      * DL: phù hợp với phần lớn các bài toán bao gồm cả sinh nội dung (tạo nội dung, tổng hợp nội dung, trợ lý số, khám phá),
    * lẫn các tác vụ dự đoán như ra quyết định, phát hiện, phân tích hình ảnh, truy xuất thông tin, cải thiện hiệu suất, cá nhân hóa, dự báo, tự động hóa quy trình và khuyến nghị. DL cần được cân nhắc trong các trường hợp yêu cầu giải thích rõ như giám sát, hoặc dữ liệu nhỏ như tự động hóa quy trình, khi mà DL có thể áp dụng được nhưng không tối ưu nếu thiếu lượng dữ liệu lớn hoặc tài nguyên tính toán phù hợp.
      * 18      GenAI: cho thấy hiệu quả vượt trội trong các bài toán sinh nội dung và tương tác ngôn ngữ tự nhiên như tạo nội dung, tổng hợp  nội dung, trợ lý số và khám phá – tất cả đều đạt điểm đánh giá tối đa. GenAI cũng có thể cân nhắc áp dụng ở các bài toán như phân tích hình ảnh, phát hiện và truy xuất thông tin, đặc biệt khi cần hỗ trợ trực quan hóa hoặc mở rộng khả năng phân tích dữ liệu phi cấu trúc. Tuy nhiên, GenAI hiện không phù hợp cho các bài toán truyền thống thiên về dự đoán định lượng và yêu cầu tính giải thích cao như ra quyết định, giám sát, cải thiện hiệu suất, cá nhân hóa, dự báo, tự động hóa quy trình và khuyến nghị, do đặc điểm sinh mô hình không rõ ràng, chi phí huấn luyện lớn và khó kiểm soát logic suy luận   19