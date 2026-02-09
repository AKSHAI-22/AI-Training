posts = [
    ["#ai", "#ml", "#python"],
    ["#python", "#datascience", "#ai"],
    ["#ai", "#python", "#deeplearning"]
]
all_tags=set()
for p in posts:
    all_tags=all_tags.union(p)
common=set(posts[0])

for p in posts[1:]:
    common=common.intersection(p)
print("All unique hashtags:", all_tags)
print("Hashtags in every post:", common)
