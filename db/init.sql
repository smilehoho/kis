/*
{
  "access_token":"*****",
  "access_token_token_expired":"2023-01-10 10:50:00",
  "token_type":"Bearer",
  "expires_in":86400
}
*/
CREATE TABLE oauth2
  (
    oauth2_id INTEGER PRIMARY KEY AUTOINCREMENT,
     access_token               TEXT,
     access_token_token_expired TEXT,
     token_type                 TEXT,
     expires_in                 INTEGER,
     status TEXT DEFAULT 'active',
     created_at                 TEXT DEFAULT CURRENT_TIMESTAMP
  ); 

  CREATE TABLE oauth2 (
  oauth2_id int primary key autoincrement, 
  access_token TEXT, access_token_token_expired TEXT, 
  token_type TEXT, expires_in INT, created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
