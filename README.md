# search algorithm

## input:
arr: mảng
target: mục tiêu
## output
vị trí của mục tiêu (bắt đầu của mảng là 0)

1. Linear Search 
- Đây là thuật toán đơn giản nhất. Mỗi phần tử đều kiểm tra và nếu tìm thấy bất kỳ kết nối nào thì phần tử cụ thể đó được trả về, nếu không thấy thì quá trình tìm kiếm tiếp tục diễn ra cho tới khi tìm kiếm hết dữ liệu
2. Binary Search 
- Thuật toán tìm kiếm nhị phâm, còn gọi là tìm kiếm nửa khoảng
- Sử dụng đệ quy
3. Ternary Search 
- Tương tự thuật toán tìm kiếm trên, nhưng là tam phân
4. Interpolation Search 
- Dựa trên Binary Search, thay đổi vị trí so sánh bằng phép tính nội suy như sau:
Search = left + (right - left) * 1/2
Trong công thức trên chúng ta sẽ thay giá trị 1/2 bằng biểu thức sau:
(X - T[left]) / (T[right] - T[left])