from build_court_dossier_smart_cropped import counts
print('Loaded counts:', len(counts))
for i, c in enumerate(counts):
    print(f"{i+1}. {c['count_no']}: {c['count_title'][:35]} | img: {c['img_p1']}")
