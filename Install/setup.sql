use hepatica;

create table `staff_account_DB` (
  `id` int unsigned not null auto_increment primary key,
  `staff_name` text not null, -- 직원 이름
  `phone` text not null, -- 직원 전화번호
  `email` text not null, -- 직원 이메일
  `work_times` text null, -- 직원 업무 시간대
  `password` varchar(255) null -- 직원 비밀번호
);

create table `staff_work_status_DB` (
  `id` int unsigned not null auto_increment primary key,
  `staff_name` text not null, -- 직원 이름
  `work_result` BOOLEAN null, -- 직원 출근 결과
  `attendance_status` text null -- 직원 출근 시간
);

create table `product_info_DB` (
  `id` int unsigned not null auto_increment primary key,
  `product name` text null, -- 상품 이름
  `info_url` text null  -- 상품 상세설명 파일
);

create table `account_book_DB` (
  `id` int unsigned not null auto_increment primary key,
  `product` text null, -- 제품 명
  `staff` text null, -- 판매자
  `payment` BOOLEAN null -- 결제 방식 True : 카드, 계좌이체 등, False : 현금
);

CREATE USER 'hepatica_db'@'%' IDENTIFIED BY 'hepatica0427';
GRANT ALL PRIVILEGES ON hepatica.* TO 'hepatica'@'%';
FLUSH PRIVILEGES;