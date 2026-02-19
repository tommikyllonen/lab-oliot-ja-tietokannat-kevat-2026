.mode table
.headers ON

CREATE TABLE metric (
  dev_id TEXT,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  cpu_temp NUMBER NOT NULL,
  gps_location TEXT,

  FOREIGN KEY (dev_id) REFERENCES device(mac)
);