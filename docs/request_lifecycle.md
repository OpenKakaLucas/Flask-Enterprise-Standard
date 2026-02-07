Client
  ↓
Rate Limit
  ↓
JWT Auth
  ↓
Validation
  ↓
Controller
  ↓
Service
  ↓
DB
  ↓
Response Formatter
  ↓
Logging + Metrics

所有横切能力通过 before_request / after_request 实现