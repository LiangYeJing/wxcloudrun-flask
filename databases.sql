-- 用户表
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- 用户 ID
  openid VARCHAR(255) NOT NULL,       -- 用户 OpenID
  nickname VARCHAR(255) NOT NULL,     -- 用户昵称
  avatar_url VARCHAR(255) NOT NULL,   -- 用户头像 URL
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 用户注册时间
);

-- 情侣关系表
-- 创建情侣关系表
CREATE TABLE couples (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- 情侣关系 ID
  user1_id INT NOT NULL,              -- 用户 1 的 ID (外键)
  user2_id INT NOT NULL,              -- 用户 2 的 ID (外键)
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- 绑定时间
  FOREIGN KEY (user1_id) REFERENCES users(id),    -- 外键约束，关联到用户表
  FOREIGN KEY (user2_id) REFERENCES users(id)     -- 外键约束，关联到用户表
);

-- 为情侣关系表创建索引
CREATE INDEX idx_user1_id ON couples (user1_id);
CREATE INDEX idx_user2_id ON couples (user2_id);


-- 图片表
CREATE TABLE images (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- 图片 ID
  couple_id INT NOT NULL,             -- 情侣关系 ID (外键)
  image_url VARCHAR(255) NOT NULL,    -- 图片的 URL
  uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- 上传时间
  FOREIGN KEY (couple_id) REFERENCES couples(id)  -- 外键约束，关联到情侣关系表
);

CREATE INDEX idx_couple_id_images ON images (couple_id);


-- 情书表
CREATE TABLE love_letters (
  id INT AUTO_INCREMENT PRIMARY KEY,      -- 情书 ID
  sender_id INT NOT NULL,                 -- 发送者的用户 ID (外键)
  receiver_id INT NOT NULL,               -- 接收者的用户 ID (外键)
  content TEXT NOT NULL,                  -- 情书内容
  sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- 发送时间
  status ENUM('sent', 'read', 'deleted') DEFAULT 'sent', -- 情书状态
  FOREIGN KEY (sender_id) REFERENCES users(id),       -- 发送者外键
  FOREIGN KEY (receiver_id) REFERENCES users(id)     -- 接收者外键
);

CREATE INDEX idx_sender_id ON love_letters (sender_id);
CREATE INDEX idx_receiver_id ON love_letters (receiver_id);

-- 情书回复表
CREATE TABLE love_letter_replies (
  id INT AUTO_INCREMENT PRIMARY KEY,      -- 回复 ID
  letter_id INT NOT NULL,                 -- 被回复的情书 ID (外键)
  sender_id INT NOT NULL,                 -- 回复者的用户 ID (外键)
  content TEXT NOT NULL,                  -- 回复内容
  sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- 回复时间
  status ENUM('sent', 'read', 'deleted') DEFAULT 'sent', -- 回复状态
  FOREIGN KEY (letter_id) REFERENCES love_letters(id), -- 被回复的情书 ID
  FOREIGN KEY (sender_id) REFERENCES users(id)         -- 回复者外键
);

CREATE INDEX idx_letter_id ON love_letter_replies (letter_id);
CREATE INDEX idx_sender_id_replies ON love_letter_replies (sender_id);
