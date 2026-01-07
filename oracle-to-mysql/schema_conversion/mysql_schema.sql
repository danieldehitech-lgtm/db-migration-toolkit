CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  full_name   VARCHAR(200) NOT NULL,
  email       VARCHAR(255),
  created_at  DATETIME NOT NULL
);

CREATE TABLE orders (
  order_id     INT PRIMARY KEY,
  customer_id  INT NOT NULL,
  order_total  DECIMAL(12,2),
  order_status VARCHAR(30),
  created_at   DATETIME NOT NULL,
  INDEX idx_orders_customer (customer_id)
);
