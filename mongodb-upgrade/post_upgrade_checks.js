// Confirm version after upgrade
db.version()

// Confirm FCV
db.adminCommand({ getParameter: 1, featureCompatibilityVersion: 1 })

// Basic collection checks
use appdb
db.orders.countDocuments()
db.customers.countDocuments()
