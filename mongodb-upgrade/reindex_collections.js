use appdb

const collections = ["orders", "customers"]

collections.forEach(col => {
  print("Reindexing:", col)
  db.getCollection(col).reIndex()
})
