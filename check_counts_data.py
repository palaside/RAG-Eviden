from build_court_dossier_smart_cropped import counts
print(f"Total counts loaded: {len(counts)}")
for i, c in enumerate(counts[:5]):
    print(f"\n--- Count {i+1} ---")
    for k, v in c.items():
        if k not in ['img_data', 'p2_img_data', 'b64_img', 'b64_p2_img']:
            val_str = str(v)
            if len(val_str) > 100:
                val_str = val_str[:100] + '...'
            print(f"  {k}: {val_str}")
