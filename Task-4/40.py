documents = [
    {"doc_id": 1, "tags": ["ai", "ml", "python"]},
    {"doc_id": 2, "tags": ["ai", "python"]},
    {"doc_id": 3, "tags": ["ai", "python", "data"]},
    {"doc_id": 4, "tags": []}
]

invalid_docs = []

for d in documents:
    if not d["tags"]:
        invalid_docs.append(d["doc_id"])

print("Documents with no tags:", invalid_docs)

first = True

for d in documents:
    if d["tags"]:
        if first:
            common_tags = set(d["tags"])
            first = False
        else:
            common_tags = common_tags & set(d["tags"])

print("Tags in every document:", common_tags)
