# Vector Evidence review site

Original dashboard on port 5500 is served from `D:\Project\ชวกม.2\EDOK_NUI\VECTOR_EVIDENCE` and remains separate.
This directory is the independent review copy served only on `127.0.0.1:5501`.

Open: http://127.0.0.1:5501/EDOK_NUI/VECTOR_EVIDENCE/VECTOR_EVIDENCE_DASHBOARD.html

To start again after reboot, run from PowerShell:

```powershell
python -m http.server 5501 --bind 127.0.0.1 --directory "D:\Project\ชวกม.2\VECTOR_EVIDENCE_REVIEW_SITE"
```

The review generator defaults to this site's `EDOK_NUI\VECTOR_EVIDENCE` folder and reads the original counts source. Pass `VECTOR_MANIFEST_PATH` to generate from a manifest. Do not run the original project's generator to update this review site; it targets the original folder.