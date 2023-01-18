DROP TABLE IF EXISTS oauth2;
CREATE TABLE oauth2 (
  oauth2_id INTEGER PRIMARY KEY AUTOINCREMENT,
  access_token TEXT,
  access_token_token_expired TEXT,
  token_type TEXT,
  expires_in INTEGER,
  status TEXT DEFAULT 'active',
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO oauth2 (
    oauth2_id,
    access_token,
    access_token_token_expired,
    token_type,
    expires_in,
    status,
    created_at
  )
VALUES ();
INSERT INTO oauth2 (
    oauth2_id,
    access_token,
    access_token_token_expired,
    token_type,
    expires_in,
    status,
    created_at
  )
VALUES (
    oauth2_id :INTEGER,
    'access_token:TEXT',
    'access_token_token_expired:TEXT',
    'token_type:TEXT',
    expires_in :INTEGER,
    'status:TEXT',
    'created_at:TEXT'
  );
  
SELECT oauth2.oauth2_id,
  oauth2.access_token,
  oauth2.access_token_token_expired,
  oauth2.token_type,
  oauth2.expires_in,
  oauth2.status,
  oauth2.created_at
FROM oauth2;