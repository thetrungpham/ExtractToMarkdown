# Public_302

# Giới Thiệu

Observability (Khả Năng Quan Sát) là khả năng hiểu và chẩn đoán trạng thái nội tại của hệ thống thông qua dữ liệu được sinh ra như log, metrics và tracing.
Trong Kubernetes, observability giúp phát hiện nhanh sự cố và giảm thời gian khắc phục (MTTR).
Observability khác với Monitoring ở chỗ Monitoring chỉ tập trung vào việc theo dõi các chỉ số đã biết, trong khi Observability cung cấp góc nhìn toàn diện để tìm ra nguyên nhân gốc.

# Thành Phần Chính Của Observability

Các trụ cột chính của Observability trong Kubernetes gồm:

## Metrics

* Thu thập dữ liệu số học về hiệu năng cluster, node, pod.
* Giúp phát hiện các bất thường trong CPU, RAM, I/O.
* Công cụ phổ biến: Prometheus.

## Logging

* Ghi lại các sự kiện hệ thống và ứng dụng.
* Hỗ trợ phân tích nguyên nhân sự cố.
* Công cụ: ELK Stack, Loki.

## Tracing

* Theo dõi luồng request xuyên suốt microservices.
* Giúp phát hiện bottleneck.
* Công cụ: Jaeger, OpenTelemetry.

# Thách Thức Trong Kubernetes

* Hệ thống phân tán nhiều tầng.
* Multi-cluster làm phức tạp việc giám sát.
* Microservices tạo ra khối lượng log và dữ liệu khổng lồ.

# Công Cụ Observability Thường Dùng

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Công Cụ</th>
<th>Chức Năng</th>
<th>Ghi Chú</th>
</tr>
</thead>
<tbody>
<tr>
<td>Prometheus</td>
<td>Metrics</td>
<td>Giám sát số liệu cluster.</td>
</tr>
<tr>
<td>Grafana</td>
<td>Visualization</td>
<td>Biểu đồ, dashboard.</td>
</tr>
<tr>
<td>Jaeger / OpenTelemetry</td>
<td>Tracing</td>
<td>Theo dõi request phân<br>tán.</td>
</tr>
</tbody>
</table>
|---|---|---| |Prometheus|Metrics|Giám sát số liệu cluster.| |Grafana|Visualization|Biểu đồ, dashboard.| |Jaeger / OpenTelemetry|Tracing|Theo dõi request phân<br>tán.|    1

# Quy Trình Troubleshooting Kubernetes

Quy trình thường áp dụng khi xử lý sự cố Kubernetes:
1. Kiểm tra cluster và node.
2. Phân tích pod, container, network.
3. Đọc log, metrics và tracing.
4. Xác định nguyên nhân gốc (root cause).

# Best Practices

* Chuẩn hóa log & metrics.
* Thiết lập cảnh báo hợp lý.
* Tích hợp observability vào CI/CD.
* Tự động hóa khi có thể.
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>7. Observability vs Monitoring</th>
<th>Col2</th>
</tr>
</thead>
<tbody>
<tr>
<td>Monitoring</td>
<td>Observability</td>
</tr>
<tr>
<td>Theo dõi chỉ số định sẵn.</td>
<td>Khả năng phân tích sâu, tìm root<br>cause.</td>
</tr>
<tr>
<td>Giới hạn trong dữ liệu đã biết.</td>
<td>Khai thác dữ liệu hệ thống để trả lời<br>câu hỏi mới.</td>
</tr>
</tbody>
</table>
|---|---| |Monitoring|Observability| |Theo dõi chỉ số định sẵn.|Khả năng phân tích sâu, tìm root<br>cause.| |Giới hạn trong dữ liệu đã biết.|Khai thác dữ liệu hệ thống để trả lời<br>câu hỏi mới.|

# Kết Luận

