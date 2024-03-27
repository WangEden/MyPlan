# Matlab基本语法

### 语法基础

1. 元胞数组

```matlab
A = cell(1, 6)
A{2} = eye(3)
A{5} = magic(5)
B = A{5}
```

2. 结构体

```matlab
books = struct(
	'name', {{'Machine Learning', 'Data Mining'}},
	'price', [30, 40]
)
books.name
books.name(1)
books.name{1}
```

3. 矩阵

```matlab
A = [1 2 3 4; 5 6 7 8]
B = [4 3 2 1; 8 7 6 5]
C = A * B' % 乘
D = A .* B % 点乘
E = A / B
F = A ./ B

G = magic(5) % 生成随机5x5的矩阵
[i, j] = find(G > 20) % 返回G中大于20的数的下标
R = rand(4, 6) % 生成四行六列的随机矩阵
```

4. 流程控制

```matlab
% 判断
if xxx
	xxx;
else
	xxx;
end

% for循环
for m = 1:20
	xxx;
end

% while循环
while xxx:
	xxx
end

% switch case
switch key
	case v1
		xxx
	case v2
		xxx
	otherwise
		xxx
end
```

5. 脚本文件和函数文件

脚本文件： xxx.m

函数文件： myFunction.m

```matlab
function output = myFunction(input_)

xxx
output = xxx;
```



### 常用函数查询

- 阶乘
  ```a = factorial(30)```
  
- 连乘

  ```a = prod(1:30)```

-  输入输出

  ```matlab
  a = input('Enter a number');
  disp('Success')
  ```

- 保存图片

  ```matlab
  print('-depsc', '-tiff', '-r300', 'picture1')
  ```

- 判断是否相等

  ```matlab
  isequal(v1, v2)  —> 1 or 0
  ```

- 格式化打印

  ```matlab
  S = sprintf（"%s xxx %d xxx", [str], [int])
  disp(S)
  
  或者 直接格式化输出
  fprintf（"%s xxx %d xxx", [str], [int]）
  ```

  



### 绘图

1. 二维平面绘图

```matlab
% 画一个图
x = 0: 0.01 :  2*pi % 横坐标范围
y = sin(x)
figure % 创建画布
plot(x, y) % 根据横纵坐标画图
title('y = sin(x)')
xlabel('x')
ylabel('sin(x)')
xlim([0 2*pi]) % 设置画布中绘制的横坐标范围

% 共用一个横坐标画两个图
x = 0:0.01:20
y1 = 200 * exp(-0.05 * x) .* sin(x)
y2 = 0.8 * exp(-0.5 * x) .* sin(10 * x)
figure
[AX, H1, H2] = plotyy(x, y1, x, y2, 'plot')
set(get(AX(1), 'Ylabel'), 'String', 'Slow Decay') % 更改y标签
set(get(AX(2), 'Ylabel'), 'String', 'Fast Decay') % 更改y标签
xlabel('Time (\musec)') % 希腊字母： \mu —> μ
title('Multi xx')
set(H1, 'LineStyle', '--') % 设置图形一为虚线
set（H2， 'LineStyle', ':'） % 设置图形二为另一种虚线
```

2. 三维立体绘图

```matlab
% 螺旋线
t = 0:pi/50:10*pi
plot3(sin(t), cos(t), t) % 画3D图
xlabel('sin(t)')
ylabel('cos(t)')
zlabel('t')
grid on % 开启网格
axis square
```



### 文件导入

1. mat文件

```matlab
save data.mat x y1 y2
load data.mat % 导入到工作区
```

2. txt文件

```matlab
M = importdata('myfile.txt')
S = M.data
save 'data.txt' S -ascii
I = load('data.txt')
```

3. xls文件

```matlab
xlswrite('data.xls', S) % 或者xlsx
W = xlsread('data.xls')
```

4. csv文件

```matlab
csvwrite('data.csv', S)
W = csvread('data.csv')
```

### 快捷键

1. 切换Editor窗口和command窗口、切换各个工作窗口

   ```
   Ctrl+(Shift)+0
   Ctrl+Tab
   ```

2. 

![image-20240124134251566](./assets/image-20240124134251566.png)
