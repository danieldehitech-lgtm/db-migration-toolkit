// Check MongoDB version
db.version()

// Feature Compatibility Version
db.adminCommand({ getParameter: 1, featureCompatibilityVersion: 1 })

// Server status
db.adminCommand({ serverStatus: 1 })

// Replica set status (if applicable)
try {
  rs.status()
} catch (e) {
  print("Standalone MongoDB")
}