Observability là yếu tố then chốt để vận hành Kubernetes hiệu quả. Bằng cách kết hợp Metrics, Logging và Tracing cùng các công cụ hỗ trợ, doanh nghiệp có thể phát hiện sự cố nhanh hơn và tối ưu hiệu năng hệ thống.
<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>9. Bảng Minh Họa Với Merge Cell</th>
<th>Col2</th>
<th>Col3</th>
<th>Col4</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pipeline Observability Trong Kubernetes</td>
<td>Pipeline Observability Trong Kubernetes</td>
<td>Pipeline Observability Trong Kubernetes</td>
<td>Pipeline Observability Trong Kubernetes</td>
</tr>
<tr>
<td>Metrics</td>
<td>Logging</td>
<td>Tracing</td>
<td>Ghi Chú</td>
</tr>
<tr>
<td>Thu Thập Dữ Liệu</td>
<td>Thu Thập Dữ Liệu</td>
<td>Thu Thập Dữ Liệu</td>
<td>Prometheus,<br>ELK, Jaeger</td>
</tr>
<tr>
<td>Phân Tích</td>
<td>Quan Sát</td>
<td>Tìm Root Cause</td>
<td>Giảm MTTR</td>
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
<th>10. Bảng Pipeline Quan Sát (Phiên Bản Dài)</th>
<th>Col2</th>
<th>Col3</th>
<th>Col4</th>
<th>Col5</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pipeline Observability Mở Rộng</td>
<td>Pipeline Observability Mở Rộng</td>
<td>Pipeline Observability Mở Rộng</td>
<td>Pipeline Observability Mở Rộng</td>
<td>Pipeline Observability Mở Rộng</td>
</tr>
<tr>
<td>Bước</td>
<td>Metrics</td>
<td>Logging</td>
<td>Tracing</td>
<td>Ghi Chú</td>
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
<th>Th u Thập Dữ<br>Liệu</th>
<th>Nod<br>e<br>Exporter</th>
<th>Fl uentd / Loki</th>
<th>Jaeger Agent</th>
<th>Các agent th u<br>thập dữ liệu<br>từ cl uster</th>
</tr>
</thead>
<tbody>
<tr>
<td>Lưu Trữ</td>
<td>Prometheus TSDB<br>Elasticsearch / Loki</td>
<td>Prometheus TSDB<br>Elasticsearch / Loki</td>
<td>Jaeger<br>Collector</td>
<td>Kho dữ liệu<br>trung tâm</td>
</tr>
<tr>
<td>Phân Tích</td>
<td>PromQL</td>
<td>Kibana /<br>Grafana Loki</td>
<td>Jaeger Query</td>
<td>Phân tích dữ<br>liệu từ nhiều<br>nguồn</td>
</tr>
<tr>
<td>Trực Quan<br>Hóa</td>
<td>Grafana<br>Dashboards</td>
<td>Kibana<br>Dashboard</td>
<td>Jaeger UI</td>
<td>Cung cấp<br>dashboard<br>cho DevOps</td>
</tr>
<tr>
<td>Hành Động<br>& Tối Ưu</td>
<td>Alertmanager</td>
<td>Cảnh báo log<br>bất thường</td>
<td>Trace-based<br>alerts</td>
<td>Giảm MTTR,<br>cải thiện SLO</td>
</tr>
</tbody>
</table>
|---|---|---|---| |Pipeline Observability Trong Kubernetes|Pipeline Observability Trong Kubernetes|Pipeline Observability Trong Kubernetes|Pipeline Observability Trong Kubernetes| |Metrics|Logging|Tracing|Ghi Chú| |Thu Thập Dữ Liệu|Thu Thập Dữ Liệu|Thu Thập Dữ Liệu|Prometheus,<br>ELK, Jaeger| |Phân Tích|Quan Sát|Tìm Root Cause|Giảm MTTR|   |---|---|---|---|---| |Pipeline Observability Mở Rộng|Pipeline Observability Mở Rộng|Pipeline Observability Mở Rộng|Pipeline Observability Mở Rộng|Pipeline Observability Mở Rộng| |Bước|Metrics|Logging|Tracing|Ghi Chú|    2                                |---|---|---|---|---| |Lưu Trữ|Prometheus TSDB<br>Elasticsearch / Loki|Prometheus TSDB<br>Elasticsearch / Loki|Jaeger<br>Collector|Kho dữ liệu<br>trung tâm| |Phân Tích|PromQL|Kibana /<br>Grafana Loki|Jaeger Query|Phân tích dữ<br>liệu từ nhiều<br>nguồn| |Trực Quan<br>Hóa|Grafana<br>Dashboards|Kibana<br>Dashboard|Jaeger UI|Cung cấp<br>dashboard<br>cho DevOps| |Hành Động<br>& Tối Ưu|Alertmanager|Cảnh báo log<br>bất thường|Trace-based<br>alerts|Giảm MTTR,<br>cải thiện SLO|

# Phân Tích Chi Tiết Về Observability Trong Kubernetes

Observability trong Kubernetes không chỉ đơn thuần là giám sát (monitoring).
Nó tập trung vào khả năng hiểu rõ trạng thái bên trong của hệ thống thông qua dữ liệu quan sát được từ bên ngoài. Điều này đặc biệt quan trọng đối với các hệ thống microservices, nơi hàng chục đến hàng trăm dịch vụ tương tác phức tạp với  nhau.
Ba trụ cột chính của Observability gồm có Metrics, Logging và Tracing. Metrics cho phép thu thập các số liệu định lượng như CPU, bộ nhớ, số lượng request, độ trễ. Logging cung cấp ngữ cảnh chi tiết về sự kiện trong hệ thống. Tracing giúp theo dõi hành trình của một request qua nhiều dịch vụ khác nhau, nhờ đó phát hiện các điểm nghẽn hoặc nguyên nhân gây lỗi.
Khi triển khai Observability trong Kubernetes, tổ chức sẽ đối mặt với nhiều thách thức: 1) khối lượng dữ liệu khổng lồ; 2) chi phí lưu trữ và phân tích; 3) sự phức tạp trong tích hợp nhiều công cụ; 4) yêu cầu về kỹ năng của đội ngũ vận hành.
Để giải quyết các thách thức này, cần có kiến trúc Observability hiệu quả. Điển hình là sử dụng Prometheus để thu thập metrics, kết hợp Grafana để trực quan hóa, dùng ELK stack hoặc Loki để xử lý log, và Jaeger hoặc OpenTelemetry để thực hiện tracing. Khi các công cụ này hoạt động phối hợp, DevOps có thể nhanh chóng xác định nguyên nhân sự cố.
Một quy trình troubleshooting điển hình trong Kubernetes thường bắt đầu bằng việc kiểm tra cluster và node, sau đó đi sâu vào trạng thái pod và container. Nếu vấn đề không rõ ràng, nhóm vận hành sẽ phân tích log, metrics và tracing để tìm ra gốc rễ (root cause). Việc này giúp giảm MTTR (Mean Time To Repair) và nâng cao SLO/SLI cho dịch vụ.
Best Practices cho Observability trong Kubernetes bao gồm: 1) Chuẩn hóa log và metrics; 2) Sử dụng nhãn (label) thống nhất; 3) Tích hợp Observability vào   3      pipeline CI/CD; 4) Tự động hóa cảnh báo; 5) Liên tục đánh giá và tối ưu hóa chi phí lưu trữ dữ liệu.
Một ví dụ thực tế: khi ứng dụng microservice gặp lỗi 'Pod CrashLoopBackOff',
metrics có thể cho thấy pod liên tục khởi động lại, log cung cấp thông tin về lỗi ứng dụng, trong khi tracing cho thấy request dừng lại ở một dịch vụ phụ thuộc.
Nhờ quan sát đầy đủ, đội ngũ DevOps nhanh chóng sửa lỗi cấu hình và khôi phục dịch vụ.

# So Sánh Observability và Monitoring

<table border="1" cellpadding="6" cellspacing="0">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Khía Cạnh</th>
<th>Monitori<br>ng</th>
<th>Ob servability</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mục Tiêu</td>
<td>Theo dõi tình trạng hệ<br>thống</td>
<td>Hiểu rõ nguyên nhân<br>bên trong</td>
</tr>
<tr>
<td>Dữ Liệu</td>
<td>Chủ yếu metrics cơ bản</td>
<td>Metrics, Logging,<br>Tracing</td>
</tr>
<tr>
<td>Công Cụ</td>
<td>Nagios, Zabbix</td>
<td>Prometheus, Grafana,<br>Jaeger, ELK</td>
</tr>
<tr>
<td>Phạm Vi</td>
<td>Hệ thống tổng thể</td>
<td>Từng dịch vụ, request cụ<br>thể</td>
</tr>
</tbody>
</table>
|---|---|---| |Mục Tiêu|Theo dõi tình trạng hệ<br>thống|Hiểu rõ nguyên nhân<br>bên trong| |Dữ Liệu|Chủ yếu metrics cơ bản|Metrics, Logging,<br>Tracing| |Công Cụ|Nagios, Zabbix|Prometheus, Grafana,<br>Jaeger, ELK| |Phạm Vi|Hệ thống tổng thể|Từng dịch vụ, request cụ<br>thể|    4